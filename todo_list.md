<!--
Markdown Interactive Checkbox Preview
https://github.com/GSejas/markdown-checkbox-preview/blob/master/README.md
--GSejas

Transform your Markdown task lists into an interactive, synchronized workspace. Click to toggle checkboxes, navigate with tree views, and track progress—all while your changes sync instantly to your source files.

✨ Key Features
🎯 Interactive Checkbox Preview
One-click toggling - Click any checkbox in the preview to change its state
Real-time sync - Changes instantly update your Markdown source files
Smart navigation - Click headers to jump directly to source locations
Auto-preview mode - Optional automatic preview opening for markdown files
📊 Progress Tracking
Visual progress bars showing completion percentages
Hover information with status, content, and quick actions
Status bar integration displaying completion statistics at a glance
🌲 Tree View Navigation
Hierarchical organization - Tasks grouped by headers and structure
Sidebar integration - Browse all checkboxes from the Explorer panel
Toggle visibility - Show/hide headers for focused task management
One-click updates - Click any tree item to toggle its state
💻 Editor Integration
CodeLens actions - Toggle buttons appear directly above checkbox lines
Inline hover cards - See status and actions without leaving your cursor
Seamless workflow - All features integrate naturally with VS Code
🚀 Quick Start
Open Interactive Preview
Open any Markdown file with checkboxes

Press Ctrl+Shift+P (or Cmd+Shift+P on Mac)

Search for "Open Interactive Checkbox Preview"
Click checkboxes to toggle them—changes save automatically!
Navigate with Tree View
Open a Markdown file with checkboxes

Find "Markdown Checkboxes" in the Explorer sidebar

Browse your tasks organized by headers

Click any checkbox to toggle its state instantly
Use the refresh button (↻) to update the view

Toggle header visibility (👁) to focus on tasks only

Enable Auto-Preview
Click the eye icon in the status bar (bottom-right) to enable auto-preview mode:

👁 ✓ = Auto-preview enabled
👁 ✗ = Auto-preview disabled
When enabled, previews open automatically for all markdown files.



📝 Supported Syntax
The extension recognizes standard Markdown checkbox syntax:

# Project Tasks

## Development
- [ ] Set up project structure
- [x] Configure build tools
  - [x] Install dependencies
  - [ ] Set up linting
    - [x] ESLint configuration
    - [ ] Prettier setup

## Documentation
- [ ] Write README
- [ ] Add API docs
-- >

## Development
- [ ] Set up project structure
- [x] Configure build tools
  - [x] Install dependencies
  - [ ] Set up linting
    - [x] ESLint configuration
    - [ ] Prettier setup

## Documentation
- [ ] Write README
- [ ] Add API docs