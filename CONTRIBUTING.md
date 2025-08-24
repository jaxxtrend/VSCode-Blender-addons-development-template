# Contributing to Blender Add-on Development Template

Thank you for your interest in contributing to this template! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Issues

If you encounter problems or have suggestions for improvements:

1. **Check existing issues** first to avoid duplicates
2. **Use the issue templates** when available
3. **Provide detailed information**:
   - Operating system and version
   - Python version
   - VS Code version
   - Blender version
   - Steps to reproduce the issue
   - Expected vs actual behavior
   - Any error messages or logs

### Suggesting Enhancements

When suggesting new features or improvements:

1. **Explain the use case** - why would this be helpful?
2. **Describe the solution** - what should happen?
3. **Consider alternatives** - are there other ways to achieve this?
4. **Keep it focused** - this is a template, not a full development framework

### Pull Requests

We welcome pull requests! Please follow these guidelines:

1. **Fork the repository** and create a feature branch
2. **Keep changes focused** - one feature/fix per PR
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Follow the code style** established in the project

## Development Setup

To work on this template:

1. **Fork and clone** the repository
2. **Test the template** by following the setup instructions
3. **Make your changes** in a feature branch
4. **Test again** to ensure everything still works
5. **Update relevant documentation**

## Code Style Guidelines

### Python Code

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use meaningful variable and function names
- Add docstrings for classes and functions
- Keep functions small and focused
- Use type hints where helpful

### JSON Configuration

- Use consistent indentation (4 spaces)
- Include comments explaining non-obvious settings
- Group related settings together
- Use workspace variables (`${workspaceFolder}`) for portability

### Documentation

- Use clear, concise language
- Include code examples where helpful
- Update all relevant documentation files
- Test instructions on different platforms when possible

## What We're Looking For

### High Priority

- **Cross-platform compatibility** improvements
- **Documentation** enhancements and clarifications
- **Setup script** improvements for better error handling
- **VS Code configuration** optimizations
- **Troubleshooting** additions for common issues

### Medium Priority

- **Example add-on** enhancements (more operators, better structure)
- **Additional utility scripts** for common development tasks
- **CI/CD** setup for automated testing
- **Template variants** for different use cases

### Low Priority

- **Advanced features** that might complicate the template
- **External dependencies** beyond what's absolutely necessary
- **IDE-specific** features for editors other than VS Code

## Testing Guidelines

When contributing changes, please test:

1. **Fresh setup** - test the complete setup process from scratch
2. **Different platforms** - Windows, macOS, Linux if possible
3. **Different Python versions** - 3.10, 3.11, 3.12
4. **Different Blender versions** - 3.x and 4.x series
5. **Both manual and automated setup** methods

### Testing Checklist

- [ ] Template can be cloned/downloaded
- [ ] Setup script runs without errors
- [ ] Virtual environment is created successfully
- [ ] Dependencies install correctly
- [ ] VS Code recognizes the Python interpreter
- [ ] Autocomplete works for Blender modules
- [ ] Blender can be launched from VS Code
- [ ] Add-on loads and runs in Blender
- [ ] Debugging works (breakpoints, variable inspection)
- [ ] Hot reload works (save file → addon reloads)

## Documentation Standards

### README Updates

- Keep the main README focused on getting started quickly
- Move detailed information to separate files
- Use clear section headers and consistent formatting
- Include both manual and automated setup instructions

### Code Comments

- Explain **why**, not just **what**
- Use inline comments sparingly
- Prefer self-documenting code with good naming
- Add docstrings for public functions and classes

### Configuration Comments

- Explain the purpose of each major setting
- Include platform-specific notes where relevant
- Provide examples of alternative values
- Link to official documentation when helpful

## Release Process

For maintainers releasing new versions:

1. **Update version numbers** in relevant files
2. **Update CHANGELOG** with new features and fixes
3. **Test thoroughly** on all supported platforms
4. **Create release notes** with migration instructions if needed
5. **Tag the release** with semantic versioning

## Code of Conduct

This project follows a simple code of conduct:

- **Be respectful** to all contributors
- **Be constructive** in feedback and criticism
- **Be patient** with newcomers and questions
- **Be collaborative** and help others succeed

## Getting Help

If you need help contributing:

- **Open an issue** with your question
- **Check existing documentation** first
- **Look at recent pull requests** for examples
- **Ask in the discussion section** for general questions

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for helping make this template better for the Blender development community!