import re

# Archivo HTML
html_file_path = "./index.html"
with open(html_file_path, "r") as html_file:
    html_content = html_file.read()

# Buscar scripts maliciosos en el archivo HTML
script_tags = re.findall(r'<script[\s\S]*?>[\s\S]*?</script>', html_content)
if script_tags:
    print("Se encontraron scripts maliciosos en el archivo HTML:")
    for script_tag in script_tags:
        print(f"- {script_tag}")

# Buscar referencias a recursos externos sospechosos en el archivo HTML
external_resources = re.findall(r'src=[\'"]?([^\'" >]+)', html_content)
if external_resources:
    print("\nReferencias a recursos externos sospechosos en el archivo HTML:")
    for resource in external_resources:
        print(f"- {resource}")

# Archivo CSS
css_file_path = "./style.css"
with open(css_file_path, "r") as css_file:
    css_content = css_file.read()

# Buscar patrones maliciosos en el archivo CSS
# (Este es un ejemplo básico y puede necesitar ajustes según tus necesidades)
if "eval(" in css_content:
    print("\nSe encontró el patrón 'eval(' en el archivo CSS. Esto podría ser una vulnerabilidad.")

# Archivo JS
js_file_path = "./script.js"
with open(js_file_path, "r") as js_file:
    js_content = js_file.read()

# Revisar el código JavaScript en busca de vulnerabilidades conocidas
# (Este es un ejemplo básico y puede necesitar ajustes según tus necesidades)
if "alert(" in js_content:
    print("\nSe encontró el patrón 'alert(' en el archivo JavaScript. Esto podría ser una vulnerabilidad.")

# Archivo nginx.conf
nginx_conf_path = "./nginx.conf"
with open(nginx_conf_path, "r") as nginx_conf_file:
    nginx_conf_content = nginx_conf_file.read()

# Verificar la configuración del servidor en el archivo nginx.conf
# (Este es un ejemplo básico y puede necesitar ajustes según tus necesidades)
if "server_tokens off;" not in nginx_conf_content:
    print("\nLa configuración 'server_tokens off;' no está presente en nginx.conf. Se recomienda desactivar la divulgación de versiones de software.")

# Este scrip se realizo de forma basica para cumplir el desafio 16 y 17, hay que tener en cuenta que existen muchisimas validaciones que pueden agregarse.