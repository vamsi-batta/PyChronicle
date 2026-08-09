# PyChronicle

## Project Overview
PyChronicle is a Python project that uses the Abstract Syntax Tree (AST) module to analyze Python source code and detect variable assignments.

## Features
- Reads a Python source file
- Parses code using the AST module
- Detects variable assignments
- Displays variable names and line numbers

## Technologies Used
- Python 3
- AST Module

## Project Structure

PyChronicle/
├── main.py
├── sample.py
└── README.md

## How to Run

```bash
python main.py
```

## Sample Output

Variable: x
Line: 1
----------------

## Week 2 Progress

### Features Implemented

- Execution tracing using `sys.settrace()`
- Variable state tracking
- SQLite database integration
- Database record viewer
- Basic Textual UI
## Week 3 Progress

### Delta Compression

- Detects variable value changes
- Stores only changed variables
- Tracks old and new values
- Avoids storing unchanged values

### SQLite Delta Storage

- Stores variable changes in `pychronicle.db`
- Saves timestamp for each change
- Saves variable name and value
- Saves line number

### Time-Scrubbing

- Reads variable history from SQLite
- Reconstructs variable state at a specific line
- Supports interactive line selection
- Displays the state of variables at the selected line

### Week 3 Files

- `delta_tracer.py` - Delta compression and SQLite storage
- `history_reader.py` - History reading and state reconstruction
- `pychronicle.db` - SQLite database containing variable history

### Week 3 Status

- Delta Compression ✅
- SQLite Storage ✅
- Timestamp Tracking ✅
- Line Number Tracking ✅
- History Reader ✅
- State Reconstruction ✅
- Interactive Time-Scrubbing ✅
## Week 4 Progress

### Features Implemented

- Variable history search
- Line history search
- Variable and line combination search
- Old → New value tracking
- History timeline
- Invalid history handling