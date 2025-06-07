# Graphical Password Authentication Software

This project implements a graphical password authentication system using Python. Instead of traditional alphanumeric passwords, users authenticate by selecting a series of images or points on an image, enhancing security and usability.

## Project Summary

Graphical passwords offer an alternative authentication method that is often easier to remember and harder to guess. This system allows users to register and authenticate using image-based inputs, with a graphical interface built using Python's GUI libraries.

## Features

- Image-based user registration and login
- Graphical User Interface (GUI) for ease of use
- Local database (`SQLite`) to store user credentials
- Modular codebase for extensibility
- Asset management for custom images and buttons

## Technologies Used

- Python 3
- Tkinter (GUI)
- SQLite (Database)
- PIL (Python Imaging Library)
- Custom image assets

## File Structure

- `gui.py`, `gui2.py` – Graphical interfaces for login and registration
- `Insert.py` – Handles user insertion into the database
- `image_mod.py` – Image handling and processing
- `users.db` – SQLite database storing user credentials
- `assets/` – Contains GUI image assets (buttons, entries, etc.)

## How to Run

1. Ensure Python 3 is installed.
2. Install required libraries (if not already available):
   ```bash
   pip install pillow

