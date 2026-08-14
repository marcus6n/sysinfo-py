# Learnings

## What I did

I built a Python CLI tool that collects and displays real system information using psutil. I organized the code into separate collection, report-building, display, and JSON export functions, created a virtual environment, installed dependencies from requirements.txt, and validated execution using both default and custom output files.

## What I learned

- A small CLI project becomes easier to maintain when data collection and presentation are separated.
- JSON export is more useful when values stay numeric instead of being formatted strings.
- Argument parsing with argparse makes the tool feel like a real command-line utility.
- Using a virtual environment avoids dependency issues and keeps the project reproducible.
- It is important to activate the virtual environment before running tests and commands.
- On Linux environments, python3 may exist while python may not be available globally.
- A clear repository structure and concise documentation make the project easier to explain and share.

## Problems I faced

### Running commands without the virtual environment

I initially ran commands without activating the virtual environment first.

**Solution:** I standardized execution by activating venv before every run.

### Command mismatch between python and python3

In some runs, python was not available while python3 worked.

**Solution:** I confirmed the environment setup and used the interpreter available inside the activated virtual environment.

### Inconsistent naming and language in output

Parts of the project used Portuguese text and mixed field naming styles.

**Solution:** I translated user-facing output to English and normalized report keys for consistency.

## What I would improve next

- Add unit tests for each data collection function.
- Add optional CSV export in addition to JSON.
- Improve uptime formatting to include days for long-running systems.
- Add error handling for permission-restricted environments.
- Extend the report with network interface and process summary data.
