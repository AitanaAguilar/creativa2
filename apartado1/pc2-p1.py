import os
import subprocess
import shutil

# Función para verificar si una herramienta está instalada en el sistema
def is_tool(name):
    """Verificar si una herramienta está instalada."""
    from shutil import which
    return which(name) is not None

# Función para instalar pip utilizando los comandos de apt-get de Ubuntu
def install_pip():
    """Instalar pip si no está instalado."""
    subprocess.run(['sudo', 'apt-get', 'update'])  # Actualizar la lista de paquetes
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'python3-pip'])  # Instalar pip

# Función para clonar un repositorio de GitHub, si ya existe, se elimina y se vuelve a clonar
def clone_repo(url, directory):
    """Clonar un repositorio de Git. Si ya existe, eliminarlo y clonar de nuevo."""
    if os.path.isdir(directory):
        shutil.rmtree(directory)  # Eliminar el directorio si ya existe
    subprocess.run(['git', 'clone', url, directory])  # Clonar el repositorio en 'directory'

# Función para instalar las dependencias del proyecto desde un archivo requirements.txt
def install_requirements():
    """Instalar dependencias desde requirements.txt (usando Python 3.9)."""
    subprocess.run(['python3.9', '-m', 'pip', 'install', '-r', 'requirements.txt'])  # Instalar dependencias

# Función para modificar el archivo HTML e incluir el nombre del grupo
def modify_html_file(filename, team_id):
    """Modificar el archivo HTML para incluir el TEAM_ID."""
    with open(filename, 'r') as file:
        html_content = file.read()  # Leer el contenido del archivo

    # En el enunciado piden obtenerlo desde la variable de entorno TEAM_ID
    html_content = html_content.replace('Simple Bookstore App', f'g{team_id} - Simple Bookstore App')

    with open(filename, 'w') as file:
        file.write(html_content)  # Escribir el contenido modificado de nuevo en el archivo

# Función principal del script
def main():
    # Verificar e instalar pip si es necesario
    if not is_tool('pip3'):
        install_pip()  # Instalar pip si no está instalado

    # URL del repositorio y directorio local
    repo_url = 'https://github.com/CDPS-ETSIT/practica_creativa2.git'
    local_dir = 'practica_creativa2'

    # Clonar el repositorio
    clone_repo(repo_url, local_dir)

    # Cambiar al directorio del repositorio
    os.chdir(f'{local_dir}/bookinfo/src/productpage')  # Cambiar al directorio de trabajo

    # Instalar las dependencias
    install_requirements()

    # Modificar el archivo HTML
    team_id = os.getenv('TEAM_ID', 'desconocido')  # Obtener el id del grupo desde TEAM_ID
    modify_html_file('templates/productpage.html', team_id)  # Modificar el archivo HTML

    # Iniciar la aplicación en un puerto específico (distinto del 9090 por defecto)
    puerto = '9080'
    subprocess.run(['python3.9', 'productpage_monolith.py', puerto])  # Iniciar la aplicación

# Punto de entrada del script
if __name__ == '__main__':
    main()
