# Climate
This Python tool is a simple command-line weather app, to allow a user to input a location and receive the weather conditions and temperature.

## Usage
### Check Weather Conditions
```bash
climate -w {location}
```

## Installation
1. Clone this repository or download the source code.
2. Run the `installClimate.sh` script with `sudo` permissions:
```bash
sudo bash installClimate.sh
```
3. Follow the on-screen prompts to complete installation.

## Uninstallation
Once `installClimate.sh` has been run, `uninstallClimate.sh` will automatically be generated. This script uses hash validation to authenticate that the script does not unintentionally remove directory content that happens to also share the name `climate`. This script can be generated into the original download directory and can be run using:
```bash
sudo bash uninstallClimate.sh
```

## License
This project is licensed under the [MIT License](LICENSE).