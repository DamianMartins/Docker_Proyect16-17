import subprocess
from bs4 import BeautifulSoup

# Ruta al archivo index.html
html_file_path = "/usr/share/nginx/html/index.html"

# Leer el contenido del archivo HTML
with open(html_file_path, "r") as html_file:
    html_content = html_file.read()

# Utilizar BeautifulSoup para extraer el contenido del script JavaScript
soup = BeautifulSoup(html_content, "html.parser")
script_content = soup.find("script").string

# Guardar el contenido del script en un archivo temporal
temp_script_path = "/tmp/temp_script.js"
with open(temp_script_path, "w") as temp_script:
    temp_script.write(script_content)

# Ejecutar bandit en el archivo temporal
try:
    result = subprocess.run(["bandit", "-r", temp_script_path], check=True, capture_output=True, text=True)
    output = result.stdout

    # Verificar si se encontraron vulnerabilidades.
    if "No issues identified" not in output:
        print('Encontradas vulnerabilidades en el código JavaScript')

        # Imprimir la salida de bandit
        print(output)
    else:
        print('No se encontraron vulnerabilidades en el código JavaScript')
except subprocess.CalledProcessError as e:
    # Manejar errores de bandit
    print(f'Error al ejecutar bandit: {e.stderr}')
except Exception as e:
    # Manejar otros errores
    print(f'Error: {e}')

# Eliminar el archivo temporal
subprocess.run(["rm", temp_script_path])