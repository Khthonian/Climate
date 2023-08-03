#!/bin/bash

APP_NAME="climate"

# Add the path to the Go binary
export PATH=$PATH:/usr/local/go/bin

# Print the PATH variable for debugging
echo "PATH: $PATH"

# Check if the script is run as root
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root (use sudo)." 1>&2
   exit 1
fi

# Check if an executable with the same name exists in the user's path
if command -v $APP_NAME > /dev/null; then
  echo "An executable named '$APP_NAME' is already in your PATH. Please choose a different name or make sure you're not overwriting something important."
  exit 1
fi

# Warning message
echo "WARNING: This script will install '$APP_NAME' system-wide."
read -p "Do you want to continue? (y/n): " confirm

if [ "$confirm" != "y" ]; then
  echo "Installation cancelled."
  exit 0
fi

# Compile the program
echo "Compiling '$APP_NAME'..."
go build -o $APP_NAME

# Hash the binary
HASH=$(sha256sum "$APP_NAME" | awk '{ print $1 }')

# Move to /usr/local/bin
echo "Installing '$APP_NAME' to /usr/local/bin..."
mv $APP_NAME /usr/local/bin/

# Make it executable
echo "Making '$APP_NAME' executable..."
chmod +x /usr/local/bin/$APP_NAME

# Write uninstall script with the hash for verification
cat <<EOL > uninstallClimate.sh
#!/bin/bash

# Hash of the installed file
INSTALLED_HASH="$HASH"

# Destination for the binary
DESTINATION="/usr/local/bin/$APP_NAME"

# Hash the currently installed binary
CURRENT_HASH=\$(sha256sum "\$DESTINATION" | awk '{ print \$1 }')

# Verify the hash
if [ "\$INSTALLED_HASH" != "\$CURRENT_HASH" ]; then
  echo "Hash mismatch. The file at \$DESTINATION may not be the correct taskit binary."
  exit 1
fi

# If hash matches, uninstall
rm "\$DESTINATION"
echo "$APP_NAME uninstalled successfully."

# Delete this uninstall script
echo "Removing uninstall script..."
rm -- "uninstallClimate.sh"

echo "Uninstall complete."

EOL

# Make the uninstall script executable
chmod +x uninstallClimate.sh

echo "'$APP_NAME' installed successfully. You can now use it from anywhere! Run 'uninstallClimate.sh' to uninstall."
