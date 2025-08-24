# VS Code Blender Add-on Development Template

This is a development template for creating Blender 3D add-ons with VS Code integration, featuring Python virtual environments, autocomplete support, and debugging capabilities.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

- **Bootstrap and setup the repository**:
  - `python3 setup.py` -- takes ~20 seconds to complete. NEVER CANCEL. Set timeout to 60+ seconds.
  - Alternative: `./setup.sh` (Linux/macOS) or `setup.bat` (Windows)
  - This creates `.venv/` virtual environment and installs dependencies

- **Install dependencies manually** (if automated setup fails):
  - `python3 -m venv .venv`
  - **Linux/macOS**: `source .venv/bin/activate`
  - **Windows**: `.venv\Scripts\Activate.ps1` (PowerShell) or `.venv\Scripts\activate.bat` (CMD)
  - `pip install --upgrade pip --timeout 300` (with extended timeout for slow networks)
  - `pip install -r requirements.txt --timeout 300` -- takes ~15 seconds. NEVER CANCEL. Set timeout to 300+ seconds for slow networks.

- **Format and lint code**:
  - `source .venv/bin/activate` (activate venv first)
  - `black addon/` -- formats code, takes ~0.3 seconds
  - `black --check addon/` -- check formatting without changes
  - `pylint addon/ --disable=import-error` -- lint code, takes ~4 seconds. NEVER CANCEL.

