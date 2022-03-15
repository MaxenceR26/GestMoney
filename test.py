import tkinter as tk
from tkinter import ttk
import pandas as pd
root = tk.Tk()
style1 = ttk.Style()
style1.configure("mystyle1.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11, 'bold')) # Modify the font of the body
style1.configure("mystyle1.Treeview.Heading", font=('Calibri', 10,'bold'), background="blue") # Modify the font of the headings
style1.layout("mystyle1.Treeview", [('mystyle1.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
def displaytree():
    app = tk.Toplevel()
    sample = {"File Name":[f"file_{i}" for i in range(5)],
              'Sheet Name': [f"sheet_{i}" for i in range(5)],
              'Number Of Rows': [f"row_{i}" for i in range(5)],
              'Number Of Columns': [f"col_{i}" for i in range(5)]
              }
    df = pd.DataFrame(sample)
    cols = list(df.columns)
    treeV = ttk.Treeview(app, style="mystyle1.Treeview")
    treeV.pack()
    treeV["columns"] = cols
    for i in cols:
        treeV.column(i, anchor="w")
        treeV.heading(i, text=i, anchor='w')
    for index, row in df.iterrows():
        treeV.insert("","end",text=index,values=list(row))
    app.mainloop()
bt1 = tk.Button(root, text="DISPLAY TREE VIEW", font="Times 12 bold", activebackground="white",
                activeforeground="green",width=16,height=1,bg="green",fg="white", command=displaytree)
bt1.pack()
root.mainloop()