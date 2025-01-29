import cv2
import mediapipe as mp
import random
import time

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Game choices
choices = ["Rock", "Paper", "Scissors"]

# Function to classify hand gesture
def classify_gesture(landmarks):
    thumb_tip = landmarks[4].y
    index_tip = landmarks[8].y
    middle_tip = landmarks[12].y
    ring_tip = landmarks[16].y
    pinky_tip = landmarks[20].y

    # Rock: All fingers closed
    if index_tip > landmarks[6].y and middle_tip > landmarks[10].y:
        return "Rock"
    # Scissors: Only index and middle fingers up
    elif index_tip < landmarks[6].y and middle_tip < landmarks[10].y and ring_tip > landmarks[14].y:
        return "Scissors"
    # Paper: All fingers open
    elif index_tip < landmarks[6].y and middle_tip < landmarks[10].y and ring_tip < landmarks[14].y:
        return "Paper"
    
    return None  # No valid gesture detected

# Function to determine the winner
def get_winner(player, computer):
    if player == computer:
        return "It's a Tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

# Start video capture
cap = cv2.VideoCapture(0)

last_capture_time = time.time()
gesture = None
computer_choice = None
round_start_time = time.time()
countdown_duration = 3  # Computer waits 3 seconds before choosing

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip for natural mirror effect
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Detect gesture every 3 seconds
            if time.time() - last_capture_time > 3:
                gesture = classify_gesture(hand_landmarks.landmark)
                last_capture_time = time.time()
                round_start_time = time.time()  # Restart countdown for computer's turn
                computer_choice = None  # Reset computer choice

    # Countdown before computer makes a move
    elapsed_time = time.time() - round_start_time
    if elapsed_time < countdown_duration:
        countdown_text = f"Computer choosing in {int(countdown_duration - elapsed_time)}..."
        cv2.putText(frame, countdown_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    else:
        if computer_choice is None:  # Only pick once after countdown
            computer_choice = random.choice(choices)

        # Display choices
        if gesture:
            cv2.putText(frame, f"You: {gesture}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f"Computer: {computer_choice}", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, get_winner(gesture, computer_choice), (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow("Rock Paper Scissors", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