- **Required external tools**:
  - **Python 3.10+**: Must be installed on system (not Blender's Python)
  - **Blender 3.x or 4.x**: Install via package manager or download from blender.org
  - **VS Code Extensions**: Python (Microsoft), Blender Development (Jacques Lucke)

## Validation

- **ALWAYS validate setup by running**:
  - `python3 setup.py` (should complete in ~20 seconds)
  - `source .venv/bin/activate && pip list` (should show fake-bpy-module-latest, black, pylint, mypy)
  - `source .venv/bin/activate && black --check addon/`
  - `source .venv/bin/activate && pylint addon/ --disable=import-error`

- **Test Blender integration**:
  - Install Blender: `sudo apt install blender` (Linux) or download from blender.org
  - Update `.vscode/settings.json` with correct Blender path
  - **Linux example**: `"path": "/usr/bin/blender"`
  - **Windows example**: `"path": "C:/Program Files/Blender Foundation/Blender 4.2/blender.exe"`
  - **macOS example**: `"path": "/Applications/Blender.app/Contents/MacOS/Blender"`

- **ALWAYS test complete user scenario after changes**:
  1. Run setup process: `python3 setup.py` (should complete in ~20 seconds)
  2. Activate virtual environment: `source .venv/bin/activate`
  3. Test code formatting: `black --check addon/` (should show no changes needed)
  4. Test code linting: `pylint addon/ --disable=import-error` (should rate ~9/10)
  5. Verify VS Code settings are updated correctly for current platform
  6. Check that addon files can be imported: `python3 -c "import bpy; print('bpy available for autocomplete')"`
  7. Verify Blender integration: `blender --version` (should show 4.x)

## Build and Development Process

- **No build step required** - this is a Python development template
- **Development workflow**:
  1. Edit files in `addon/` directory
  2. Save files to trigger hot reload in Blender (if VS Code extension is configured)
  3. Test add-on functionality in Blender

- **Configuration files automatically updated by setup**:
  - `.vscode/settings.json` - Python paths updated for current platform
  - `.vscode/launch.json` - Debug configurations for Blender integration

- **VS Code integration**:
  - Command Palette: "Blender: Start" launches Blender with add-on linked
  - Debugging: Set breakpoints, use "Blender: Launch & Debug" configuration
  - Hot reload: Files automatically reload in Blender when saved

## Platform-Specific Requirements

### Linux (Tested on Ubuntu 24.04)
- Install Blender: `sudo apt install blender` (installs Blender 4.0.2)
- Python path: `.venv/bin/python`
- Blender path: `/usr/bin/blender`

### Windows
- Python path: `.venv\Scripts\python.exe`
- Blender path example: `C:/Program Files/Blender Foundation/Blender 4.2/blender.exe`
- PowerShell execution policy: May need `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### macOS
- Python path: `.venv/bin/python`
- Blender path example: `/Applications/Blender.app/Contents/MacOS/Blender`
- Setup script: May need `chmod +x setup.sh` first

## Common Tasks and Timing

### Setup Process
- **Complete setup**: ~20 seconds via `python3 setup.py`
- **Virtual environment creation**: ~2 seconds
- **Dependency installation**: ~15 seconds
- **Settings update**: ~1 second

### Development Tasks
- **Code formatting**: ~0.3 seconds via `black addon/`
- **Code linting**: ~4 seconds via `pylint addon/ --disable=import-error`
- **Blender startup**: Variable depending on system

### Common File Operations
```bash
# Repository root contents
ls -a
.git .gitignore .vscode CONTRIBUTING.md README.md TROUBLESHOOTING.md
addon requirements.txt setup.bat setup.py setup.sh

# Virtual environment after setup
ls .venv/
bin include lib lib64 pyvenv.cfg

# Addon directory structure
ls addon/
__init__.py operators.py
```

## Dependencies and Packages

### Python Dependencies (from requirements.txt)
- **fake-bpy-module-latest**: Provides Blender API autocomplete/type hints
- **black**: Code formatter
- **pylint**: Code linter
- **mypy**: Type checker

### Expected Package Versions
```
fake-bpy-module-latest  20250630
black                   25.1.0
pylint                  3.3.8
mypy                    1.17.1
```

## Key Configuration Files

### .vscode/settings.json
- **Purpose**: Python interpreter paths, Blender executable path, extension settings
- **Platform handling**: Setup scripts automatically comment/uncomment platform-specific paths
- **Critical settings**: 
  - `python.defaultInterpreterPath`
  - `blender.blenderExecutable.path`
  - `python.analysis.extraPaths`

### .vscode/launch.json
- **Purpose**: Debug configurations for Blender integration
- **Key configuration**: "Blender: Launch & Debug"

### addon/__init__.py
- **Purpose**: Main add-on file with bl_info metadata
- **Contains**: Operator classes, Panel classes, registration functions

## Troubleshooting

### Setup Issues
- **Virtual environment fails**: Ensure Python 3.10+ is installed and accessible
- **Dependency installation fails**: 
  - Check internet connection, network timeouts are common in restricted environments
  - Try manual setup: `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
  - Use longer pip timeout: `pip install --timeout 300 -r requirements.txt`
  - Alternative: Copy packages from working environment or use offline installation
- **Permission errors**: Ensure not using sudo with pip when venv is activated
- **Network timeouts**: Common in CI/containerized environments - document as known limitation

### Development Issues
- **Autocomplete not working**: Verify fake-bpy-module-latest is installed and Python paths are correct
- **Blender not starting**: Check blender.blenderExecutable.path in settings.json
- **Hot reload not working**: Ensure blender.addon.reloadOnSave is true

### Code Quality Issues
- **Linting errors**: Run `pylint addon/ --disable=import-error` to see issues
- **Formatting issues**: Run `black addon/` to auto-format code
- **Import errors**: Remember that bpy modules only work within Blender context

## Important Notes

- **NEVER use sudo with pip** when virtual environment is activated
- **ALWAYS activate virtual environment** before installing packages or running tools
- **File formatting**: The setup process reformats Python files with black
- **Platform paths**: Setup automatically configures paths for current platform
- **Extensions required**: Must install Python and Blender Development extensions in VS Code
- **Blender versions**: Template works with Blender 3.x and 4.x series
- **Network limitations**: In restricted environments (CI, containers), pip installations may timeout
  - Document as "pip install fails due to network limitations" when encountered
  - Use manual setup with extended timeouts: `pip install --timeout 300`
- **Firewall restrictions**: Some corporate/institutional networks block PyPI access

## Expected Validation Results

### Successful Setup Output
```
Blender Add-on Development Template Setup
========================================
✓ Python 3.12.3 found
Creating Python virtual environment...
✓ Virtual environment created successfully
Installing dependencies...
✓ pip upgraded successfully
✓ Dependencies installed successfully
Updating VS Code settings for current platform...
✓ VS Code settings updated for current platform
```

### Successful Formatting
```
$ black addon/
reformatted addon/__init__.py
reformatted addon/operators.py
All done! ✨ 🍰 ✨
2 files reformatted.
```

### Linting Results
```
$ pylint addon/ --disable=import-error
Your code has been rated at 9.10/10
```

Remember: This is a development template, not a build system. The primary workflow is editing Python files and testing them in Blender via the VS Code extension integration.

## Comprehensive Validation Checklist

Use this checklist to validate that the template is working correctly:

```bash
# 1. Setup validation
python3 setup.py  # Should complete in ~20 seconds

# 2. Environment validation
source .venv/bin/activate
pip list | grep -E "(fake-bpy|black|pylint|mypy)"  # Should show all 4 packages

# 3. Code quality validation
black --check addon/  # Should show "files would be left unchanged"
pylint addon/ --disable=import-error  # Should rate ~9/10

# 4. Dependencies validation
python3 -c "import bpy; print('SUCCESS: bpy available for autocomplete')"

# 5. External tools validation
blender --version  # Should show Blender 4.x

# 6. Configuration validation
grep -q "python.defaultInterpreterPath.*bin/python" .vscode/settings.json  # Linux/macOS
# OR grep -q "python.defaultInterpreterPath.*Scripts/python.exe" .vscode/settings.json  # Windows
```

**Expected results**: All commands should succeed without errors. If any fail, document the specific failure and provide workarounds in instructions.