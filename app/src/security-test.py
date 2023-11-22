import subprocess
from bs4 import BeautifulSoup

# Ruta al archivo index.html
html_file_path = "/app/index.html"

# Leer el contenido del archivo HTML
with open(html_file_path, "r") as html_file:
    html_content = html_file.read()

# Utilizar BeautifulSoup para extraer el contenido del script JavaScript
soup = BeautifulSoup(html_content, "html.parser")
script_tags = soup.find_all("script")

# Verificar si se encontraron scripts en el HTML
if script_tags:
    script_content = "\n".join(tag.string for tag in script_tags if tag.string)

    # Verificar si script_content es una cadena antes de intentar escribirlo en el archivo temporal
    if script_content and isinstance(script_content, str):
        # Guardar el contenido del script en un archivo temporal
        temp_script_path = "/tmp/temp_script.js"
        with open(temp_script_path, "w") as temp_script:
            temp_script.write(script_content)

        try:
            # Ejecutar bandit en el archivo temporal
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
    else:
        print('El contenido del script no es una cadena')
else:
    print('No se encontró un script JavaScript en el archivo HTML')

