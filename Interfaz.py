import tkinter as tk
#def PONG():
#    import ProyectoPONG as PONG 
wn = tk.Tk()
wn.title("PROYECTO ARCADEMY")
wn.configure(background="black")
#wn.iconbitmap("Joistic.ico")
#wn.geometry("800x650")
wn.configure(bd = 25)
wn.configure(relief="sunken")
wn.config(cursor="pirate")

miframe = tk.Frame()
miframe.pack(side="top")
miframe.config(bg= "dark gray")
miframe.config(width="1200", height="300")
miframe.config(bd = 15)
miframe.config(relief="groove")
miframe.config(cursor="star")

Etiqueta = tk.Label(miframe, text="ARCADEMY", fg ="black", font=("Castellar", 32))
Etiqueta.place(x="450", y="20")



opcion = tk.StringVar(wn)
opcion.set('Opciones')
Etiqueta2 = tk.Label(miframe, text="OPCIONES", fg ="black", font=("Castellar", 20), textvariable = opcion)
Etiqueta2.place(x="525", y="90")
opciones = [PONG]
Opciones = tk.OptionMenu(wn, opcion, *opciones)
Opciones.pack(side="left", padx = 530, pady = 0)


wn.mainloop()
