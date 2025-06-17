import cv2
import time
import mediapipe as mp

def detect_hand_orientation(hand_landmarks):
    wrist_z = hand_landmarks.landmark[mp_holistic.HandLandmark.WRIST].z
    middle_mcp_z = hand_landmarks.landmark[mp_holistic.HandLandmark.MIDDLE_FINGER_MCP].z
    if middle_mcp_z < wrist_z:
        return "Palma"
    else:
        return "Dorso"

def classify_hand_gesture(hand_landmarks):
    finger_states = []

    thumb_tip = hand_landmarks.landmark[mp_holistic.HandLandmark.THUMB_TIP].x
    thumb_ip = hand_landmarks.landmark[mp_holistic.HandLandmark.THUMB_IP].x
    finger_states.append(thumb_tip < thumb_ip)

    finger_tips_ids = [
        mp_holistic.HandLandmark.INDEX_FINGER_TIP,
        mp_holistic.HandLandmark.MIDDLE_FINGER_TIP,
        mp_holistic.HandLandmark.RING_FINGER_TIP,
        mp_holistic.HandLandmark.PINKY_TIP
    ]

    finger_pip_ids = [
        mp_holistic.HandLandmark.INDEX_FINGER_PIP,
        mp_holistic.HandLandmark.MIDDLE_FINGER_PIP,
        mp_holistic.HandLandmark.RING_FINGER_PIP,
        mp_holistic.HandLandmark.PINKY_PIP
    ]

    for tip_id, pip_id in zip(finger_tips_ids, finger_pip_ids):
        tip = hand_landmarks.landmark[tip_id].y
        pip = hand_landmarks.landmark[pip_id].y
        finger_states.append(tip > pip)  

    if all(finger_states):
        return "Pedra"
    elif not any(finger_states): 
        return "Papel"
    elif finger_states[1] == False and finger_states[2] == False and finger_states[0] and finger_states[3]:  
        return "Tesoura"
    else:
        return "Indefinido"

mp_holistic = mp.solutions.holistic
holistic_model = mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mp_drawing = mp.solutions.drawing_utils

capture = cv2.VideoCapture(0)

previousTime = 0

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1000, 800))
    frame = cv2.flip(frame, 1) 

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = holistic_model.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    left_gesture = None
    right_gesture = None

    if results.right_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        right_gesture = classify_hand_gesture(results.right_hand_landmarks)
        right_orientation = detect_hand_orientation(results.right_hand_landmarks)
        cv2.putText(image, f'Direita: {right_gesture} ({right_orientation})', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    if results.left_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        left_gesture = classify_hand_gesture(results.left_hand_landmarks)
        left_orientation = detect_hand_orientation(results.left_hand_landmarks)
        cv2.putText(image, f'Esquerda: {left_gesture} ({left_orientation})', (10, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    if left_gesture and right_gesture:
        if left_gesture != "Indefinido" and right_gesture != "Indefinido":
            if left_gesture == right_gesture:
                result = "Empate!"
            elif (left_gesture == "Pedra" and right_gesture == "Tesoura") or \
                 (left_gesture == "Tesoura" and right_gesture == "Papel") or \
                 (left_gesture == "Papel" and right_gesture == "Pedra"):
                result = "Esquerda VENCE!"
            else:
                result = "Direita VENCE!"
            cv2.putText(image, result, (10, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)

    cv2.putText(image, "Mostre a PALMA da mao para melhor deteccao", (10, 580), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)

    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime
    cv2.putText(image, f"{int(fps)} FPS", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Pedra, Papel, Tesoura", image)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
