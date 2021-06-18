"""
Created on Fri Jun 18 2021

@author: Han Yang, Academia Sinica, Institute of Economics
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from functools import partial
import os
import subprocess


#function that assigns file path
def openfile(entryBox):
    filename = filedialog.askopenfilename()
    entryBox.delete(0, tk.END)
    entryBox.insert(tk.END, filename)
   
#function that assigns folder path
def openfolder(entryBox):
    filename = filedialog.askdirectory()
    entryBox.delete(0, tk.END)
    entryBox.insert(tk.END, filename)
    
    
root = tk.Tk()
root.title('Blender Background Rendering')
root.geometry("400x250")

#Load blender path
filesSelector = ttk.Frame(root)
filesSelector.pack()
filesSelector.config(height = 600, width = 400)
fileEntry1=ttk.Entry(filesSelector)
fileEntry1.grid(row=0,column=1)
selectButton1=ttk.Button(filesSelector,text="Select your Blender main program folder",command=partial(openfolder,fileEntry1))
selectButton1.grid(row=0,column=2)

#load .blend file
fileEntry2=ttk.Entry(filesSelector)
fileEntry2.grid(row=1,column=1)
selectButton2=ttk.Button(filesSelector,text="Select your .blend file location",command=partial(openfile,fileEntry2))
selectButton2.grid(row=1,column=2)

#set render output path
fileEntry3=ttk.Entry(filesSelector)
fileEntry3.grid(row=2,column=1)
selectButton3=ttk.Button(filesSelector,text="Select render output path",command=partial(openfolder,fileEntry3))
selectButton3.grid(row=2,column=2)

def click_action():
    msg_1 = 'Your Blender folder: ' + fileEntry1.get()
    print_blender_folder = tk.Label(root,text = msg_1)
    print_blender_folder .pack()
    
    msg_2 = 'Your .blende file: ' +fileEntry2.get()
    print_blender_file = tk.Label(root,text = msg_2)
    print_blender_file .pack()
    
    msg_3 = 'Your render output path: ' +fileEntry3.get()+'/'
    print_render_path = tk.Label(root,text = msg_3)
    print_render_path.pack()
    
    #Now start render
    ##open blender
    cmd_load_blender = 'cd '+'"'+fileEntry1.get()+'"'
    ##Render
    cmd_render = 'blender -b '+'"'+fileEntry2.get()+'"'+' -o '+'"'+ fileEntry3.get()+'/'+'"'+' -a'
    
    #Write Commands in to .bat file
    render_bat_temp = open(r'render.bat','w+')
    render_bat_temp.write(cmd_load_blender+'\n')
    render_bat_temp.write(cmd_render)
    render_bat_temp.close()
    
    #Run .bat file
    subprocess.call([r'render.bat'])
    #delete .bat file
    os.remove("render.bat")
    
    print_completion = tk.Label(root, text = 'Render completed')
    print_completion.pack()

myButton = tk.Button(root,text = 'Start background rendering', padx = 75, pady =20,command=click_action)
myButton.pack()


root.mainloop()


