import json
import os
import sys
from PyQt6.QtWidgets import QApplication
from qt_material import apply_stylesheet
from auratext.Core.window import Window

"""
This file includes the code to run the app. It also scans if the app is being opened for the first time in order to show the
setup instructions.
"""

local_app_data = os.path.join(os.path.expanduser('~'), 'Library', 'Application Support', 'AuraText')

# Ensure the directory exists
if not os.path.exists(local_app_data):
    os.makedirs(local_app_data)

# Load configuration files
config_path = os.path.join(local_app_data, 'data', 'config.json')
theme_path = os.path.join(local_app_data, 'data', 'theme.json')

if os.path.exists(config_path):
    with open(config_path, 'r') as config_file:
        _config = json.load(config_file)
else:
    _config = {}

if os.path.exists(theme_path):
    with open(theme_path, 'r') as theme_file:
        _theme = json.load(theme_file)
else:
    _theme = {"theming": "default", "material_type": "default"}

def main():
    app = QApplication(sys.argv)
    if _theme["theming"] == "material":
        theme = _theme["material_type"] + ".xml"
        apply_stylesheet(app, theme=theme)
    ex = Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
