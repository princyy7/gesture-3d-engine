import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Load model
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

def get_finger_states(hand_landmarks):
    fingers = []

    # Thumb (x comparison because thumb moves sideways)
    fingers.append(hand_landmarks[4].x < hand_landmarks[3].x)

    # Other fingers (y comparison)
    fingers.append(hand_landmarks[8].y < hand_landmarks[6].y)
    fingers.append(hand_landmarks[12].y < hand_landmarks[10].y)
    fingers.append(hand_landmarks[16].y < hand_landmarks[14].y)
    fingers.append(hand_landmarks[20].y < hand_landmarks[18].y)

    return fingers


def recognize_gesture(fingers):
    if fingers == [False, False, False, False, False]:
        return "ROCK ✊"

    if fingers == [True, True, True, True, True]:
        return "PAPER ✋"

    if fingers == [False, True, True, False, False]:
        return "SCISSORS ✌️"

    if fingers == [False, True, False, False, False]:
        return "POINT ☝️"

    if fingers == [True, False, False, False, True]:
        return "CALL ME 🤙"

    return "UNKNOWN"


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=frame_rgb
    )

    result = detector.detect(mp_image)

    gesture_text = ""

    if result.hand_landmarks:
        for hand in result.hand_landmarks:

            fingers = get_finger_states(hand)
            gesture_text = recognize_gesture(fingers)

            # Draw landmarks
            for lm in hand:
                x = int(lm.x * frame.shape[1])
                y = int(lm.y * frame.shape[0])
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    cv2.putText(frame, gesture_text, (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    cv2.imshow("Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()