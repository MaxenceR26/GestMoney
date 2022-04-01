import tkinter as tk
import tkinter.ttk as ttk
import time

tree = ttk.Treeview()
for i in range(100):
    iid = tree.insert('', 'end', text=i)
tree.pack()

def event_test(iid):
    t['text'] = iid
    print("iid", iid)

def move_bottom():
    iid = tree.get_children('')[-1]
    time.sleep(1)
    if iid != tree.focus():
        iid = tree.get_children('')[50]
        tree.focus(iid)
        tree.selection_set(iid)
        print("iid", iid)

        tree.event_add('<<Declenche>>', '<ButtonRelease-1>')
        tree.after(1000, lambda: tree.event_generate('<<Declenche>>'))
        tree.bind('<<Declenche>>', event_test(iid))

t = tk.Label()
t.pack()
tk.Button(text='move', command=move_bottom).pack()

tree.mainloop()