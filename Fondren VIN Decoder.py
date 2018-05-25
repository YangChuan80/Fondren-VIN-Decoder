from libvin.decoding import Vin
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

def decodeButton():         
    vin_input = text_VIN.get('1.0', tk.END)[:17]   
    
    if len(vin_input) != 17:
        messagebox.showwarning("Invalid VIN length", 
                               "Sorry, the length of the VIN you have input is wrong. Please check!")
    
    else:   

        # Capitalization:
        vin = vin_input.upper()
        
        try:
            # Parse VIN
            v = Vin(vin)            

            year = v.year    
            country = v.country
            region = v.region.capitalize()
            manufacturer = v.manufacturer
            make = v.make

            # Differentiate Year:    
            if year < 2000:
                year = year + 30

            # Sections    
            text_WMI.delete('1.0', tk.END)
            text_WMI.insert('1.0', vin[:3])  

            text_VDS.delete('1.0', tk.END)
            text_VDS.insert('1.0', vin[3:9])  

            text_SPN.delete('1.0', tk.END)
            text_SPN.insert('1.0', vin[11:])  

            # Parameters
            text_region.delete('1.0', tk.END)
            text_region.insert('1.0', region)  

            text_country.delete('1.0', tk.END)
            text_country.insert('1.0', country)  

            text_manufacturer.delete('1.0', tk.END)
            text_manufacturer.insert('1.0', manufacturer)  

            text_make.delete('1.0', tk.END)
            text_make.insert('1.0', make)  

            text_year.delete('1.0', tk.END)
            text_year.insert('1.0', year)     
            
        except:            
            messagebox.showwarning("Invalid VIN", "Sorry, the VIN you input is invalid. Please check!")  

def about():
    messagebox.showinfo("About", "Author: Chuan Yang")

# Main Frame////////////////////////////////////////////////////////////////////////////////////////
root = tk.Tk()

w = 930 # width for the Tk root
h = 660 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#root.attributes('-fullscreen', True)
root.title('Fondren VIN Decoder')
#root.iconbitmap('Heart.ico')

#///////////Image Title///////////////////////////////
#photo=tk.PhotoImage(file='FrontLight.png')
#label_photo=tk.Label(root, image=photo, relief='sunken', borderwidth=3)
#label_photo.place(x=260,y=35)

#/////////////Text///////////////////////////////////////////////////////////////////

text_VIN=tk.Text(root, width=40,height=1, font=('tahoma', 9), bd=2)
text_VIN.place(x=320, y=90)
label_VIN=tk.Label(root, text='VIN (Vehicle Identification Number):', font=('tahoma', 9))
label_VIN.place(x=340,y=60)

#/////////////////////////////
y_position = 260
text_WMI=tk.Text(root, width=15,height=1, font=('tahoma', 9), bd=2)
text_WMI.place(x=60, y=y_position)
label_WMI=tk.Label(root, text='WMI (World Manufacture Identifier):', font=('tahoma', 9))
label_WMI.place(x=60,y=y_position-30)

text_VDS=tk.Text(root, width=15,height=1, font=('tahoma', 9), bd=2)
text_VDS.place(x=380, y=y_position)
label_VDS=tk.Label(root, text='VDS (Vehicle Descriptor Section):', font=('tahoma', 9))
label_VDS.place(x=380,y=y_position-30)

text_SPN=tk.Text(root, width=25,height=1, font=('tahoma', 9), bd=2)
text_SPN.place(x=660, y=y_position)
label_SPN=tk.Label(root, text='Sequential Production Number:', font=('tahoma', 9))
label_SPN.place(x=660,y=y_position-30)

#//////////////////
y_position = 360
text_manufacturer=tk.Text(root, width=40,height=1, font=('tahoma', 9), bd=2)
text_manufacturer.place(x=60, y=y_position)
label_manufacturer=tk.Label(root, text='Manufacturer:', font=('tahoma', 9))
label_manufacturer.place(x=60,y=y_position-30)

text_year=tk.Text(root, width=15,height=1, font=('tahoma', 9), bd=2)
text_year.place(x=400, y=y_position)
label_year=tk.Label(root, text='Year:', font=('tahoma', 9))
label_year.place(x=400,y=y_position-30)

text_make=tk.Text(root, width=40,height=1, font=('tahoma', 9), bd=2)
text_make.place(x=580, y=y_position)
label_make=tk.Label(root, text='Make:', font=('tahoma', 9))
label_make.place(x=580,y=y_position-30)

#//////////////////////////////////////////////////////////////////////////////////
y_position = 430
text_region=tk.Text(root, width=25,height=1, font=('tahoma', 9), bd=2)
text_region.place(x=60, y=y_position)
label_region=tk.Label(root, text='Region:', font=('tahoma', 9))
label_region.place(x=60,y=y_position-30)

text_country=tk.Text(root, width=25,height=1, font=('tahoma', 9), bd=2)
text_country.place(x=340, y=y_position)
label_country=tk.Label(root, text='Contry:', font=('tahoma', 9))
label_country.place(x=340,y=y_position-30)

text_model=tk.Text(root, width=25,height=1, font=('tahoma', 9), bd=2)
text_model.place(x=600, y=y_position)
label_model=tk.Label(root, text='Model:', font=('tahoma', 9))
label_model.place(x=600,y=y_position-30)

#////////////////////////////////////
y_position = 500

text_body=tk.Text(root, width=25,height=1, font=('tahoma', 9), bd=2)
text_body.place(x=60, y=y_position)
label_body=tk.Label(root, text='Body:', font=('tahoma', 9))
label_body.place(x=60,y=y_position-30)

text_engine=tk.Text(root, width=25,height=1, font=('tahoma', 9), bd=2)
text_engine.place(x=340, y=y_position)
label_engine=tk.Label(root, text='Engine:', font=('tahoma', 9))
label_engine.place(x=340,y=y_position-30)

text_gearbox=tk.Text(root, width=25,height=1, font=('tahoma', 9), bd=2)
text_gearbox.place(x=600, y=y_position)
label_gearbox=tk.Label(root, text='Gearbox:', font=('tahoma', 9))
label_gearbox.place(x=600,y=y_position-30)


#/////////////Button///////////////////////////////////////////////////////////////


button_decode=ttk.Button(root, text='Decode', width=40, command=decodeButton)
button_decode.place(x=340, y=140)

button_about=ttk.Button(root, text='About...', width=20, command=about)
button_about.place(x=180, y=580)

button_close=ttk.Button(root, width=20, text='Exit', command=root.destroy)
button_close.place(x=600, y=580)


root.mainloop()