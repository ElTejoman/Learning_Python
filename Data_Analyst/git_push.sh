#!/bin/bash

# Añadir todos los archivos al staging area
git add .

# Hacer commit con un mensaje proporcionado como argumento
git commit -m "$1"

# Hacer push al repositorio remoto
git push
