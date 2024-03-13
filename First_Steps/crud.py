import sqlite3
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk


# Función para conectar a la base de datos
def conectar_bd():
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    return conexion, cursor


# Crear la tabla libros si no existe
def crear_tabla():
    conexion, cursor = conectar_bd()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY,
            titulo TEXT,
            autor TEXT,
            anio INTEGER
        )
    """
    )
    conexion.commit()
    conexion.close()


# Función para insertar un nuevo libro
def agregar_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    anio = entry_anio.get()
    if titulo and autor and anio:
        conexion, cursor = conectar_bd()
        cursor.execute(
            "INSERT INTO libros (titulo, autor, anio) VALUES (?, ?, ?)",
            (titulo, autor, anio),
        )
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", "Libro agregado correctamente.")
        mostrar_libros()
        limpiar_campos()
    else:
        messagebox.showerror("Error", "Por favor completa todos los campos.")


# Función para mostrar todos los libros
def mostrar_libros():
    for row in tree.get_children():
        tree.delete(row)
    conexion, cursor = conectar_bd()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    for libro in libros:
        tree.insert("", "end", values=libro)
    conexion.close()


# Función para limpiar los campos de entrada
def limpiar_campos():
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_anio.delete(0, tk.END)


# Función para obtener el libro seleccionado
def obtener_libro_seleccionado():
    try:
        item = tree.selection()[0]
        return tree.item(item, "values")
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor selecciona un libro.")
        return None


# Función para eliminar un libro
def eliminar_libro():
    libro = obtener_libro_seleccionado()
    if libro:
        id_libro = libro[0]
        conexion, cursor = conectar_bd()
        cursor.execute("DELETE FROM libros WHERE id=?", (id_libro,))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", "Libro eliminado correctamente.")
        mostrar_libros()


# Función para modificar un libro
def modificar_libro():
    libro = obtener_libro_seleccionado()
    if libro:
        id_libro = libro[0]
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        anio = entry_anio.get()
        if titulo and autor and anio:
            conexion, cursor = conectar_bd()
            cursor.execute(
                "UPDATE libros SET titulo=?, autor=?, anio=? WHERE id=?",
                (titulo, autor, anio, id_libro),
            )
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Libro modificado correctamente.")
            mostrar_libros()
            limpiar_campos()
        else:
            messagebox.showerror("Error", "Por favor completa todos los campos.")


# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Biblioteca")
root.geometry("600x400")

# Crear la tabla libros si no existe
crear_tabla()

# Crear la tabla de visualización
tree = ttk.Treeview(root, columns=("ID", "Título", "Autor", "Año"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Título", text="Título")
tree.heading("Autor", text="Autor")
tree.heading("Año", text="Año")
tree.pack(padx=10, pady=10)

# Obtener libros y mostrarlos en la tabla
mostrar_libros()

# Crear etiquetas y campos de entrada
label_titulo = tk.Label(root, text="Título:")
label_titulo.pack()
entry_titulo = tk.Entry(root)
entry_titulo.pack()

label_autor = tk.Label(root, text="Autor:")
label_autor.pack()
entry_autor = tk.Entry(root)
entry_autor.pack()

label_anio = tk.Label(root, text="Año:")
label_anio.pack()
entry_anio = tk.Entry(root)
entry_anio.pack()

# Botones para agregar, modificar y eliminar libros
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Libro", command=agregar_libro)
btn_agregar.grid(row=0, column=0, padx=5)

btn_modificar = tk.Button(
    frame_botones, text="Modificar Libro", command=modificar_libro
)
btn_modificar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Libro", command=eliminar_libro)
btn_eliminar.grid(row=0, column=2, padx=5)

# Iniciar el bucle de eventos
root.mainloop()
