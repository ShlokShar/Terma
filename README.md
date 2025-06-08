# Terma

Terma is a natural language command-line assistant that helps you run terminal commands without needing to memorize syntax. Whether you're installing software, updating packages, or configuring your environment, Terma translates plain English instructions into accurate shell commands for your terminal. 

## Description

Terma (short for Terminal Assistant) is designed to make the terminal more human-friendly. It removes the need to remember complex package manager commands, instead letting you type instructions like `terma install Node.js`. It intelligently detects your OS (Linux, macOS, or Windows) and uses the correct command — whether that’s `apt`, `brew`, or `choco`. Powered by an AI model and built with a modular architecture, Terma helps beginners learn, and helps experts go faster.

## Getting Started

### Dependencies

* Python 3.7+
* macOS, Linux, or Windows 10+
* Internet connection (for API-based LLM usage)
* `pip` for installation

### Installing

* You can download Terma from PyPI:
  * ```pip install terma```

### Executing program

1. Open a terminal.
2. Make sure `terma` is in your PATH.
3. Run any natural-language command:
   - ```terma exec "install nodejs"```
   - ```terma exec "uninstall flask"```
   - ```terma exec "update all packages"```

## Help

If you run into issues, try the built-in help command:
```
terma --help
```

## Authors

Shlok Sharma <br>
shlokrma@gmail.com

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details