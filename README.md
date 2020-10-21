# 🐍 STC-PYTHON-WORKSHOP-2020 - INTERMEDIATE
Resource, materials, lesson files, and other stuff for [Sunway Tech Club](https://facebook.com/sunwaytechclub)'s Python Workshop 2020 !

##To know a little about the workshop, click [here](bit.ly/stcpyw20)


🔖  **Topics Covered**

Slides viewable here:  [Click Me!](bit.ly/stcpyw20ifs)

- CSV: [Exercise #1](https://bit.ly/3js5WPf), [Exercise #2](https://bit.ly/3kjcnFv)
- Pandas: [Exercise #1](https://bit.ly/37uLCdm), [Exercise #2](https://bit.ly/3md05ia)
- Tkinter: [Exercise #1](https://bit.ly/3ogdRm4), [Exercise #2](https://bit.ly/35gZYvk), [Exercise #3](https://bit.ly/3dJrKEE)
<br/>

💡  **Intermediate Project**

<img src="https://github.com/shongyang/STC-PYTHON-WORKSHOP-2020---INTERMEDIATE/blob/main/OTHER%20MATERIALS/demo1.png" width="100" height="100">.
<img src="https://github.com/shongyang/STC-PYTHON-WORKSHOP-2020---INTERMEDIATE/blob/main/OTHER%20MATERIALS/demo2.png" width="100" height="100">


An annoying, CSV/Pandas-based desktop alarm (wrapped in a Tkinter GUI) that plays audio when triggered by an event you&#39;ve &quot;committed&quot; to, e.g. meeting, online lesson. Just so you know… could be paired with a scraper script that gets activated when the hour has come (or just about anything)!

Download buggy, heavy .exe version [here](bit.ly/35mvvff).

If the .exe in the `dist` folder doesn&#39;t work, I think you&#39;ll need to go to `ALARM.PY EXE\__pycache__\ alarm.cpython-37.pyc`
and run it from there. Brownie points awarded to anyone who can fix this problem.

<br/>

🗺️  **Getting Started**

**## Libraries required:**

```
from tkcalendar import DateEntry
from playsound import playsound
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
from datetime import date
from tkinter import ttk
from tkinter import *
import pandas as pd
import tkinter.ttk
import time

```

**## Ready-made functions for you:**

```
def set_upcoming_text(df):
    date_list = df["date"].tolist()
    hour_list = df["hour"].tolist()
    minute_list = df["minute"].tolist()
    description_list = df["description"].tolist()
    text = ""
    for i in range(len(df)):
        text = (
            text
            + "\n"
            + str(date_list[i])
            + "   |   "
            + str(hour_list[i])
            + ":"
            + str(minute_list[i])
            + "   |   "
            + str(description_list[i])
            + "\n"
            + "---------------------------------------------------------------------------------------------------------------------------------------------------------------"
            + "\n"
        )
    upcoming_text.delete(1.0, END)
    upcoming_text.insert("end-1c", text)


def set_past_text(df):
    date_list = df["date"].tolist()
    hour_list = df["hour"].tolist()
    minute_list = df["minute"].tolist()
    description_list = df["description"].tolist()
    text = ""
    for i in range(len(df)):
        text = (
            text
            + "\n"
            + str(date_list[i])
            + "   |   "
            + str(hour_list[i])
            + ":"
            + str(minute_list[i])
            + "   |   "
            + str(description_list[i])
            + "\n"
            + "---------------------------------------------------------------------------------------------------------------------------------------------------------------"
            + "\n"
        )
    past_text.delete(1.0, END)
    past_text.insert("end-1c", text)


def check_alarm():
    # reading excel file
    df = pd.read_excel(excel_file_path)
    desc = ""
    # matching time and date
    today_date = date.today()
    today_date = str(today_date.strftime("%d/%m/%y"))

    now_time = datetime.now()
    current_time = now_time.strftime("%H:%M")

    for index, row in df.iterrows():
        # checking only those alarm which are still pending and ignore else
        if df["status"][index] != "finish":
            alarm_date = row["date"]
            hour = row["hour"]
            minute = row["minute"]
            hour_str = minute_str = hour_minute_str = ""

            # converting hours from 1 to 01, 9 ot 09 etc
            if hour >= 0 and hour <= 9:
                hour_str = "0" + str(hour)
            else:
                hour_str = str(hour)
            # converting minutes from 1 to 01, 9 ot 09 etc
            if minute >= 0 and minute <= 9:
                minute_str = "0" + str(minute)
            else:
                minute_str = str(minute)

            # matching current time with all alarms time
            hour_minute_str = hour_str + ":" + minute_str
            if today_date == alarm_date and current_time == hour_minute_str:
                df["status"][index] = "finish"
                desc = df["description"][index]
                df.to_excel(excel_file_path, index=False)
                return (True, desc)

    return (False, "")


def user_input_values_to_excel(df1, date, hours, minutes, description, mp3_filepath):
    df2 = pd.DataFrame(
        {
            "date": [date],
            "hour": [hours],
            "minute": [minutes],
            "description": [description],
            "mp3 file path": [mp3_filepath],
        }
    )

    df1 = df1.append(df2)
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(excel_file_path, engine="xlsxwriter")
    # Convert the dataframe to an XlsxWriter Excel object.
    df1.to_excel(writer, sheet_name="Sheet1", index=False)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()


def sorting_table_on_hour(df1):
    # sorting on base of hours
    df = pd.read_excel(excel_file_path)
    result = df.sort_values("hour")
    result.to_excel(excel_file_path, index=False)
    return result


def stop_loop():
    global flag
    flag = False


def upload_mp3_file():
    global mp3_filepath
    mp3_filepath = filedialog.askopenfilename(
        initialdir="/",
        title="Select A MP3 File",
        filetype=(("mp3", "*.mp3"), ("Äll Files", "*.*")),
    )


def set_alarm(btn_obj):
    global flag
    flag = True
    date = calendar.get()
    hours = hour_input.get()
    minutes = minute_input.get()
    description = description_input.get()
    hour_input.delete(0, "end")
    minute_input.delete(0, "end")
    description_input.delete(0, "end")
    try:
        if int(hours) > 24 or int(minutes) > 60 or description == "":
            messagebox.showinfo("Alert", "invalid field!")
        else:
            df = pd.read_excel(excel_file_path, parse_dates=False)

            # writing user input values to excel file
            df = user_input_values_to_excel(
                df, date, hours, minutes, description, mp3_filepath
            )
            df = sorting_table_on_hour(df)
            # reading data frames from excel file
            df = pd.read_excel(excel_file_path, parse_dates=False)
            upcoming_df = df.loc[df["status"] != "finish"]

            past_df = df.loc[df["status"] == "finish"]

            # fill UPCOMING alarm field
            set_upcoming_text(upcoming_df)

            # fill PAST alarm field
            set_past_text(past_df)

            # ringing alarm if time matches
            while True:
                # funtion for checking current time matches any alarm or not
                alarm_match_flag, desc = check_alarm()
                if alarm_match_flag:
                    # ring alarm tone
                    playsound(mp3_filepath)
                    messagebox.showinfo("Alarm", desc)
                    # reading data frames from excel file
                    df = pd.read_excel(excel_file_path, parse_dates=False)
                    upcoming_df = df.loc[df["status"] != "finish"]
                    past_df = df.loc[df["status"] == "finish"]
                    # fill UPCOMING alarm field
                    set_upcoming_text(upcoming_df)
                    # fill PAST alarm field
                    set_past_text(past_df)

                if flag:
                    alarm_window.update()
                    time.sleep(1.0)
                else:
                    break
    except:
        messagebox.showinfo("Alert", "Please fill fields!")
    hour_input.delete(0, END)
    minute_input.delete(0, END)
    description_input.delete(0, END)

```

**## Unique GUI elements for reference**

```
alarm_window = Tk()  # creating tkinger window
alarm_window.title("STC Python Workshop 2020 - Intermediate Project")  # set title of window
alarm_window.iconbitmap = "python-logo-2b.ico" #icon
w = alarm_window.winfo_screenwidth()  # getting current window width
h = alarm_window.winfo_screenheight()  # getting current window height
alarm_window.geometry("%dx%d+0+0" % (w, h))  # setting size of window to full
alarm_window.resizable(width=True, height=True)  # fixing size of window

# for date and time label
date_calendar = Label(alarm_window, text="Select Date/Time")
date_calendar.config(font=("Helvetica", 15))
date_calendar.grid(row=0, column=0, columnspan=5)

# for description label
description_label = Label(alarm_window, text="Description")
description_label.config(font=("Helvetica", 15))
description_label.grid(row=0, column=6, padx=250)

# for mp3 label
mp3_label = Label(alarm_window, text="mp3 upload")
mp3_label.config(font=("Helvetica", 15))
mp3_label.grid(row=0, column=7, padx=100)

########## row = 1  #########
# for calendar pop-up
calendar = DateEntry(
    alarm_window,
    width=12,
    background="darkblue",
    foreground="white",
    borderwidth=2,
    date_pattern="dd/mm/yy",
)

calendar.config(font=("Helvetica", 15))
calendar.grid(row=1, column=0)

# for hour label
hour_label = Label(alarm_window, text="Hour:")
hour_label.config(font=("Helvetica", 15))
hour_label.grid(row=1, column=1)

# for hour input
hour_input = Entry(alarm_window, borderwidth=3, width=3)
hour_input.config(font=("Helvetica", 15))
hour_input.grid(row=1, column=2)

# for minute label
minute_label = Label(alarm_window, text="Minute:")
minute_label.config(font=("Helvetica", 15))
minute_label.grid(row=1, column=3)

# for minute input
minute_input = Entry(alarm_window, borderwidth=3, width=3)
minute_input.config(font=("Helvetica", 15))
minute_input.grid(row=1, column=4)

# for description input
description_input = Entry(alarm_window, borderwidth=3, width=40)
description_input.config(font=("Helvetica", 15))
description_input.grid(row=1, column=6)

# for upload mp3 file
upload_btn = Button(alarm_window, text="upload audio", bd=3, command=upload_mp3_file)
upload_btn.config(font=("Helvetica"))
upload_btn.grid(row=1, column=7)

########## row = 2   ##########
commit_btn = Button(
    alarm_window, text="commit", bd=3, command=lambda: set_alarm(commit_btn)
)
commit_btn.config(font=("Helvetica"))
commit_btn.grid(row=2, column=7, pady=20)

########## row = 3   ##########
line_canvas = Canvas(alarm_window, width=1350, height=2, background="black")
line_canvas.grid(row=3, column=0, columnspan=9)
line_canvas.create_line(0, 0, 400, 400, fill="black")

########## row = 4   ##########
# for minute label
upcoming_label = Label(alarm_window, text="Upcoming Alarms")
upcoming_label.config(font=("Helvetica", 15))
upcoming_label.grid(row=4, column=0, columnspan=2)

new_alarm_btn = Button(alarm_window, text="stop", bd=3, command=stop_loop)
new_alarm_btn.config(font=("Helvetica"))
new_alarm_btn.grid(row=4, column=7, columnspan=7)

########## row = 5   ##########
# for upcoming text field
upcoming_text = Text(alarm_window, borderwidth=2, width=90, height=10)
upcoming_text.config(font=("Helvetica", 12))
upcoming_text.grid(row=5, column=2, columnspan=5)
scrollbar = Scrollbar(alarm_window, command=upcoming_text.yview)
scrollbar.grid(row=5, column=7, sticky=W, ipady=70)
upcoming_text.config(yscrollcommand=scrollbar.set)

########## row = 6   ##########
line_canvas = Canvas(alarm_window, width=1350, height=2, background="black")
line_canvas.grid(row=6, column=0, columnspan=9, pady=20)
line_canvas.create_line(0, 0, 400, 400, fill="black")

########## row = 7   ##########
# for minute label
past_label = Label(alarm_window, text="Past Alarms")
past_label.config(font=("Helvetica", 15))
past_label.grid(row=7, column=0, columnspan=2)

########## row = 8   ##########
# for upcoming text field
past_text = Text(alarm_window, borderwidth=2, width=90, height=10)
past_text.config(font=("Helvetica", 12))
past_text.grid(row=8, column=2, columnspan=5)
scrollbar = Scrollbar(alarm_window, command=past_text.yview)
scrollbar.grid(row=8, column=7, sticky=W, ipady=70)
past_text.config(yscrollcommand=scrollbar.set)
alarm_window.mainloop()  # compiling all objects in window

```

💌  **Last but not least**

**This repository is part of Sunway Tech Club&#39;s** _ **Python Workshop 2020** _

- Session 1 (Beginner): https://github.com/JustNunuz/STC-PYTHON-WORKSHOP-2020
- Session 2 (Intermediate): https://github.com/shongyang/STC-PYTHON-WORKSHOP-2020---INTERMEDIATE
- Session 3 (Project / Advanced): https://github.com/easonchai/python2020-workshop

**The Long List of Sources:**

- http://www.py2exe.org/index.cgi/Tutorial
- https://adibro.github.io/Data-Science-Resources/Cheat-Sheets/Data-Analysis/Pandas-Cheat-Sheet-3.pdf
- https://automatetheboringstuff.com/chapter14/
- https://code.visualstudio.com/docs/getstarted/tips-and-tricks
- https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf
- https://dataconomy.com/2015/03/14-best-python-pandas-features/
- https://data-flair.training/blogs/advantages-and-disadvantages-of-python/
- https://datatofish.com/executable-pyinstaller/
- https://docs.python.org/3/library/csv.html
- https://docs.python.org/3/library/modulefinder.html
- https://docs.python.org/3/library/tk.html
- https://docs.python.org/3/library/tkinter.ttk.html
- https://en.wikipedia.org/wiki/Comma-separated\_values
- https://en.wikipedia.org/wiki/Pandas\_(software)
- https://en.wikipedia.org/wiki/Tkinter
- https://github.com/chriskiehl/Gooey
- https://intellipaat.com/blog/advantages-and-disadvantages-of-python/
- https://learnpython.com/blog/python-programming-advantages-disadvantages/
- https://medium.com/@ahmed.nafies/my-top-10-visual-studio-code-extensions-for-python-in-2020-9896beb04e89
- https://medium.com/@mindfiresolutions.usa/advantages-and-disadvantages-of-python-programming-language-fd0b394f2121
- https://medium.com/@mukerong/data-wrangling-csv-module-466cd0d453e
- https://medium.com/swlh/why-you-should-use-python-to-script-8f1d591cf2c1
- https://pandas.pydata.org/docs/user\_guide/index.html#user-guide
- https://pip.pypa.io/en/stable/reference/pip\_freeze/
- https://pypi.org/project/pipreqs/
- https://pypi.org/project/pyttsx3/
- https://pyttsx3.readthedocs.io/en/latest/engine.html
- https://realpython.com/python-lambda/#anonymous-functions
- https://riptutorial.com/Download/pandas.pdf
- https://scrapy.org/
- https://squareboat.com/blog/advantages-and-disadvantages-of-python
- https://stackoverflow.com/questions/10937798/when-i-run-a-very-simple-py2exe-test-it-gives-me-errors
- https://stackoverflow.com/questions/15974787/difference-between-import-tkinter-as-tk-and-from-tkinter-import
- https://stackoverflow.com/questions/23584325/cannot-use-geometry-manager-pack-inside
- https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given
- https://stackoverflow.com/questions/24644339/python-tkinter-resize-widgets-evenly-in-a-window
- https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend#:~:text=What%20is%20the%20difference%20between%20the%20list%20methods%20append%20and,the%20list%2C%20extending%20the%20list.
- https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend#:~:text=What%20is%20the%20difference%20between%20the%20list%20methods%20append%20and,the%20list%2C%20extending%20the%20list.
- https://stackoverflow.com/questions/26147180/convert-row-to-column-header-for-pandas-dataframe
- https://stackoverflow.com/questions/27060098/replacing-few-values-in-a-pandas-dataframe-column-with-another-value
- https://stackoverflow.com/questions/31569384/set-value-for-particular-cell-in-pandas-dataframe-with-iloc
- https://stackoverflow.com/questions/31630792/py2exe-error-no-commands-supplied
- https://stackoverflow.com/questions/35628521/how-to-sort-a-csv-file-alphabetically
- https://stackoverflow.com/questions/36157553/how-to-replace-a-word-in-a-csv-file-in-specific-column-with-python
- https://stackoverflow.com/questions/47156055/tkinters-button-cant-change-border-color
- https://stackoverflow.com/questions/4902198/pil-how-to-scale-text-size-in-relation-to-the-size-of-the-image
- https://stackoverflow.com/questions/51473273/replace-partial-string-char-in-columdata-of-panda-dataframe
- https://stackoverflow.com/questions/54546368/python-split-a-string-in-a-csv-file-by-delimiter
- https://stackoverflow.com/questions/54670995/retrieving-the-requirements-of-a-python-single-script
- https://stackoverflow.com/questions/57033158/how-to-save-images-with-the-save-button-on-the-tkinter-in-python
- https://stackoverflow.com/questions/61291932/changing-one-whole-column-in-csv-file-into-sequential-numbers-in-python
- https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take
- https://stackoverflow.com/questions/725782/in-python-what-is-the-difference-between-append-and
- https://starwarsintrocreator.kassellabs.io/
- https://techvidvan.com/tutorials/python-advantages-and-disadvantages/
- https://thepythonguru.com/pros-cons-of-using-python-for-web-development/
- https://vilmate.com/blog/python-vs-other-programming-languages/
- https://waverleysoftware.com/blog/the-benefits-of-python/
- https://wiki.python.org/moin/GuiProgramming
- https://www.a2hosting.com/blog/python-advantages/
- https://www.altcademy.com/explain/foo-bar-baz
- https://www.codecademy.com/forum\_questions/52d4702552f863b90f000289
- https://www.codeproject.com/Questions/1111687/Write-row-numbers-in-csv-file
- https://www.c-sharpcorner.com/blogs/create-application-title-and-icon-in-python-gui
- https://www.daniweb.com/programming/software-development/threads/155928/removing-commas-from-list
- https://www.datacamp.com/community/tutorials/pandas-read-csv
- https://www.edureka.co/blog/python-applications/
- https://www.geeksforgeeks.org/loading-images-in-tkinter-using-pil/
- https://www.geeksforgeeks.org/python-language-advantages-applications/
- https://www.geeksforgeeks.org/python-pil-imagedraw-draw-text/
- https://www.invensis.net/blog/benefits-of-python-over-other-programming-languages/
- https://www.kite.com/python/answers/how-to-remove-a-comma-from-a-string-in-python
- https://www.kite.com/python/answers/how-to-replace-column-values-in-a-pandas-dataframe-in-python#:~:text=Access%20a%20specific%20pandas.,old%20values%20to%20new%20values.
- https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
- https://www.netguru.com/blog/python-in-finance
- https://www.pexels.com/photo/airplane-flying-against-sky-327331/
- https://www.pexels.com/photo/beautiful-girl-in-white-and-yellow-floral-dress-covering-her-face-with-her-hand-3771639/
- https://www.pexels.com/photo/beige-and-green-house-2439595/
- https://www.pexels.com/photo/blue-sedan-on-snow-849836/
- https://www.pexels.com/photo/man-in-red-polo-shirt-3779453/
- https://www.pexels.com/photo/toddler-with-red-adidas-sweat-shirt-783941/
- https://www.pexels.com/photo/two-women-sitting-on-vehicle-roofs-2409681/
- https://www.pngitem.com/middle/hwwohTR\_explosion-transparent-file-cartoon-explosion-png-png-download/
- https://www.probytes.net/blog/games-made-with-python/
- https://www.programiz.com/python-programming/
- https://www.python.org/about/success/ilm/
- https://www.pythonforbeginners.com/learn-python/benefits-of-learning-python
- https://www.quora.com/Are-there-any-well-known-games-that-were-coded-in-Python
- https://www.quora.com/What-is-a-CSV-file-and-its-uses
- https://www.w3schools.com/python/python\_try\_except.asp
- https://www.w3schools.com/python/ref\_string\_replace.asp
- https://www.youtube.com/watch?v=16AfQUAyv5M
- https://www.youtube.com/watch?v=Aim\_7fC-inw
- https://www.youtube.com/watch?v=Klp2Q462chU
- https://www.youtube.com/watch?v=yaU6QFawRYY
- https://www.zibtek.com/blog/the-incredible-growth-of-python/
