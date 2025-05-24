# Treasure Hunt Game (COM4103 Python Artefact)

**Author:** Mohammad Samee  
**Module:** COM4103 Computing Skills Portfolio  

---

## 📌 Project Overview

The Treasure Hunt Game (for the COM4103 Computing Skills Portfolio module) is a grid-based treasure hunt game designed in Python. The game includes a 5x5 grid, with obstacles, traps, power-ups, and a treasure that can be found.

The game is played by two players iteratively taking turns searching the grid for the treasure with the added caveat of a health system, traps that can take away health, and power-ups that can add health or give hints to the treasure. The game is won by the first player to find the treasure on the grid.

---

## 🧠 Key Features

• 2 player turn-based game  
• The following will be randomly placed in the game:  
 • Treasure (T)  
 • Traps (X)  
 • Obstacles (O)  
 • Powerups (P)  
• Health system, where players are eliminated if their health is less than 1  
• The following power-up effects:  
 • health increase  
 • treasure hints  
• The following different search algorithms:  
 • Binary Search (BS) on row/column  
 • Breadth First Search (BFS) for the shortest path  
 • Depth First Search (DFS) for an alternative path  
• Command line interface (CLI)

---

## ▶️ How to Run the Game

**Requirements:**  
• Python 3.12 or higher  
• VS Code or any other code editor, as long as there is terminal

**To run:**  
1. Store the file as `treasure_hunt.py`  
2. Open your terminal in the project folder  
3. Run the game script:  
```bash
python3 treasure_hunt.py
```

---

## 🎮 Commands

Players will have the following commands available:  
• `move up` / `move down` / `move left` / `move right`  
• `bs row` — Binary search a row (i.e. `bs row 3`)  
• `bs col` — Binary search a column (i.e. `bs col 2`)  
• `bfs` — Finds the shortest path to the treasure  
• `dfs` — Finds an alternative path to the treasure

---

## 🛠️ Technologies Used

• Python 3.12  
• VS Code

---

## 🧪 Testing

The game was manually tested by:  
• On traps and power-ups obtained  
• Result of search algorithms  
• Edge and collision tests  
• Multiple loop of full game with 2 players

---

## ⚖️ Ethical Issues

• No user data is collected  
• Game is fully offline  
• No external packages were used

---

## 🔗 GitHub Repository

[https://github.com/samee123x/treasure-hunt.git](https://github.com/samee123x/treasure-hunt.git)

---

## 📁 Submission Information

The project was submitted in:  
• A ZIP file containing the `treasure_hunt.py` file and this `README`  
• A GitHub repository (as linked above)  
• A technical report in PDF format
