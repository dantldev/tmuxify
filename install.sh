#!/bin/bash

# Define the installation directory
INSTALL_DIR="/usr/local/bin"

# Define the main script name
SCRIPT_NAME="tmuxify.py"

# Download the script from the repository
echo "Downloading Tmuxify..."
curl -fsSL https://raw.githubusercontent.com/dantldev/tmuxify/main/$SCRIPT_NAME -o $SCRIPT_NAME

echo "Installing Tmuxify to $INSTALL_DIR"

# Move the script to the installation directory
if mv "$SCRIPT_NAME" "$INSTALL_DIR/tmuxify"; then
  chmod +x "$INSTALL_DIR/tmuxify"
  echo "Installation successful!"
  echo "You can now run 'tmuxify' from anywhere in your terminal."
else
  echo "Installation failed. You might need to run this script with sudo."
fi
