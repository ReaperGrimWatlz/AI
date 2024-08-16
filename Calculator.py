import tkinter as mk
import cube
import time
start=time.time()
def opencalc(root):
    root.destroy()
    root=mk.Tk()
    root.title("Calculator")
    entry = mk.Entry(root, width=35, borderwidth=5)
    def click_button(button):
        if button == '=':
            try:
                result = eval(entry.get())
                entry.delete(0, mk.END)
                entry.insert(mk.END, str(result))
            except Exception as e:
                entry.delete(0, mk.END)
                entry.insert(mk.END, "Error")
        else:
            entry.insert(mk.END, button)
    def clear_entry():
        entry.delete(0, mk.END)
    def quit_calculator():
        root.destroy()
    entry.grid(row=0, column=0, columnspan=4)
    buttons = ['7', '8', '9', '/',
               '4','5', '6', '*',
               '1', '2', '3', '-',
               '0', '.', '=', '+',]
    row_val = 1
    col_val = 0
    for button in buttons:
        mk.Button(root, text=button, width=5, command=lambda button=button: click_button(button)).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1
    mk.Button(root, text="C", width=21, command=clear_entry).grid(row=row_val, column=0, columnspan=4)
    mk.Button(root, text="Quit", width=21, command=quit_calculator).grid(row=row_val+1, column=0, columnspan=4)
    root.mainloop()

def doingit(root):
    try:
        cube.cubemaker()
        cubem.destroy()
        newboy=mk.Button(root,text="Open Calculator",fg="gray",command=lambda: opencalc(root))
        newboy.pack(side="right")
    except:
        cubem.destroy()
        newboy=mk.Button(root,text="Open Calculator",fg="gray",command=lambda: opencalc(root))
        newboy.pack(side="right")

root=mk.Tk()
cubem=mk.Button(root,text="Draw Cube",fg="Blue",command=lambda: doingit(root))
cubem.pack(side="right")
quit=mk.Button(root,text="exit",fg="Red",command=root.destroy)
quit.pack(side="top")
root.mainloop()
end=time.time()
print("Time taken: ", end-start, " seconds")
