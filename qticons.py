from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

app = QApplication([])

# Set the icon theme to the current system theme
QIcon.setThemeName(QIcon.themeName())

# Retrieve all available icon names
icon_names = QIcon.themeSearchPaths()

# Print all icon names
for icon_name in icon_names:
    print(icon_name)
