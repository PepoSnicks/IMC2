import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
import os

def calcular_imc(peso, altura, sexo, edad):
    """
    Calcula el Índice de Masa Corporal (IMC) según las fórmulas proporcionadas.
    """
    ks = 1.0 if sexo == "Masculino" else 1.1
    ka = 1 + 0.01 * (edad - 25)
    imc = peso / (altura ** 2) * ks * ka
    return imc

def mostrar_resultado():
    """
    Muestra el IMC calculado en la GUI.
    """
    try:
        peso = float(peso_entry.get())
        altura = float(altura_entry.get())
        sexo = sexo_var.get()
        edad = int(edad_entry.get())
        
        imc = calcular_imc(peso, altura, sexo, edad)
        resultado_label.config(text=f"Su Índice de Masa Corporal es: {imc:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

def guardar_datos():
    """
    Guarda los datos ingresados en un archivo CSV con el nombre de la persona.
    Si el archivo no existe, se crea.
    """
    nombre = nombre_entry.get()
    if not nombre:
        messagebox.showerror("Error", "Por favor ingrese su nombre.")
        return

    archivo_csv = f'{nombre}.csv'
    try:
        with open(archivo_csv, mode='w', newline='') as file:  # 'w' para escribir datos
            writer = csv.writer(file)
            writer.writerow(["Peso", "Altura", "Sexo", "Edad", "Indice de Masa Corporal"])
            
            peso = float(peso_entry.get())
            altura = float(altura_entry.get())
            sexo = sexo_var.get()
            edad = int(edad_entry.get())
            
            imc = calcular_imc(peso, altura, sexo, edad)
            
            writer.writerow([peso, altura, sexo, edad, imc])
            
            messagebox.showinfo("Guardado", f"Datos guardados exitosamente en {archivo_csv}.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar los datos: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo del Índice de Masa Corporal")

# Evitar redimensionamiento de la ventana
ventana.resizable(False, False)

# Función para cargar y redimensionar imágenes
def cargar_imagen(ruta, tamaño):
    if not os.path.exists(ruta):
        messagebox.showerror("Error", f"No se encontró la imagen en la ruta: {ruta}")
        ventana.destroy()
        exit()
    try:
        imagen = Image.open(ruta)
        imagen = imagen.resize(tamaño, Image.LANCZOS)  # Corregido a Image.LANCZOS para redimensionar correctamente
        return ImageTk.PhotoImage(imagen)
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al cargar la imagen {ruta}: {str(e)}")
        ventana.destroy()
        exit()

# Cargar imagen de fondo
fondo_imagen = cargar_imagen('C:/Users/jlsau/OneDrive/Escritorio/Gui imagenes/IMC con imagenes/blanco.png', (ventana.winfo_screenwidth(), ventana.winfo_screenheight()))

# Crear una etiqueta para la imagen de fondo
fondo_label = tk.Label(ventana, image=fondo_imagen)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)  # Colocar la etiqueta sobre toda la ventana

# Cargar imágenes para los botones
calcular_photo = cargar_imagen('C:/Users/jlsau/OneDrive/Escritorio/Gui imagenes/IMC con imagenes/IMC.png', (110, 50))
guardar_photo = cargar_imagen('C:/Users/jlsau/OneDrive/Escritorio/Gui imagenes/IMC con imagenes/IMC2.png', (110, 50))

# Cargar imagen adicional (imss.png) para mostrar debajo del campo de edad
imss_photo = cargar_imagen('C:/Users/jlsau/OneDrive/Escritorio/Gui imagenes/IMC con imagenes/imss.png', (150, 100))

# Función para cambiar cursor a una manita cuando se pase sobre los botones
def cambiar_cursor_manita(event):
    event.widget.configure(cursor="hand2")

# Etiqueta para mostrar el resultado del IMC
resultado_label = tk.Label(ventana, text="", font=("Times", 12, "bold"), fg="blue", anchor="center")
resultado_label.grid(row=6, column=0, columnspan=2, pady=10)

# Botón para calcular IMC y mostrar resultado
calcular_button = tk.Button(ventana, image=calcular_photo, command=mostrar_resultado)
calcular_button.grid(row=7, column=0, pady=10)
calcular_button.bind("<Enter>", cambiar_cursor_manita)  # Cambiar cursor al pasar sobre el botón

# Botón para guardar datos en CSV
guardar_button = tk.Button(ventana, image=guardar_photo, command=guardar_datos)
guardar_button.grid(row=7, column=1, pady=10)
guardar_button.bind("<Enter>", cambiar_cursor_manita)  # Cambiar cursor al pasar sobre el botón

# Campos de entrada
tk.Label(ventana, text="Nombre:", bg="#FFFFFF", font=("Times")).grid(row=0, column=0, padx=10, pady=5)
nombre_entry = tk.Entry(ventana)
nombre_entry.grid(row=0, column=1)

tk.Label(ventana, text="Peso (kg):", bg="#FFFFFF", font=("Times")).grid(row=1, column=0, padx=10, pady=5)
peso_entry = tk.Entry(ventana)
peso_entry.grid(row=1, column=1)

tk.Label(ventana, text="Altura (m):", bg="#FFFFFF", font=("Times")).grid(row=2, column=0, padx=10, pady=5)
altura_entry = tk.Entry(ventana)
altura_entry.grid(row=2, column=1)

tk.Label(ventana, text="Sexo:", bg="#FFFFFF", font=("Times")).grid(row=3, column=0, padx=10, pady=5)
sexo_var = tk.StringVar(ventana)
sexo_var.set("Masculino")  
tk.Radiobutton(ventana, text="Masculino", variable=sexo_var, value="Masculino", bg="#FFFFFF").grid(row=3, column=1, sticky="w")
tk.Radiobutton(ventana, text="Femenino", variable=sexo_var, value="Femenino", bg="#FFFFFF").grid(row=3, column=2, sticky="w")

tk.Label(ventana, text="Edad (años):", bg="#FFFFFF", font=("Times")).grid(row=4, column=0, padx=10, pady=5)
edad_entry = tk.Entry(ventana)
edad_entry.grid(row=4, column=1)

# Etiqueta para la imagen adicional (imss.png)
imss_label = tk.Label(ventana, image=imss_photo)
imss_label.grid(row=5, column=0, columnspan=2, pady=5)  # Colocar la imagen debajo del campo de "Edad" y antes de los botones

ventana.mainloop()
