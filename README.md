# Rock Paper Scissors - Computer Vision Game

A simple **Rock, Paper, Scissors** game using **OpenCV and MediaPipe** to recognize hand gestures and play against the computer. The game introduces a **slow-paced experience**, where the computer waits **3 seconds** before making a move, adding suspense and fairness.

## Features
- 🎥 **Hand Gesture Recognition** using MediaPipe Hands
- ⏳ **Slower Gameplay** (3-second delay for computer moves)
- 🤖 **Computer Opponent** that chooses randomly
- 🏆 **Winner Announcement** after each round
- 🛑 **Exit Anytime** by pressing 'Q'

---

## Installation
Ensure you have **Python 3.x** installed, then install the required libraries:

```bash
pip install opencv-python mediapipe numpy
```

---

## How to Play
1. **Run the script**:
   ```bash
   python rock_paper_scissors.py
   ```
2. Show one of the following **hand gestures** in front of the camera:
   - ✊ **Rock**: All fingers closed
   - ✋ **Paper**: All fingers open
   - ✌️ **Scissors**: Only index and middle fingers extended
3. Wait **3 seconds** for the computer to choose.
4. The **winner is displayed** on the screen.
5. Press **'Q' to exit** anytime.

---

## How It Works
- The camera captures **hand movements** and detects key points using **MediaPipe Hands**.
- The program **identifies** Rock, Paper, or Scissors based on **finger positions**.
- After detecting a move, a **3-second countdown** starts before the computer makes its move.
- The result is displayed on the screen.

---

## Possible Enhancements
✅ Improve gesture detection using **Machine Learning**
✅ Add **Score Tracking** for multiple rounds
✅ Include **Voice Announcements** for results
✅ Implement **Multiplayer Mode** over a network

---

## License
This project is **open-source** and free to use under the **MIT License**.

---

Happy Gaming! 🎮✊✋✌️

