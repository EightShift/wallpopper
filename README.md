# WallPopper

WallPopper is a Python application designed to set HTML wallpapers across multiple monitors using CEF for Windows.

## Installation

To install WallPopper, follow these steps:

1. Clone the repository:
```
git clone https://github.com/EightShift/wallpopper.git
cd wallpopper
```
2. Install the dependencies listed in `requirements.txt`:
```
pip install -r requirements.txt
```

## Usage

1. Default wallpapers are stored in the `wallpapers/` directory.

2. Configure the wallpaper source path by editing `config.json`:
```json
{
    "source": "./wallpapers/metaballs"
}
```
3. Run WallPopper.py to set the wallpapers:
```
python WallPopper.py
```

## Python Version Compatibility

WallPopper is compatible with Python up to version 3.9. It may not work correctly with newer versions.

## Future Development

GUI functionality is planned for future updates to enhance user interaction and configuration options.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
```
This README.md provides basic instructions for installation, usage, planned features, dependencies, and licensing for your WallPopper project on GitHub. Adjust paths, descriptions, and sections as needed to fit your project's specifics.
```