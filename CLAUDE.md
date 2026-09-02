# Project: Focus Tracker

## Goal
A Windows desktop app that asks what task I'm working on at boot, and shows a popup if I get sidetracked into an app not part of that task.

## Stack
- Python 3.11+
- PySide6 for UI — hand-drawn pixel art assets from LibreSprite, no default Qt widget styling
- pywin32 for Windows integration (startup registration, foreground window detection)
- psutil for resolving a foreground window's process to an app name

## Visual theme
Pixel art, purple/night palette, cats, moon, witch, nightcore aesthetic.

## Feature roadmap (build in this order, one step at a time — don't jump ahead)
1. Boot at startup
2. Main window: menu with "Choose a plan" / "Create a plan", plus a "Stats" tab
3. Choose a plan → pick from a dropdown of saved plans
4. Create a plan → name, description, icon, list of apps involved
5. After picking/creating a plan, window closes but stays running in the system tray
6. Opening a non-plan app shows a centered popup: not included, with options to add it or close the app
7. User marks the plan "Completed?"
8. Back to step 2's menu. Stats tab shows daily streak, time focused, tasks completed as a bar graph

## Known follow-ups (deferred on purpose, revisit later)
- Plan storage is still in-memory only (a list on MainWindow), even though step 5 (tray persistence) is now built. Switch to file-based (JSON) persistence — serializing Plan via dataclasses.asdict/json.dump, loading on boot, handling a missing/corrupt file — since plans currently don't survive an app restart despite the app now living in the tray across a session.
- Step 1 (boot at startup) was skipped — steps 2-5 got built first. Revisit via pywin32 registry registration (e.g. the Run key) once the step 6 popup feature is in a good place; it's self-contained and doesn't block anything else.

## How I want to work
I'm learning as I build this. Follow Mentor output style rules for feature code — hints and doc pointers only, no full implementations. Repo/environment scaffolding (git, venv, installs) can be done directly.