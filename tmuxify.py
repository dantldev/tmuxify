#!/usr/bin/env python3

import subprocess
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python tmuxify.py [file_path] [optional_session_name]")
        sys.exit(1)

    file_path = sys.argv[1]
    if not file_path.endswith('.tmuxify'):
        print("Error: File must have a '.tmuxify' extension")
        sys.exit(1)

    session_name = sys.argv[2] if len(sys.argv) > 2 else "mysession"

    try:
        # Start a new TMUX session
        subprocess.run(['tmux', 'new-session', '-d', '-s', session_name], check=True)

        # Open file and read paths
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue

                # Split the line into path and optional custom pane name
                parts = line.split(' --- ')
                path = parts[0]
                window_name = parts[1] if len(parts) > 1 else path.split('/')[-1]

                # Create a new window for each path with the specified or default name
                subprocess.run(['tmux', 'new-window', '-t', session_name, '-n', window_name], check=True)
                # Change directory in that window
                subprocess.run(['tmux', 'send-keys', '-t', session_name + ':' + window_name, f'cd {path}', 'C-m'], check=True)

        # Select the first window
        subprocess.run(['tmux', 'select-window', '-t', session_name + ':0'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run tmux command: {e}")

    # Attach to the session
    subprocess.run(['tmux', 'attach', '-t', session_name])

if __name__ == "__main__":
    main()
