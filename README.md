# Tmuxify

Welcome to **Tmuxify** — my own set of cool scripts to work with tmux, enhancing productivity and streamlining your development environment. These scripts are designed to automate the management of tmux sessions, windows, and panes, making it easier and quicker to jump right into your projects.

## Features

- **Dynamic Session Management**: Start tmux sessions with customizable names.
- **Automated Window Creation**: Automatically create tmux windows for each project directory listed in your `.tmuxify` files, with optional custom names for each pane.
- **Flexible**: Supports custom `.tmuxify` file formats for specifying project paths and pane names.
- **Easy to Use**: Simple command-line interface to manage complex tmux setups.

## Installation

To install Tmuxify, run the following command in your terminal:

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/dantldev/tmuxify/main/install.sh)"
```

This command will download and run the installation script from the Tmuxify repository. The script will:

- Download the latest version of the Tmuxify script.
- Place it in `/usr/local/bin`, making it executable and accessible from anywhere in your terminal.

**Note**: Depending on your system setup, you may need to run the installation with `sudo` to ensure proper permissions.

## Usage

To use Tmuxify, you need a `.tmuxify` file that specifies the paths and optional custom pane names. Here’s how to run the main script:

```bash
tmuxify /path/to/your_file.tmuxify [optional_session_name]
```

### File Format

Your `.tmuxify` file should contain lines in the following format:

```
/path/to/project/directory --- OptionalCustomPaneName
```

If no custom pane name is provided, the script will use the last directory name in the path as the pane name.

### Example

```txt
/home/user/project1 --- Project1
/home/user/code/project2
```

In this example, `tmuxify` will open two tmux windows. The first window will be named "Project1" and will open the directory `/home/user/project1`. The second will use "project2" as its name and will open `/home/user/code/project2`.

## Contributing

Contributions are welcome! If you have a bug report, feature request, or patch, please feel free to submit a pull request or open an issue.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- This project was inspired by daily routines and the need for more efficient project management within tmux.
