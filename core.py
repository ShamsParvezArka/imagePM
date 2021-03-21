import pyperclip
from tkinter import *
from tkinter import filedialog
from exif import Image


# Core Function
def file_browser():
    filename = filedialog.askopenfile(initialdir = "/arka/programming/", title = "select file", filetypes = (("Images", ".jpg .png .jpeg"),))
    lbl2_blank.configure(text = "[ √ ]")    
    
    path0 = filename.name               # Path of the selected image
    with open(path0, 'rb') as file_obj:
        selected_file = Image(file_obj)

    entry0.delete(0, 'end')
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry5.delete(0, 'end')
    
#   if selected_file.has_exif == True:       # Ckeckpoint of metadata's existance 
#        lbl4.configure(text = "Bingo", fg = "green")
#    else:
#        lbl4.configure(text = "Opps! No metadata found ", fg = "red")

    flash_info = selected_file.flash
    if flash_info.flash_fired == True:
        entry2.insert(10, "Yes")
    else:
        entry2.insert(10, "No")

    date_time = selected_file.datetime
    entry1.insert(10, date_time)

    devicename = selected_file.model
    entry0.insert(10, devicename)

    focalength = selected_file.focal_length
    entry4.insert(10, focalength)

    try:
        lati = selected_file.gps_latitude
        entry3.insert(10, lati)
    except AttributeError:
        entry3.insert(10, "Not Found")

    try:
        longi = selected_file.gps_longitude
        entry5.insert(10, longi)
    except AttributeError:
        entry5.insert(10, "Not Found")

def copy0():
    x = entry3.get()
    pyperclip.copy(x)
def copy1():
    y = entry5.get()
    pyperclip.copy(y)


# GUI code
window = Tk()

window.title("Metadata sucker")
window.geometry("530x150")


# r0c0
lbl0_blank = Label(window, text = "", width = 10)
lbl0_blank.grid(row = 0, column = 0)
#r0c1
lbl3_blank = Label(window, text = "", width = 10)
lbl3_blank.grid(row = 0, column = 1)
#r0c2
lbl2_blank = Label(window, text = "", width = 5)
lbl2_blank.grid(row = 0, column = 2,)
#r0c3
lbl1 = Label(window, text = "Input image", width = 10, fg = "black")
lbl1.grid(row = 0, column = 3, sticky = 'w')
#r0c4
browse_btn = PhotoImage(file = 'icons/button.png')
btn_explore = Button(window, image = browse_btn, borderwidth = 0, command = file_browser)
btn_explore.grid(row = 0, column = 4)


#r1c2
lbl4 = Label(window, text = "", width = 5)
lbl4.grid(row = 1, column = 2)


#r2c0
lbl5 = Label(window, text = "Device", width = 10)
lbl5.grid(row = 2, column = 0)
#r2c1
entry0 = Entry(window, text = "", width = 11)
entry0.grid(row = 2, column = 1)
#r2c3
lbl6 = Label(window, text = "Date/Time", width = 10)
lbl6.grid(row = 2, column = 3)
#r2c4
entry1 = Entry(window, text = "", width = 18)
entry1.grid(row = 2, column = 4)


#r3c0
lbl7 = Label(window, text = "Flash fired", width = 10)
lbl7.grid(row = 3, column = 0)
#r3c1
entry2 = Entry(window, text = "", width = 11)
entry2.grid(row = 3, column = 1)
#r3c3
lbl8 = Label(window, text = "Altitude", width = 10)
lbl8.grid(row = 3, column = 3)
#r3c4
entry3 = Entry(window, text = "", width = 18)
entry3.grid(row = 3, column = 4)
#r3c5
btn_img = PhotoImage(file = 'icons/button0.png')
btn_copy0 = Button(window, image = btn_img, borderwidth = 0 , command = copy0)
btn_copy0.grid(row = 3, column = 5)


#r4c0
lbl9 = Label(window, text = "Focal Length", width = 10)
lbl9.grid(row = 4, column = 0)
#r4c1
entry4 = Entry(window, text = "", width = 11)
entry4.grid(row = 4, column = 1)
#r4c3
lbl10 = Label(window, text = "Longitude", width = 10)
lbl10.grid(row = 4, column = 3)
#r4c4
entry5 = Entry(window, text = "", width = 18)
entry5.grid(row = 4, column = 4)
#r4c5
btn_copy1 = Button(window, image = btn_img, borderwidth = 0, command = copy1)
btn_copy1.grid(row = 4, column = 5)





window.mainloop()
