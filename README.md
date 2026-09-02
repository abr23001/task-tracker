# Focus Tracker

A Windows desktop app that asks what task you're working on at boot, and shows a popup if you get sidetracked into an app not part of that task.

See [CLAUDE.md](CLAUDE.md) for the full feature roadmap and project notes.

## Stack

- Python 3.11+
- [PySide6](https://doc.qt.io/qtforpython-6/) for the UI (hand-drawn pixel-art assets, no default Qt widget styling)
- [pywin32](https://github.com/mhammond/pywin32) for Windows integration (startup registration, foreground window detection)
- [psutil](https://psutil.readthedocs.io/) for resolving a foreground window to its app name

## Setup

```
git clone https://github.com/abr23001/task-tracker.git
cd task-tracker
python -m venv .venv
```

Activate the environment:

```
.venv\Scripts\activate.bat   # Windows (cmd)
.venv\Scripts\Activate.ps1   # Windows (PowerShell)
```

Install dependencies:

```
pip install -r requirements.txt
```

## Running

```
python -m scripts.main
```

(Run from the repo root — the app is structured as a package, `task_tracker/`, with `scripts/main.py` as the entry point, so it needs to be launched as a module rather than as a standalone script.)

## Status

Under active development. Currently working: main window navigation, creating and choosing plans, and closing to the system tray. See CLAUDE.md's roadmap for what's built versus still pending.
