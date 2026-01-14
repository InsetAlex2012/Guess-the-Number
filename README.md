# 🎲 Guess The Number (Python)

A graphical **Guess the Number game** built with Python and Tkinter.  
Players select a difficulty level, try to guess the randomly generated number, and receive visual feedback to guide them.

---

## ✨ Features

### Game Mechanics
- Random number generated based on selected difficulty:
  - **Easy:** 0–50  
  - **Medium:** 0–100  
  - **Hard:** 0–200
- Input your guess using a **Spinbox**
- Tracks the number of tries
- Color-coded feedback based on tries:
  - Green: excellent
  - Gold: moderate
  - Red: high
  - Black: too many tries

### Visual Feedback
- Direction indicators for guesses:
  - **Up arrow:** guess is too low
  - **Down arrow:** guess is too high
  - **Correct:** guess is correct
- “You win!” message displayed upon guessing correctly
- Victory disables input and highlights success

### Graphical User Interface (GUI)
- Built with **Tkinter** and **ttkthemes** (theme: "breeze")
- Styled radio buttons for difficulty selection
- Buttons and labels use custom fonts
- Themed window icon (`dice.png`)
- Images used for game feedback (`up.png`, `down.png`, `correct.png`, `question.png`)

### Additional Features
- Dynamic Spinbox range based on difficulty
- Tracks and displays **tries in real-time**
- Clean layout and responsive UI

---

## 🛠 Technologies Used

- **Python 3** (required)
- **Tkinter** (built-in GUI)
- **ttkthemes** (UI theming)
- **random** (number generation)

---

## ▶️ How to Run

1. Make sure Python 3 is installed
2. Install the external dependency:
   ```bash
   pip install ttkthemes
   ```
3. Ensure the following image files are in the same directory as the script:
   - `up.png`
   - `down.png`
   - `correct.png`
   - `question.png`
   - `dice.png`
4. Run the program:
   ```bash
   python guess_the_number.py
   ```

---

## 📂 Required Files

- `guess_the_number.py`
- `up.png`
- `down.png`
- `correct.png`
- `question.png`
- `dice.png`

---

## ⚠️ Notes

- Designed for **educational purposes** and learning Tkinter GUI development
- Difficulty levels affect the number range and scoring feedback
- Number of tries affects color-coded visual feedback

---

## 👤 Author

**AlexIsNotInset**
