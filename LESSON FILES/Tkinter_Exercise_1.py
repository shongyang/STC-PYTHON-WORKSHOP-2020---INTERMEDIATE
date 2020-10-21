import tkinter

try:
    root = tkinter.Tk()
    root.geometry("500x500")
    Label1 = tkinter.Label(root, text="I am Root!")
    Label1.pack()
    root.mainloop()
except:
    print("Alamak")
else:
    print("WooHooHoo!")