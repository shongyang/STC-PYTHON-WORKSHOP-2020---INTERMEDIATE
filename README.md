# STC-PYTHON-WORKSHOP-2020---INTERMEDIATE
Resource, materials, lesson files, and other stuff for Sunway Tech Club's Python Workshop 2020 !

🐍 **STC-PYTHON-WORKSHOP-2020**

🔖  **Topics covered**

Slides viewable here: bit.ly/stcpyw20ifs

- CSV: Exercise #1 (https://bit.ly/3js5WPf), Exercise #2 (https://bit.ly/3kjcnFv)
- Pandas: Exercise #1 (https://bit.ly/37uLCdm), Exercise #2 (https://bit.ly/3md05ia)
- Tkinter: Exercise #1 (https://bit.ly/3ogdRm4), Exercise #2 (https://bit.ly/35gZYvk), Exercise #3 (https://bit.ly/3dJrKEE)


💡  **Intermediate Project**

An annoying, CSV/Pandas-based desktop alarm (wrapped in a Tkinter GUI) that plays audio when triggered by an event you&#39;ve &quot;committed&quot; to, e.g. meeting, online lesson. Just so you know… could be paired with a scraper script that gets activated when the hour has come (or just about anything)!

Download buggy, heavy .exe version here: bit.ly/35mvvff

If the .exe in the &quot;dist&quot; folder doesn&#39;t work, I think you&#39;ll need to go to &quot;ALARM.PY EXE\_\_pycache\_\_\alarm.cpython-37.pyc&quot; and run it from there. Brownie points awarded to anyone who can fix this problem.

![](RackMultipart20201021-4-1yz97ug_html_2c4f0c3bfc9f1f47.png) ![](RackMultipart20201021-4-1yz97ug_html_a52744d1422e028a.png)

🗺️  **Getting Started**

**## Libraries required:**

```from tkcalendar import DateEntry

from playsound import playsound

from tkinter import messagebox

from tkinter import filedialog

from datetime import datetime

from datetime import date

from tkinter import ttk

from tkinter import \*

import pandas as pd

import tkinter.ttk

import time
```

**## Ready-made functions for you:**

