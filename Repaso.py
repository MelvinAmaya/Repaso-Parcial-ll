from queue import Empty
from PIL import Image,ImageTk
from tkinter import Tk,Button,Label,Entry,filedialog,messagebox,GROOVE
from tkinter.ttk import Combobox

class interfaz():
    def __init__(self):
        self.ventana1 = Empty
        self.ventana2 = Empty
        self.Entradanombre = Empty
        self.Entradaapellido = Empty
        self.Entradafecha = Empty
        self.Entradagenero = Empty
        self.imagen = Entry
        self.archivo = ""
        self.render = Empty


        self.nombre = ""
        self.apellido = ""
        self.fecha = ""
        self.genero = ""
        self.size = (300,300)


    def principal(self):
        self.ventana1 = ventana = Tk()
        ventana.geometry("650x500")
        ventana.title("Registro")
        ventana.resizable(0,0)
        titulo = Label(ventana,text="Instituto Melvin Pereira.")
        titulo.pack()
        self.imagen = Label(ventana,image="",relief=GROOVE,border=10)
        self.imagen.place(x = 40,y = 40,width=300,height=300)
        botonCargar = Button(ventana,text="Cargar Imagen",command=inter.cargarImagen)
        botonCargar.place(x = 110, y = 350,width = 150,height = 40)
        lbNombre = Label(ventana,text="Nombre:")
        lbNombre.place(x = 355,y = 40)
        self.Entradanombre = Entry(ventana)
        self.Entradanombre.place(x = 420,y = 40,width=200)
        lbApellido = Label(ventana,text="Apellido:")
        lbApellido.place(x = 355,y = 80)
        self.Entradaapellido = Entry(ventana)
        self.Entradaapellido.place(x = 420,y = 80,width=200)
        lbFecha = Label(ventana,text="Fecha Nacimiento:")
        lbFecha.place(x = 355,y = 120)
        self.Entradafecha = Entry(ventana)
        self.Entradafecha.place(x = 460,y = 120,width=160)
        lbGenero = Label(ventana,text="Genero:")
        lbGenero.place(x = 355,y = 160)
        self.Entradagenero = Combobox(ventana,state="readonly")
        self.Entradagenero['values']=("Masculino","Femenino","No Especificado")
        self.Entradagenero.place(x = 420,y = 160,width=200)
        botonRegistrar = Button(ventana,text="Registrarce",command=inter.registrarce)
        botonRegistrar.place(x = 420,y = 200,width = 150,height = 40)
        if self.ventana2 is Empty:
            pass
        else:
            self.ventana2.destroy()
        ventana.mainloop()
        

    def Secundaria(self):
        self.ventana1.destroy()
        self.ventana2 = ventana2 = Tk()
        ventana2.title("Resultado")
        ventana2.geometry("700x400")
        lbtitulo = Label(ventana2,text="Alumno Registrado.",font='Helvetica 15 bold')
        lbtitulo.pack()
        lbImagenA = Label(ventana2,image="",relief=GROOVE,border=10)
        imagen3 = Image.open(self.archivo)
        imagen2resiz = imagen3.resize(self.size,Image.Resampling.LANCZOS)
        render3 = ImageTk.PhotoImage(imagen2resiz)
        lbImagenA.configure(image=render3)
        lbImagenA.image = render3
        lbImagenA.place(x = 40,y = 60,width=300,height=300)
        lbNombre2 = Label(ventana2,text=f"Nombre: {self.nombre}",font='Helvetica 14 bold')
        lbNombre2.place(x = 355,y = 60)
        lbApellido2 = Label(ventana2,text=f"Apellido: {self.apellido}",font='Helvetica 14 bold')
        lbApellido2.place(x = 355,y = 100)
        lbFecha2 = Label(ventana2,text=f"Fecha Nacimiento: {self.fecha}",font='Helvetica 14 bold')
        lbFecha2.place(x = 355,y = 140)
        lbGenero2 = Label(ventana2,text=f"Genero: {self.genero}",font='Helvetica 14 bold')
        lbGenero2.place(x = 355,y = 180)
        btn = Button(ventana2,text="Aceptar",command=inter.Aceptar)
        btn.place(x = 355, y = 240,width = 150,height = 40)

        ventana2.mainloop()

    def cargarImagen(self):
        self.archivo = filedialog.askopenfilename(title="Seleccione una imagen",filetypes=(("jpg file","*.jpg"),("png files","*.png"),("all files","*.*")))
        try:
            imagen2 = Image.open(self.archivo)
            imagen2resiz = imagen2.resize(self.size,Image.Resampling.LANCZOS)
            self.render = render2 = ImageTk.PhotoImage(imagen2resiz)
            self.imagen.configure(image=render2)
            self.imagen.image = render2
        except:
            messagebox.showerror("Procesar imagen","Debe seleccionar una imagen jpg.")

    def registrarce(self):
        if self.Entradaapellido.get() != "" and self.Entradanombre.get() != "" and self.Entradafecha.get() != "" and self.Entradagenero.get() != "" and self.archivo != "":
            self.nombre = self.Entradanombre.get()
            self.apellido = self.Entradaapellido.get()
            self.fecha = self.Entradafecha.get()
            self.genero = self.Entradagenero.get()
            inter.Secundaria()
        else:
            messagebox.showerror("Registro","Ingrese todos los datos")
    def Aceptar(self):
        inter.principal()

inter = interfaz()
inter.principal()