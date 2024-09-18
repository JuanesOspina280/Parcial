#
# RESPUESTA A PREGUNTA 7:
# b. Crea la ventana principal de una aplicación gráfica.
#

import tkinter as tk

from tkinter import messagebox

#
# RESPUESTA A PREGUNTA 6.
# d. Delimitar bloques de código, como bucles, condicionales, definiciones de funciones y clases.
#

# Clase para el gestor de recetas
class Receta:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes

#
# RESPUESTA A PREGUNTA 2:
# b. Definir una plantilla para crear objetos
#
class GestorRecetas:
    
    #
    # RESPUESTA A PREGUNTA 3:
    # c. Inicializa los atributos de un objeto cuando se crea una nueva instancia de una clase.
    #
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, nombre, ingredientes):
        receta = Receta(nombre, ingredientes)
        self.recetas.append(receta)
        messagebox.showinfo("Gestor de Recetas", f"Receta '{nombre}' agregada correctamente.")

    def ver_recetas(self):
        if not self.recetas:
            messagebox.showinfo("Gestor de Recetas", "No hay recetas guardadas.")
        else:
            recetas_str = "\n".join([f"{i + 1}. {r.nombre}" for i, r in enumerate(self.recetas)])
            messagebox.showinfo("Recetas", recetas_str)


# Interfaz con Tkinter
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Pacientes y Recetas")
        self.gestor_recetas = GestorRecetas()
        self.menu_principal()

    def limpiar_ventana(self):
        # Borra todos los widgets de la ventana actual
        for widget in self.root.winfo_children():
            widget.destroy()

    def menu_principal(self):
        self.limpiar_ventana()
        #
        # RESPUESTA A PREGUNTA 9:
        # c. Mostrar texto o imágenes en una interfaz grafica.
        #
        tk.Label(self.root, text="Menú Principal", font=("Arial", 20)).pack(pady=10)
        tk.Button(self.root, text="Gestor de Recetas", command=self.menu_recetas, width=30).pack(pady=10)
        tk.Button(self.root, text="Salir", command=self.root.quit, width=30).pack(pady=10)

    def menu_recetas(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Gestor de Recetas", font=("Arial", 20)).pack(pady=10)
        tk.Button(self.root, text="Agregar Receta", command=self.agregar_receta, width=30).pack(pady=10)
        tk.Button(self.root, text="Ver Recetas", command=self.ver_recetas, width=30).pack(pady=10)
        tk.Button(self.root, text="Volver al Menú Principal", command=self.menu_principal, width=30).pack(pady=10)

    def agregar_receta(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Agregar Receta", font=("Arial", 20)).pack(pady=10)
        tk.Label(self.root, text="Nombre de la receta:").pack()
        nombre_entry = tk.Entry(self.root)
        nombre_entry.pack()
        tk.Label(self.root, text="Ingredientes (separados por comas):").pack()
        ingredientes_entry = tk.Entry(self.root)
        ingredientes_entry.pack()

        def guardar_receta():
            nombre = nombre_entry.get()
            #
            # RESPUESTA A PREGUNTA 5.
            # d. Dividir una cadena en subcadenas utilizando un delimitador especificado y devuelve una lista de subcadenas resultantes.
            #
            ingredientes = ingredientes_entry.get().split(",")
            self.gestor_recetas.agregar_receta(nombre, ingredientes)

        tk.Button(self.root, text="Guardar Receta", command=guardar_receta).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.menu_recetas).pack(pady=10)

    def ver_recetas(self):
        self.gestor_recetas.ver_recetas()

# Inicializar la aplicación
root = tk.Tk()
app = App(root)

#
# RESPUESTA A PREGUNTA 8:
# c. mainloop().
#
root.mainloop()
