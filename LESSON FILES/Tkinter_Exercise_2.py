from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFont, ImageDraw

root = Tk()

root.title("The Highly Advanced Imaging Software of the Future")
# root.iconbitmap(r"bico.ico")
root.geometry("700x400")
root.resizable(True, True)
root.labelFrame1 = LabelFrame(root, text="Choose File to Insert Watermark")
root.labelFrame1.grid(column=0, row=1, padx=20, pady=20)


def openFile():
    file1 = filedialog.askopenfilename(
        initialdir="/",
        # title="Select A File",
        defaultextension=".jpeg",
        filetypes=[
            ("Image file", ".jpg"),
            ("Image file", ".png"),
            ("All files", ".*"),
        ],
    )
    if not file1:
        return

    global img
    img = Image.open(file1)
    # img = Image.new("RGBA", (900,900), "white")
    str1 = "Heyyyy"

    fontsize = 1
    img_fraction = 0.50
    font = ImageFont.truetype("comicbd.ttf", fontsize)
    while font.getsize(str1)[0] < img_fraction * img.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype("comicbd.ttf", fontsize)

    # optionally de-increment to be sure it is less than criteria
    fontsize -= 1
    font = ImageFont.truetype("comicbd.ttf", fontsize)

    font = font
    # font.getsize(str1)
    draw = ImageDraw.Draw(img)
    # draw.text(900, 400, str1, font=font, fill=(0, 0, 0))
    draw.text((5, 5), str1, fill="red", font=font, align="right")

    # resize the image and apply a high-quality down sampling filter
    displayimg1 = img
    displayimg1 = displayimg1.resize((250, 250), Image.ANTIALIAS)

    # PhotoImage class is used to add image to widgets, icons etc
    displayimg1 = ImageTk.PhotoImage(displayimg1)

    # create a label
    panel = Label(root, image=displayimg1)

    # set the image as img

    panel.image = displayimg1
    panel.grid(row=1, column=2)


def saveFile():
    savedfilename1 = filedialog.asksaveasfile(
        mode="w",
        initialdir="/",
        defaultextension=".jpg",
        filetypes=[
            ("Image file", ".jpeg"),
            ("Image file", ".png"),
            ("All files", ".*"),
        ],
    )
    if not savedfilename1:
        return
    img.save(savedfilename1)


root.button1 = Button(
    root.labelFrame1, text="Browse A File", command=openFile, anchor="center"
)
root.button1.grid(column=1, row=1, sticky="NSEW")


root.label = ttk.Label(root.labelFrame1, text="")
root.label.grid(column=1, row=4)


button2 = Button(text="Save File", command=saveFile)
button2.grid()
root.mainloop()