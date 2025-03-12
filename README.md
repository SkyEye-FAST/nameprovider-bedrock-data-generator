# NameProvider Data Generator (Bedrock)

A Python script that generates Lua data for [Module:NameProviderBedrock](https://zh.minecraft.wiki/w/Module:NameProviderBedrock) on Minecraft Wiki (ZH). The script downloads Minecraft Bedrock Edition language files and converts them into the required Lua data format.

## Features

- Downloads language files from [Mojang/bedrock-samples](https://github.com/Mojang/bedrock-samples)
- Processes both main and preview branches for different game versions

## Requirements

- Python 3.x
- `requests` library
- `mclang` library

## Usage

1. Ensure all required libraries are installed:

   ``` shell
   pip install requests mclang
   ```

2. Run the script:

   ``` shell
   python main.py
   ```

3. The script will generate two output files:
   - `output_main.lua` - Contains language data from the `main` branch
   - `output_preview.lua` - Contains language data from the `preview` branch

## Output Format

The generated Lua files follow the format required by Module:NameProviderBedrock:

- Version metadata for tracking data freshness
- Generation timestamp
- Language data organized as key-value pairs with translations in multiple languages

## License

The script is released under the [Apache 2.0 license](LICENSE).

``` text
  Copyright 2025 SkyEye_FAST

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
```
