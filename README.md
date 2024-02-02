# Shuf: Python Implementation of GNU shuf command

## Overview

This repository contains a Python implementation of the GNU `shuf` command, named `shuf.py`. The implementation prioritizes user-friendliness, compatibility, and efficient error handling.

## Key Features

- Implemented essential `shuf` options: `--echo`, `--input-range`, `--head-count`, and `--repeat`.
- Utilized argparse for modern command-line parsing, enhancing extensibility.

## How to Reproduce and Run `shuf.py`

To reproduce and run the `shuf.py` script in your terminal, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Shuf.git
   ```

2. **Navigate to the Repository:**
   ```bash
   cd Shuf
   ```

3. **Run the Script:**
   - Ensure you have Python 3 installed on your system.
   - Execute the script with the desired options. For example:
     ```bash
     python3 shuf.py --echo Hello World
     ```
     This command will shuffle and echo the input "Hello World."

4. **Explore `shuf.py` Options:**
   - Experiment with different options, such as `--input-range` or `--head-count`, to observe varied outputs.
   - Refer to the help message for guidance:
     ```bash
     python3 shuf.py --help
     ```

## Efficient Error Handling

- Implemented robust error handling for invalid arguments and file-related issues.
- Ensured error reporting consistency with GNU `shuf`.

## Development Environment

- Used Emacs for efficient code development.
- Restricted imports to essential modules, aligning with project specifications.
