# Graphical-Password-Software-Information-Security-

This project implements a graphical password authentication system where users select image segments in sequence. Built with Python's Tkinter for GUI and SQLite for database storage, it offers secure, visual-based authentication.

---

## Key Features

- **Image Segmentation**: Divides uploaded images into 3x3 grid segments
- **Sequence Authentication**: Users authenticate by selecting segments in predefined order
- **Multi-User Support**: Stores multiple users with individual image sets
- **Encrypted Storage**: Passwords stored as SHA-256 hashed sequences
- **Database Management**: SQLite backend for user credentials and image metadata

---

## System Workflow

### Registration Phase
1. User uploads image (JPG/PNG)
2. System segments image into 9 parts
3. User selects 4-6 segments in sequence
4. System stores:
   - Original image path
   - Segment sequence pattern
   - SHA-256 hash of sequence

### Authentication Phase
1. System displays jumbled segments
2. User recreates original sequence
3. System verifies against stored hash

---

## Database Schema (SQLite)
