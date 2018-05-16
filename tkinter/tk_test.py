# instalar modulo 

# vía anaconda
# conda install -c anaconda tk 

#vía descarga
# seguir instrucciones de la documentación
# http://www.tkdocs.com/tutorial/install.html

import tkinter as tk

window = tk.Tk()

# adds a tittle to the window
window.title("My app")

# Sizes the window when first appears,
# measured in pixels
window.geometry("400x400")

#---------label-------------- 
prompt = tk.Label(text = "hello world, tkinter app",
font = ("Times New Roman", 20))
prompt.grid()

#--------Entry Fields----------
entry_field = tk.Entry()
entry_field.grid()

#-----------Button-------------
button1 = tk.Button(text = "Click on me ", bg = "red")
button1.grid()

#-------- text Fields-----------
text_field = tk.Text(master = window, height = 10, width = 30)
text_field.grid()

# makes the frame appear on screen
window.mainloop()

# documentación
# http://www.tkdocs.com/index.html