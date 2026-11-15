import customtkinter as ctk
from SudokuSolverBackend import SudokuSolverClass 

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = SudokuSolverClass()
    app.mainloop()