```
def set\_upcoming\_text(df):

date\_list = df[&quot;date&quot;].tolist()

hour\_list = df[&quot;hour&quot;].tolist()

minute\_list = df[&quot;minute&quot;].tolist()

description\_list = df[&quot;description&quot;].tolist()

text = &quot;&quot;

for i in range(len(df)):

text = (

text

+ &quot;\n&quot;

+ str(date\_list[i])

+ &quot; | &quot;

+ str(hour\_list[i])

+ &quot;:&quot;

+ str(minute\_list[i])

+ &quot; | &quot;

+ str(description\_list[i])

+ &quot;\n&quot;

+ &quot;---------------------------------------------------------------------------------------------------------------------------------------------------------------&quot;

+ &quot;\n&quot;

)

upcoming\_text.delete(1.0, END)

upcoming\_text.insert(&quot;end-1c&quot;, text)

def set\_past\_text(df):

date\_list = df[&quot;date&quot;].tolist()

hour\_list = df[&quot;hour&quot;].tolist()

minute\_list = df[&quot;minute&quot;].tolist()

description\_list = df[&quot;description&quot;].tolist()

text = &quot;&quot;

for i in range(len(df)):

text = (

text

+ &quot;\n&quot;

+ str(date\_list[i])

+ &quot; | &quot;

+ str(hour\_list[i])

+ &quot;:&quot;

+ str(minute\_list[i])

+ &quot; | &quot;

+ str(description\_list[i])

+ &quot;\n&quot;

+ &quot;---------------------------------------------------------------------------------------------------------------------------------------------------------------&quot;

+ &quot;\n&quot;

)

past\_text.delete(1.0, END)

past\_text.insert(&quot;end-1c&quot;, text)

def check\_alarm():

# reading excel file

df = pd.read\_excel(excel\_file\_path)

desc = &quot;&quot;

# matching time and date

today\_date = date.today()

today\_date = str(today\_date.strftime(&quot;%d/%m/%y&quot;))

now\_time = datetime.now()

current\_time = now\_time.strftime(&quot;%H:%M&quot;)

for index, row in df.iterrows():

# checking only those alarm which are still pending and ignore else

if df[&quot;status&quot;][index] != &quot;finish&quot;:

alarm\_date = row[&quot;date&quot;]

hour = row[&quot;hour&quot;]

minute = row[&quot;minute&quot;]

hour\_str = minute\_str = hour\_minute\_str = &quot;&quot;

# converting hours from 1 to 01, 9 ot 09 etc

if hour \&gt;= 0 and hour \&lt;= 9:

hour\_str = &quot;0&quot; + str(hour)

else:

hour\_str = str(hour)

# converting minutes from 1 to 01, 9 ot 09 etc

if minute \&gt;= 0 and minute \&lt;= 9:

minute\_str = &quot;0&quot; + str(minute)

else:

minute\_str = str(minute)

# matching current time with all alarms time

hour\_minute\_str = hour\_str + &quot;:&quot; + minute\_str

if today\_date == alarm\_date and current\_time == hour\_minute\_str:

df[&quot;status&quot;][index] = &quot;finish&quot;

desc = df[&quot;description&quot;][index]

df.to\_excel(excel\_file\_path, index=False)

return (True, desc)

return (False, &quot;&quot;)

def user\_input\_values\_to\_excel(df1, date, hours, minutes, description, mp3\_filepath):

df2 = pd.DataFrame(

{

&quot;date&quot;: [date],

&quot;hour&quot;: [hours],

&quot;minute&quot;: [minutes],

&quot;description&quot;: [description],

&quot;mp3 file path&quot;: [mp3\_filepath],

}

)

df1 = df1.append(df2)

# Create a Pandas Excel writer using XlsxWriter as the engine.

writer = pd.ExcelWriter(excel\_file\_path, engine=&quot;xlsxwriter&quot;)

# Convert the dataframe to an XlsxWriter Excel object.

df1.to\_excel(writer, sheet\_name=&quot;Sheet1&quot;, index=False)

# Close the Pandas Excel writer and output the Excel file.

writer.save()

def sorting\_table\_on\_hour(df1):

# sorting on base of hours

df = pd.read\_excel(excel\_file\_path)

result = df.sort\_values(&quot;hour&quot;)

result.to\_excel(excel\_file\_path, index=False)

return result

def stop\_loop():

global flag

flag = False

def upload\_mp3\_file():

global mp3\_filepath

mp3\_filepath = filedialog.askopenfilename(

initialdir=&quot;/&quot;,

title=&quot;Select A MP3 File&quot;,

filetype=((&quot;mp3&quot;, &quot;\*.mp3&quot;), (&quot;Äll Files&quot;, &quot;\*.\*&quot;)),

)

def set\_alarm(btn\_obj):

global flag

flag = True

date = calendar.get()

hours = hour\_input.get()

minutes = minute\_input.get()

description = description\_input.get()

hour\_input.delete(0, &quot;end&quot;)

minute\_input.delete(0, &quot;end&quot;)

description\_input.delete(0, &quot;end&quot;)

try:

if int(hours) \&gt; 24 or int(minutes) \&gt; 60 or description == &quot;&quot;:

messagebox.showinfo(&quot;Alert&quot;, &quot;invalid field!&quot;)

else:

df = pd.read\_excel(excel\_file\_path, parse\_dates=False)

# writing user input values to excel file

df = user\_input\_values\_to\_excel(

df, date, hours, minutes, description, mp3\_filepath

)

df = sorting\_table\_on\_hour(df)

# reading data frames from excel file

df = pd.read\_excel(excel\_file\_path, parse\_dates=False)

upcoming\_df = df.loc[df[&quot;status&quot;] != &quot;finish&quot;]

past\_df = df.loc[df[&quot;status&quot;] == &quot;finish&quot;]

# fill UPCOMING alarm field

set\_upcoming\_text(upcoming\_df)

# fill PAST alarm field

set\_past\_text(past\_df)

# ringing alarm if time matches

while True:

# funtion for checking current time matches any alarm or not

alarm\_match\_flag, desc = check\_alarm()

if alarm\_match\_flag:

# ring alarm tone

playsound(mp3\_filepath)

messagebox.showinfo(&quot;Alarm&quot;, desc)

# reading data frames from excel file

df = pd.read\_excel(excel\_file\_path, parse\_dates=False)

upcoming\_df = df.loc[df[&quot;status&quot;] != &quot;finish&quot;]

past\_df = df.loc[df[&quot;status&quot;] == &quot;finish&quot;]

# fill UPCOMING alarm field

set\_upcoming\_text(upcoming\_df)

# fill PAST alarm field

set\_past\_text(past\_df)

if flag:

alarm\_window.update()

time.sleep(1.0)

else:

break

except:

messagebox.showinfo(&quot;Alert&quot;, &quot;Please fill fields!&quot;)

hour\_input.delete(0, END)

minute\_input.delete(0, END)

description\_input.delete(0, END)
```

**## Unique GUI elements for reference**

