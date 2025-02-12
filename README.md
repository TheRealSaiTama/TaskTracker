<div align="center">

# Task Tracker CLI

```
████████╗ █████╗ ███████╗██╗  ██╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║   ███████║███████╗█████╔╝        ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
   ██║   ██╔══██║╚════██║██╔═██╗        ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ██║  ██║███████║██║  ██╗       ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
```

![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)
![Version](https://img.shields.io/badge/version-1.0.0-green.svg?style=flat-square)
![Python Version](https://img.shields.io/badge/python-v3.6+-blue?style=flat-square)
![Status](https://img.shields.io/badge/status-active-success.svg?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)


A powerful command-line interface application for managing and tracking tasks efficiently. This Python-based task tracker helps you organize your work with features like task creation, status updates, and progress monitoring.

[📖 Documentation](#-documentation) • [🚀 Features](#-features) • [⚡️ Quick Start](#-installation) • [🤝 Contributing](#-contributing) • [📝 License](#-license)

</div>

## 📑 Table of Contents

- [✨ Features](#-features)
- [🏗️ Project Structure](#️-project-structure)
- [💻 Tech Stack](#-tech-stack)
- [🚀 Installation](#-installation)
- [📖 Usage](#-usage)
- [🎨 Status Display](#-status-display)
- [📋 Available Commands](#-available-commands)
- [📂 File Structure](#-file-structure)
- [🤝 Contributing](#-contributing)
- [📝 License](#-license)

## ✨ Features

- ✨ Create and manage tasks with titles and descriptions
- 🔄 Update task status (Not Started, In Progress, Completed)
- 📊 View tasks with colorized status display
- 🗑️ Delete tasks when no longer needed
- 📝 Edit existing task details
- 🔍 Search and filter tasks by status
- 💾 Persistent storage using JSON
- 📈 Progress tracking and statistics
- 🏷️ Task categorization and tagging
- ⏰ Due date management
- 🔔 Priority levels
- 📊 Export tasks to various formats

## 🏗️ Project Structure

The project follows a clean and modular architecture:

- Core application logic in `main.py`
- Task management functionality in `task_manager.py`
- Utility functions in `utils.py`
- Data persistence through JSON storage
- Comprehensive test coverage
- Clear separation of concerns

## 💻 Tech Stack

- **Python 3.6+** - Core programming language
- **JSON** - Data persistence
- **Click** - Command-line interface creation
- **Rich** - Terminal formatting and colors
- **PyTest** - Testing framework
- **Black** - Code formatting
- **Flake8** - Code linting
- **Poetry** - Dependency management
- **Pre-commit** - Git hooks for code quality

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager
- Git (for cloning the repository)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/TheRealSaitama/task-tracker-cli.git
cd task-tracker-cli
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Verify installation:
```bash
python main.py --version
```

## 📖 Usage

### Add a new task
```bash
python main.py add "Complete documentation" "Write comprehensive documentation for the project"
```

### Update task status
```bash
python main.py update 1 --status "in_progress"
```

### List all tasks
```bash
python main.py list
```

### Delete a task
```bash
python main.py delete 1
```

## 🎨 Status Display

Tasks are displayed with intuitive color-coded status indicators:

- 🔴 Not Started - Red
- 🟡 In Progress - Yellow
- 🟢 Completed - Green

Example output:
```
ID: 1 | Title: Complete documentation | Status: 🟡 In Progress
ID: 2 | Title: Write tests           | Status: 🔴 Not Started
ID: 3 | Title: Deploy application    | Status: 🟢 Completed
```

## 📋 Available Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `add` | Create a new task | `python main.py add <title> <description>` |
| `list` | Show all tasks | `python main.py list` |
| `update` | Update task status or details | `python main.py update <id> --status <status>` |
| `delete` | Remove a task | `python main.py delete <id>` |
| `search` | Search tasks by status | `python main.py search <status>` |
| `export` | Export tasks to file | `python main.py export <format>` |
| `stats` | View task statistics | `python main.py stats` |

## 📂 File Structure

```
task-tracker-cli/
├── main.py
├── requirements.txt
├── requirements-dev.txt
├── setup.py
├── README.md
├── LICENSE
├── .gitignore
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_task_manager.py
└── src/
    ├── __init__.py
    ├── task_manager.py
    ├── utils.py
    └── config.py
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Install development dependencies (`pip install -r requirements-dev.txt`)
4. Make your changes
5. Run tests (`pytest`)
6. Ensure code quality (`black . && flake8`)
7. Commit your changes (`git commit -m 'Add AmazingFeature'`)
8. Push to the branch (`git push origin feature/AmazingFeature`)
9. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details, inspiration by [Roadmap.sh](https://roadmap.sh/projects/task-tracker).

<div align="center">
<p>Made with ❤️ by TheRealSaitama</p>
<p>

[![GitHub](https://img.shields.io/badge/GitHub-TheRealSaitama-181717?style=for-the-badge&logo=github)](https://github.com/TheRealSaitama)

</p>
</div>
