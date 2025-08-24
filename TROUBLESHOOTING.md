# Troubleshooting Guide

This guide covers common issues you might encounter when setting up or using the Blender Add-on Development Template.

## Setup Issues

### Python Virtual Environment

**Problem**: `python -m venv .venv` fails
- **Solution**: Ensure Python 3.10+ is installed and accessible via `python` command
- **Windows**: Install Python from [python.org](https://python.org) and ensure it's added to PATH
- **macOS**: Use `python3` instead of `python` or install via Homebrew: `brew install python`
- **Linux**: Install via package manager: `sudo apt install python3 python3-venv`

**Problem**: Virtual environment activation fails
- **Windows PowerShell**: Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- **Windows CMD**: Use `activate.bat` instead of `Activate.ps1`
- **macOS/Linux**: Ensure the script is executable: `chmod +x setup.sh`

### Dependency Installation

**Problem**: `fake-bpy-module-latest` installation fails
- **Solution**: Update pip first: `python -m pip install --upgrade pip`
- **Alternative**: Try installing a specific version: `pip install fake-bpy-module-4.2`

**Problem**: Permission errors during installation
- **Solution**: Ensure virtual environment is activated before installing packages
- **Never use sudo**: Don't use `sudo pip install` as it installs globally

## VS Code Issues

### Python Interpreter

**Problem**: VS Code doesn't recognize the virtual environment
- **Solution**: 
  1. Open Command Palette (`Ctrl+Shift+P`)
  2. Type "Python: Select Interpreter"
  3. Choose the interpreter from `.venv/Scripts/python.exe` (Windows) or `.venv/bin/python` (macOS/Linux)

**Problem**: Autocomplete not working for Blender modules
- **Check**: Ensure `fake-bpy-module-latest` is installed in your venv: `pip list | grep fake-bpy`
- **Check**: Verify `python.analysis.extraPaths` in `.vscode/settings.json` points to your venv's site-packages
- **Reload**: Restart VS Code or reload the window (`Ctrl+Shift+P` → "Developer: Reload Window")

### Extensions

**Problem**: Blender Development extension not working
- **Check**: Ensure the extension is installed and enabled
- **Update**: Make sure you have the latest version
- **Settings**: Verify `blender.blenderExecutable.path` points to your Blender executable

## Blender Integration Issues

### Blender Path Configuration

**Problem**: "Blender executable not found"
- **Find Blender path**:
  - **Windows**: Usually `C:\Program Files\Blender Foundation\Blender [version]\blender.exe`
  - **macOS**: `/Applications/Blender.app/Contents/MacOS/Blender`
  - **Linux**: `/usr/bin/blender` or wherever you installed it
- **Update**: Edit `.vscode/settings.json` and set the correct path in `blender.blenderExecutable.path`

**Problem**: Blender starts but add-on is not loaded
- **Check**: Ensure the add-on is enabled in Blender's preferences
- **Path**: Verify the add-on directory path in the Blender Development extension settings
- **Reload**: Try manually reloading the add-on in Blender

### Debugging Issues

**Problem**: Debugger doesn't connect to Blender
- **Port**: Check if port 8080 is available (change in `.vscode/launch.json` if needed)
- **Python**: Ensure `blender.python.executable.path` points to your venv's Python
- **Firewall**: Check if your firewall is blocking the connection

**Problem**: Breakpoints not working
- **Source**: Ensure you're setting breakpoints in the correct source files
- **Mapping**: Check that the file paths match between VS Code and Blender
- **Mode**: Set `"justMyCode": false` in launch configuration to debug into Blender code

## Platform-Specific Issues

### Windows

**Problem**: PowerShell execution policy errors
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Problem**: Path separator issues in settings.json
- Use forward slashes `/` or escaped backslashes `\\` in JSON
- Example: `"C:/Program Files/Blender Foundation/Blender 4.2/blender.exe"`

### macOS

**Problem**: "Permission denied" when running setup.sh
```bash
chmod +x setup.sh
./setup.sh
```

**Problem**: Blender.app not recognized
- Use the full path to the Blender executable inside the .app bundle
- Example: `/Applications/Blender.app/Contents/MacOS/Blender`

### Linux

**Problem**: Blender not in PATH
- Install via package manager: `sudo apt install blender`
- Or download from blender.org and extract to `/opt/blender/`

## Development Issues

### Add-on Not Reloading

**Problem**: Changes not reflected in Blender
- **Check**: Ensure `blender.addon.reloadOnSave` is `true` in settings
- **Manual**: Use `F8` in Blender to manually reload scripts
- **Restart**: Sometimes requires restarting Blender

### Import Errors

**Problem**: `ModuleNotFoundError` for Blender modules
- **Environment**: Ensure you're running code within Blender's context
- **Fake Module**: For development/linting, ensure `fake-bpy-module` is installed
- **Real Module**: For actual execution, code must run within Blender

### Performance Issues

**Problem**: VS Code becomes slow with large projects
- **Exclude**: Add directories to `files.exclude` in settings.json
- **Index**: Disable unnecessary language servers
- **Extensions**: Disable unused extensions

## Getting Help

### Logs and Debug Information

1. **VS Code Developer Tools**: `Help > Toggle Developer Tools`
2. **Python Extension Logs**: Check the Output panel, select "Python" from dropdown
3. **Blender Console**: Check Blender's console for error messages
4. **Extension Logs**: Check the Blender Development extension output

### Community Resources

- **Blender Development Extension**: [GitHub Repository](https://github.com/JacquesLucke/blender_vscode)
- **Blender API Documentation**: [docs.blender.org/api](https://docs.blender.org/api/)
- **Blender Stack Exchange**: [blender.stackexchange.com](https://blender.stackexchange.com/)
- **VS Code Python Extension**: [GitHub Repository](https://github.com/microsoft/vscode-python)

### Reporting Issues

When reporting issues, please include:
1. Operating system and version
2. Python version (`python --version`)
3. VS Code version
4. Blender version
5. Extension versions
6. Complete error messages
7. Steps to reproduce the issue

## Clean Reset

If all else fails, try a clean reset:

1. **Delete virtual environment**: Remove `.venv` directory
2. **Reset VS Code settings**: Delete `.vscode` directory (will lose custom settings)
3. **Clear VS Code cache**: 
   - Close VS Code
   - Delete workspace cache (location varies by OS)
4. **Start fresh**: Run setup script again

### Cache Locations
- **Windows**: `%APPDATA%\Code\User\workspaceStorage`
- **macOS**: `~/Library/Application Support/Code/User/workspaceStorage`
- **Linux**: `~/.config/Code/User/workspaceStorage`