```
alarm\_window = Tk() # creating tkinger window

alarm\_window.title(&quot;STC Python Workshop 2020 - Intermediate Project&quot;) # set title of window

alarm\_window.iconbitmap = &quot;python-logo-2b.ico&quot; #icon

w = alarm\_window.winfo\_screenwidth() # getting current window width

h = alarm\_window.winfo\_screenheight() # getting current window height

alarm\_window.geometry(&quot;%dx%d+0+0&quot; % (w, h)) # setting size of window to full

alarm\_window.resizable(width=True, height=True) # fixing size of window

# for date and time label

date\_calendar = Label(alarm\_window, text=&quot;Select Date/Time&quot;)

date\_calendar.config(font=(&quot;Helvetica&quot;, 15))

date\_calendar.grid(row=0, column=0, columnspan=5)

# for description label

description\_label = Label(alarm\_window, text=&quot;Description&quot;)

description\_label.config(font=(&quot;Helvetica&quot;, 15))

description\_label.grid(row=0, column=6, padx=250)

# for mp3 label

mp3\_label = Label(alarm\_window, text=&quot;mp3 upload&quot;)

mp3\_label.config(font=(&quot;Helvetica&quot;, 15))

mp3\_label.grid(row=0, column=7, padx=100)

########## row = 1 #########

# for calendar pop-up

calendar = DateEntry(

alarm\_window,

width=12,

background=&quot;darkblue&quot;,

foreground=&quot;white&quot;,

borderwidth=2,

date\_pattern=&quot;dd/mm/yy&quot;,

)

calendar.config(font=(&quot;Helvetica&quot;, 15))

calendar.grid(row=1, column=0)

# for hour label

hour\_label = Label(alarm\_window, text=&quot;Hour:&quot;)

hour\_label.config(font=(&quot;Helvetica&quot;, 15))

hour\_label.grid(row=1, column=1)

# for hour input

hour\_input = Entry(alarm\_window, borderwidth=3, width=3)

hour\_input.config(font=(&quot;Helvetica&quot;, 15))

hour\_input.grid(row=1, column=2)

# for minute label

minute\_label = Label(alarm\_window, text=&quot;Minute:&quot;)

minute\_label.config(font=(&quot;Helvetica&quot;, 15))

minute\_label.grid(row=1, column=3)

# for minute input

minute\_input = Entry(alarm\_window, borderwidth=3, width=3)

minute\_input.config(font=(&quot;Helvetica&quot;, 15))

minute\_input.grid(row=1, column=4)

# for description input

description\_input = Entry(alarm\_window, borderwidth=3, width=40)

description\_input.config(font=(&quot;Helvetica&quot;, 15))

description\_input.grid(row=1, column=6)

# for upload mp3 file

upload\_btn = Button(alarm\_window, text=&quot;upload audio&quot;, bd=3, command=upload\_mp3\_file)

upload\_btn.config(font=(&quot;Helvetica&quot;))

upload\_btn.grid(row=1, column=7)

########## row = 2 ##########

commit\_btn = Button(

alarm\_window, text=&quot;commit&quot;, bd=3, command=lambda: set\_alarm(commit\_btn)

)

commit\_btn.config(font=(&quot;Helvetica&quot;))

commit\_btn.grid(row=2, column=7, pady=20)

########## row = 3 ##########

line\_canvas = Canvas(alarm\_window, width=1350, height=2, background=&quot;black&quot;)

line\_canvas.grid(row=3, column=0, columnspan=9)

line\_canvas.create\_line(0, 0, 400, 400, fill=&quot;black&quot;)

########## row = 4 ##########

# for minute label

upcoming\_label = Label(alarm\_window, text=&quot;Upcoming Alarms&quot;)

upcoming\_label.config(font=(&quot;Helvetica&quot;, 15))

upcoming\_label.grid(row=4, column=0, columnspan=2)

new\_alarm\_btn = Button(alarm\_window, text=&quot;stop&quot;, bd=3, command=stop\_loop)

new\_alarm\_btn.config(font=(&quot;Helvetica&quot;))

new\_alarm\_btn.grid(row=4, column=7, columnspan=7)

########## row = 5 ##########

# for upcoming text field

upcoming\_text = Text(alarm\_window, borderwidth=2, width=90, height=10)

upcoming\_text.config(font=(&quot;Helvetica&quot;, 12))

upcoming\_text.grid(row=5, column=2, columnspan=5)

scrollbar = Scrollbar(alarm\_window, command=upcoming\_text.yview)

scrollbar.grid(row=5, column=7, sticky=W, ipady=70)

upcoming\_text.config(yscrollcommand=scrollbar.set)

########## row = 6 ##########

line\_canvas = Canvas(alarm\_window, width=1350, height=2, background=&quot;black&quot;)

line\_canvas.grid(row=6, column=0, columnspan=9, pady=20)

line\_canvas.create\_line(0, 0, 400, 400, fill=&quot;black&quot;)

########## row = 7 ##########

# for minute label

past\_label = Label(alarm\_window, text=&quot;Past Alarms&quot;)

past\_label.config(font=(&quot;Helvetica&quot;, 15))

past\_label.grid(row=7, column=0, columnspan=2)

########## row = 8 ##########

# for upcoming text field

past\_text = Text(alarm\_window, borderwidth=2, width=90, height=10)

past\_text.config(font=(&quot;Helvetica&quot;, 12))

past\_text.grid(row=8, column=2, columnspan=5)

scrollbar = Scrollbar(alarm\_window, command=past\_text.yview)

scrollbar.grid(row=8, column=7, sticky=W, ipady=70)

past\_text.config(yscrollcommand=scrollbar.set)

alarm\_window.mainloop() # compiling all objects in window
```

💌  **Last but not least**

**This repository is part of Sunway Tech Club&#39;s** _ **Python Workshop 2020** _

- Session 1 (Beginner): https://github.com/JustNunuz/STC-PYTHON-WORKSHOP-2020
- Session 2 (Intermediate): https://github.com/JustNunuz/STC-PYTHON-WORKSHOP-2020
- Session 3 (Project / Advanced): https://github.com/JustNunuz/STC-PYTHON-WORKSHOP-2020

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
