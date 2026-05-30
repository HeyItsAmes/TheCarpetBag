VS Code
🧰 VS Code Setup & Recommended Extensions
Let’s optimize your environment so coding feels smooth, fast, and reliable.

🚀 Core Extensions (Required)
These are the essentials for this course.
Python (Microsoft) – Official Python support, linting, debugging, venv detection.
Pylance – Type checker & intelligent autocomplete. Makes coding way smoother.
Excel Viewer – Lets you open .xlsx files directly inside VS Code. Note: new releases may also allow for CSV viewing!
CSV Viewer – Lets you open CSVs cleanly with filtering and sorting.
✨ Helpful Add-Ons (Optional, but recommended)
These improve quality of life and workflow.
Codachi – Nerdy fella; grows as you code.
Python Indent – Fixes weird Python indentation issues.
Black Formatter – Auto-formats code. Great for keeping your files clean.
Material Icon Theme – Helps visually organize your folders and files.
Peacock – Lets you color-code VS Code windows (great if you're running multiple projects).
Path Intellisense – Autocomplete for file paths.
🛠️ Nice-to-Have Tools (Bonus)
Not required, but fun or helpful.
GitLens – Makes Git WAY easier (if you ever want to learn version control).
.env Manager – Helps organize environment variables.
Bookmarks – Lets you mark lines of code to revisit later.
🎨 Themes & Customization
A few excellent theme options depending on your mood:

Dracula Official – The classic dark purple hacker vibe.
Night Owl – Great contrast and easy on the eyes.
Github Dark / Light Default – Clean, professional, balanced.
Tokyo Night – Beautiful pop of color without being distracting.
You can install any theme and quickly switch between dark/light using:

Command Palette → “Color Theme”
  
⚙️ Recommended Settings
Add these to your VS Code settings.json to optimize Python work:

{
  "python.defaultInterpreterPath": "./vit_py.venv/bin/python",
  "python.terminal.activateEnvInCurrentTerminal": true,
  "editor.formatOnSave": true,
  "editor.tabSize": 4,
  "files.autoSave": "afterDelay",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true
}
  
Note: VS Code automatically detects your environment, but making it explicit avoids future troubleshooting.

🖥️ Use the Integrated Terminal (Important!)
👍 Always use the VS Code integrated terminal.

Students get confused switching between Mac Terminal / Windows CMD / WSL / PowerShell.

Using the VS Code terminal ensures:
Your virtual environment activates correctly
Your interpreter matches your workspace
You avoid path issues
Your project stays isolated and clean
🧩 Have We Missed Anything?
Here are a few extra tips noobs often need:

Reload VS Code whenever an extension doesn't behave.
Use Command Palette (⌘ + Shift + P or Ctrl + Shift + P) for EVERYTHING.
Use the Explorer panel to keep track of files — avoid running code outside the project folder.
Check the status bar (bottom bar) — it always tells you which Python interpreter you're using.
Don’t install Python extensions globally in system folders — always inside your project venv.
With this setup, you’re running a professional-grade environment suitable for real Python engineering work.