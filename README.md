# Hand Gesture Recognition

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Tasks-0097A7)
![OpenCV](https://img.shields.io/badge/OpenCV-computer%20vision-5C3EE8?logo=opencv&logoColor=white)

**Rock, paper, scissors and more, recognized live from your webcam.**

A small real-time script built with MediaPipe Tasks and OpenCV. It tracks one hand, works out which fingers are up, and names the gesture on screen.

---

## Features

- **Live hand tracking:** detects 21 landmarks on one hand with the MediaPipe HandLandmarker.
- **Five gestures:** rock, paper, scissors, point and call me.
- **Landmark overlay:** draws every detected landmark on the video frame.
- **On-screen label:** shows the recognized gesture, or `UNKNOWN` when nothing matches.
- **Simple and readable:** one short script with no extra files besides the model.

---

## Supported Gestures

Each gesture is a pattern of fingers that are up or down.

| Gesture | Thumb | Index | Middle | Ring | Pinky |
|:--------|:-----:|:-----:|:------:|:----:|:-----:|
| ✊ Rock | down | down | down | down | down |
| ✋ Paper | up | up | up | up | up |
| ✌️ Scissors | down | up | up | down | down |
| ☝️ Point | down | up | down | down | down |
| 🤙 Call me | up | down | down | down | up |

Any other combination shows `UNKNOWN`.

---

## How It Works

1. **Capture** a frame from the webcam with OpenCV.
2. **Convert** it from BGR to RGB and pass it to the MediaPipe HandLandmarker.
3. **Read** the 21 landmarks and compare points to decide which fingers are up:
   - **Thumb:** the tip is compared with the joint below it along the **x-axis**, because the thumb moves sideways.
   - **Other fingers:** the tip is compared with its middle joint along the **y-axis**. If the tip is higher on screen, the finger is up.
4. **Match** the five up/down values to a known gesture.
5. **Draw** the landmarks and the gesture name on the frame.

---

## Getting Started

### Requirements

- Python 3.10+
- A webcam
- `mediapipe` and `opencv-python`
- The `hand_landmarker.task` model file

### Installation

```bash
git clone https://github.com/princyy7/gesture-3d-engine.git
cd gesture-3d-engine
pip install mediapipe opencv-python
```

### Get the model

Download `hand_landmarker.task` from the [MediaPipe Hand Landmarker page](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker) and place it in the same folder as the script.

```text
gesture-3d-engine/
├── hand_tracking.py
├── hand_landmarker.task
└── README.md
```

### Run

```bash
python3 hand_tracking.py
```

Hold one hand up to the camera and make a gesture. Press **`q`** to quit.
