import tkinter

flag = tkinter.Tk()

flag.grid()

label1 = tkinter.Label(flag, anchor="center", bg="red")
label1.grid(column=0, row=0, sticky="NSEW")

label2 = tkinter.Label(flag, anchor="center", bg="red")
label2.grid(column=1, row=0, sticky="NSEW")

label3 = tkinter.Label(flag, anchor="center", bg="red")
label3.grid(column=2, row=0, sticky="NSEW")

label4 = tkinter.Label(flag, anchor="center", bg="red")
label4.grid(column=3, row=0, sticky="NSEW")

label5 = tkinter.Label(flag, anchor="center", bg="red")
label5.grid(column=4, row=0, sticky="NSEW")

label6 = tkinter.Label(flag, anchor="center", bg="red")
label6.grid(column=5, row=0, sticky="NSEW")

label7 = tkinter.Label(flag, anchor="center", bg="red")
label7.grid(column=6, row=0, sticky="NSEW")

label8 = tkinter.Label(flag, anchor="center", bg="red")
label8.grid(column=0, row=1, sticky="NSEW")

label9 = tkinter.Label(flag, anchor="center", bg="red")
label9.grid(column=1, row=1, sticky="NSEW")

label10 = tkinter.Label(flag, anchor="center", bg="red")
label10.grid(column=2, row=1, sticky="NSEW")

label11 = tkinter.Button(flag, anchor="center", bg="white")
label11.grid(column=3, row=1, sticky="NSEW")

label12 = tkinter.Label(flag, anchor="center", bg="red")
label12.grid(column=4, row=1, sticky="NSEW")

label13 = tkinter.Label(flag, anchor="center", bg="red")
label13.grid(column=5, row=1, sticky="NSEW")

label14 = tkinter.Label(flag, anchor="center", bg="red")
label14.grid(column=6, row=1, sticky="NSEW")

label15 = tkinter.Label(flag, anchor="center", bg="red")
label15.grid(column=0, row=2, sticky="NSEW")

label16 = tkinter.Label(flag, anchor="center", bg="red")
label16.grid(column=1, row=2, sticky="NSEW")

label17 = tkinter.Button(flag, anchor="center", bg="white")
label17.grid(column=2, row=2, sticky="NSEW")

label18 = tkinter.Button(flag, anchor="center", bg="white")
label18.grid(column=3, row=2, sticky="NSEW")

label19 = tkinter.Button(flag, anchor="center", bg="white")
label19.grid(column=4, row=2, sticky="NSEW")

label20 = tkinter.Label(flag, anchor="center", bg="red")
label20.grid(column=5, row=2, sticky="NSEW")

label21 = tkinter.Label(flag, anchor="center", bg="red")
label21.grid(column=6, row=2, sticky="NSEW")

label22 = tkinter.Label(flag, anchor="center", bg="red")
label22.grid(column=0, row=3, sticky="NSEW")

label23 = tkinter.Label(flag, anchor="center", bg="red")
label23.grid(column=1, row=3, sticky="NSEW")

label24 = tkinter.Label(flag, anchor="center", bg="red")
label24.grid(column=2, row=3, sticky="NSEW")

label25 = tkinter.Button(flag, anchor="center", bg="white")
label25.grid(column=3, row=3, sticky="NSEW")

label26 = tkinter.Label(flag, anchor="center", bg="red")
label26.grid(column=4, row=3, sticky="NSEW")

label27 = tkinter.Label(flag, anchor="center", bg="red")
label27.grid(column=5, row=3, sticky="NSEW")

label28 = tkinter.Label(flag, anchor="center", bg="red")
label28.grid(column=6, row=3, sticky="NSEW")

label29 = tkinter.Label(flag, anchor="center", bg="red")
label29.grid(column=0, row=4, sticky="NSEW")

label30 = tkinter.Label(flag, anchor="center", bg="red")
label30.grid(column=1, row=4, sticky="NSEW")

label31 = tkinter.Label(flag, anchor="center", bg="red")
label31.grid(column=2, row=4, sticky="NSEW")

label32 = tkinter.Label(flag, anchor="center", bg="red")
label32.grid(column=3, row=4, sticky="NSEW")

label33 = tkinter.Label(flag, anchor="center", bg="red")
label33.grid(column=4, row=4, sticky="NSEW")

label34 = tkinter.Label(flag, anchor="center", bg="red")
label34.grid(column=5, row=4, sticky="NSEW")

label35 = tkinter.Label(flag, anchor="center", bg="red")
label35.grid(column=6, row=4, sticky="NSEW")

flag.grid_columnconfigure(0, weight=1)
flag.grid_columnconfigure(1, weight=1)
flag.grid_columnconfigure(2, weight=1)
flag.grid_columnconfigure(3, weight=1)
flag.grid_columnconfigure(4, weight=1)
flag.grid_columnconfigure(5, weight=1)
flag.grid_columnconfigure(6, weight=1)
flag.grid_rowconfigure(0, weight=1)
flag.grid_rowconfigure(1, weight=1)
flag.grid_rowconfigure(2, weight=1)
flag.grid_rowconfigure(3, weight=1)
flag.grid_rowconfigure(4, weight=1)


flag.title("The Swiss Will Be Proud")
flag.geometry("700x500")
flag.resizable(width=True, height=True)
# flag.iconbitmap(r"swissf1.ico")
flag.mainloop()