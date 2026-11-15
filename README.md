# APPDAET Sudoku Solver
---
### Sudoku Solver Prototype #1
**Included Changes**
- UI works
- Backtracking works
- Generated Puzzles can be chosen and used 

**To Work On**
- CustomHandler (for error handling)
- add customhandler (ts too hard)
- create a new function to change the text of for example if theres a conflict or the backtrack algorithm didn't work
- I think set status is good
- include light and dark mode
- crash bug (if you click on a puzzle and then click on another puzzle, it will crash the program, this is because the currentIndex is not updated when a new puzzle is generated, so when the reset button is clicked, it will try to generate the old puzzle again, which will cause an error because the old puzzle is not in the PROBLEMS list anymore) 
- zip bomb (for legal reasons thats a joke)

### How to get it Running
1. Clone the Repository
```
git clone https://github.com/ojtBSWM2025/APPDAET_SudokuSolver
cd APPDAET_SudokuSolver
```

2. run main.py
*On Windows:*
```
python.13.exe main.py
```

*On Linux*
```
python3 main.py
```


##### Authors:
Backend - Valdepenas, Cortez | Frontend - Subardiaga, Castaneda | QA Tester - Raymundo
