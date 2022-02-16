import tkinter as tk


class Main:
    def __init__(self):
        super(Main).__init__()
        self.root = tk.Tk()

    def update(self):
        self.root.mainloop()


if __name__ == "__main__":
    Main().update()
