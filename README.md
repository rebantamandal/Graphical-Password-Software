# Graphical-Password-Software-Information-Security-

A Python application for secure graphical password authentication using image segments. Users select a sequence of image parts as their password. Multiple images and user credentials are managed with SQLite. The GUI is built with Tkinter.

## Features

- Users upload images and select a sequence of segments as their password
- Authentication by clicking the correct sequence of image parts
- Supports multiple users and multiple images per user
- Credentials and image info stored securely in SQLite database

## How It Works

1. **Registration:**  
   - Upload an image  
   - Image is split into a 3x3 grid  
   - User selects a sequence of segments as their password  
   - Sequence is hashed and stored in SQLite

2. **Login:**  
   - User selects an image  
   - Clicks segments in the correct order  
   - Sequence is verified against stored hash

## Requirements

- Python 3.x
- Tkinter
- Pillow
- sqlite3 (standard with Python)

## Running the App

1. Install dependencies:  
   `pip install Pillow`
2. Run the script:  
   `python graphical_password.py`

## Applications

- Secure login systems
- Visual authentication for kiosks or shared devices

