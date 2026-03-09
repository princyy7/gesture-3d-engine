# Gesture 3D Engine - Hand Tracking

A real-time hand gesture recognition script built with **MediaPipe Tasks** and **OpenCV**.

## What It Does
- Captures webcam video
- Detects one hand in real time
- Identifies simple gestures based on finger states:
  - `ROCK ✊`
  - `PAPER ✋`
  - `SCISSORS ✌️`
  - `POINT ☝️`
  - `CALL ME 🤙`
- Draws hand landmarks on the frame
- Displays recognized gesture text on screen

## File
- `hand_tracking.py`

## Requirements
- Python 3.10+
- `mediapipe`
- `opencv-python`
- `hand_landmarker.task` (must be in the same folder)

## Install Dependencies
```bash
pip install mediapipe opencv-python
