from tkinter import filedialog

def open_file():
    file=filedialog.askopenfile(initialdir="/", title="select file", filetypes=(("image", ".jpg"), ("all files", "*.*")))
    img=file.name
    return img

def save_file():
    files = [('Image Files', '*.jpg')] 
    destination = filedialog.asksaveasfilename(title="Select where to save the final file",filetypes = files, defaultextension = files)
    return destination