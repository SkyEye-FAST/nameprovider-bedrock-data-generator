"""A script to download and convert Minecraft Bedrock language files into Lua data format."""

from datetime import datetime, timezone

import mclang
import requests

# Character escape mapping
ESCAPES = {
    '"': '\\"',
    "\\": "\\\\",
    "\n": "\\n",
    "\r": "\\r",
    "\t": "\\t",
    "\b": "\\b",
    "\f": "\\f",
}

if __name__ == "__main__":
    # List of language codes and branches
    lang_codes = ["en_US", "zh_CN", "zh_TW"]
    branches = ["main", "preview"]

    for branch in branches:
        print(f"Processing {branch} branch...")

        # Get version info for current branch
        version_url = (
            f"https://raw.githubusercontent.com/Mojang/bedrock-samples/{branch}/version.json"
        )
        version_response = requests.get(version_url)
        if version_response.status_code != 200:
            print(f"Warning: Failed to fetch version information for {branch} branch")
            version_info = {"latest": {"version": "unknown"}}
        else:
            version_info = version_response.json()
            print(f"Got version info for {branch} branch: {version_info['latest']['version']}")

        lang_data = []
        # Download and parse all language files
        for lang_code in lang_codes:
            url = f"https://raw.githubusercontent.com/Mojang/bedrock-samples/{branch}/resource_pack/texts/{lang_code}.lang"
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Warning: Failed to download {lang_code}.lang from {branch} branch")
                continue
            print(f"Successfully downloaded {lang_code}.lang")
            lang_data.append(mclang.loads(response.text))

        if not lang_data:
            print(f"Skipping {branch} branch - no language files were downloaded")
            continue

        # Generate Lua formatted output
        result = []
        keys = lang_data[0].keys()

        # Add header with version and timestamp
        current_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
        version = version_info["latest"]["version"]

        header = [
            f"-- version: {version}",
            f"-- time: {current_time}",
            "return {",
            f"\t[ '_meta.version' ] = \"{version}\",",
        ]

        for key in keys:
            # Handle string escaping
            escaped_key = "".join(ESCAPES.get(c, c) for c in key)
            values = [lang.get(key, "") for lang in lang_data]
            escaped_values = ["".join(ESCAPES.get(c, c) for c in v) for v in values]
            values_str = ", ".join(f'"{v}"' for v in escaped_values)
            result.append(f"\t[ '{escaped_key}' ] = {{ {values_str} }}")

        # Write to branch-specific file
        output_file = f"output_{branch}.lua"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(header))
            f.write("\n")
            f.write(",\n".join(result))
            f.write("\n}")
        print(f"Generated {output_file}")
