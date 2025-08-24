#!/bin/bash

echo "Blender Add-on Development Template Setup (macOS/Linux)"
echo "========================================================"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.10 or later"
    exit 1
fi

# Check Python version
python_version=$(python3 --version | grep -oE '[0-9]+\.[0-9]+')
major_version=$(echo $python_version | cut -d. -f1)
minor_version=$(echo $python_version | cut -d. -f2)

if [ "$major_version" -lt 3 ] || ([ "$major_version" -eq 3 ] && [ "$minor_version" -lt 10 ]); then
    echo "Error: Python 3.10 or later is required (found $python_version)"
    exit 1
fi

echo "✓ Python $python_version found"

echo "Creating Python virtual environment..."
python3 -m venv .venv
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment"
    exit 1
fi

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing dependencies..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

# Update VS Code settings for Unix systems
echo "Updating VS Code settings for Unix systems..."
if [ -f ".vscode/settings.json" ]; then
    # Create a backup
    cp .vscode/settings.json .vscode/settings.json.bak
    
    # Update settings for Unix
    sed -i.tmp 's|"python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe", // Windows|// "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe", // Windows|g' .vscode/settings.json
    sed -i.tmp 's|// "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",     // macOS/Linux|"python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",     // macOS/Linux|g' .vscode/settings.json
    sed -i.tmp 's|"${workspaceFolder}/.venv/Lib/site-packages", // Windows path|// "${workspaceFolder}/.venv/Lib/site-packages", // Windows path|g' .vscode/settings.json
    sed -i.tmp 's|// "${workspaceFolder}/.venv/lib/python3.10/site-packages", // macOS/Linux path (adjust Python version if needed)|"${workspaceFolder}/.venv/lib/python3.10/site-packages", // macOS/Linux path (adjust Python version if needed)|g' .vscode/settings.json
    sed -i.tmp 's|"path": "${workspaceFolder}/.venv/Scripts/python.exe" // Windows|// "path": "${workspaceFolder}/.venv/Scripts/python.exe" // Windows|g' .vscode/settings.json
    sed -i.tmp 's|// "path": "${workspaceFolder}/.venv/bin/python"      // macOS/Linux|"path": "${workspaceFolder}/.venv/bin/python"      // macOS/Linux|g' .vscode/settings.json
    
    # Remove temporary files
    rm -f .vscode/settings.json.tmp
    
    echo "✓ VS Code settings updated for Unix systems"
fi

echo ""
echo "========================================"
echo "🎉 Setup completed successfully!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Install VS Code extensions:"
echo "   - Python (by Microsoft)"
echo "   - Blender Development (by Jacques Lucke)"
echo ""
echo "2. Update Blender path in .vscode/settings.json:"
echo "   - Edit 'blender.blenderExecutable.path'"
echo "   - Set it to your Blender executable path"
echo ""
echo "3. Open VS Code in this directory:"
echo "   code ."
echo ""
echo "4. Start developing your Blender add-on!"
echo "   - Edit files in the 'addon/' directory"
echo "   - Use Ctrl+Shift+P -> 'Blender: Start' to launch Blender"
echo "   - Enable your add-on in Blender's preferences"
echo ""