# Docker_Proyect16-17
Desafío Docker-Gitactions+Kubernetes
Creación de la Máquina Virtual:
Crea un archivo Vagrantfile en la raíz de tu repositorio.
Define la configuración de la máquina virtual, incluyendo la instalación de las herramientas necesarias (Docker, kubectl, etc.).
Utilizamos un script de aprovisionamiento para instalar las herramientas necesarias con un Bootstrap.sh y ejecutándolo en el Vagrantfile.
 Vagrantfile:
 
.sh:
 

Nota: Comandos útiles:
-Levantar la VM: $ vagrant up
-Destruir VM: $ vagrant destroy
Estos comandos son útiles para destruir y volver a levantar nuestra VM ante cambios que realicemos en el proceso de creación.
PassWord: se utilizó un archivo server_password.txt que contiene dicho pass, por medidas de seguridad el mismo fue agregado al .gitignore para evitar subir credenciales:
 
Accedemos a nuestra VM:
vagrant ssh -- -L 8080:localhost:8080
 
Parte 2: Docker
Dockerización de la Aplicación:
Agregamos las siguientes líneas de código para enviar nuestra app dentro de la VM:
 

Creamos los archivos Dockerfile y Docker Compose en la carpeta de tu aplicación:
 


Dockerfile:
FROM nginx:latest
COPY index.html /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/
COPY nginx.config /etc/nginx/nginx.conf
 
Yaml:
version: '3'
services:
  web:
    build:
      context: .
    ports:
      - "8080:80"
 
Colocamos los archivos en la carpeta “app”:
 

Construcción y Ejecución:
Ejecutar para construir y ejecutar la aplicación desde la VM:
$ docker-compose up
 
 
 
Nota: Recordar tener instalado en tu VM, Docker compose:
$ apt install docker-compose

Sin embargo, utilizaremos la imagen de nuestra app, que conservamos en “dockerhub”:

Primero bajamos lo que tengamos:

$ docker system prune -a


Luego descargamos nuestra imagen desde DockerHub:
$ docker run -d -p 8080:80 --name ws-app damiankaio/web:latest
 
 
 
Nota: Para el primer ingreso a la app, pedirá usuario y contraseña:
user: desafio14
pass: bootcamp
Esto es simplemente un detalle, por lo cual se generaron credenciales para este bootcamp.

Parte 3: Automatización de Dockerfile
Configuración del CI/CD:
Configura tu herramienta de CI/CD (GitHub Actions/Docker) con un archivo de configuración (.github/workflows/ci-cd.yml):
-Esto se realizará dentro de la VM:

Por lo tanto, dentro de la carpeta donde tenemos nuestra “App”:
iniciaremos Git y lo conectaremos a un repositorio (pasos en desafíos 14 y 15).
 
Dentro del Git de la VM, creamos el archivo con las verificaciones de seguridad, que utilizaremos más adelante:
 
 
 

Copiamos el siguiente código dentro del archivo (github/workflows/ci-cd.yml):
# .github/workflows/ci-cd.yml

name: CI/CD

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Build and Push Docker Image
        run: |
          docker build -t damiankaio/my-docker-image-d17 .
          docker login -u ${{ secrets.DOCKERHUB_USERNAME }} -p ${{ secrets.DOCKERHUB_TOKEN }}
          docker push damiankaio/my-docker-image-d17

Integración de Herramientas(Análisis de vulnerabilidades):
Estos pasos adicionales se han añadido antes del paso de construcción y carga de la imagen Docker. Así, antes de realizar la construcción, se ejecutará un linting para el Dockerfile usando hadolint, y se realizará un análisis de vulnerabilidades con trivy.
 
Luego guardamos los cambios:
 
Vamos a realizar un scrip para realizar un testo básico de vulnerabilidad, como nuestra app está diseñada con html, css y js, vamos a utilizar Python:
Descargar python:
https://www.python.org/downloads/release/python-3120/ 
o
Se puede utilizar una imagen de Python para la creación de la VM.



Agregamos el testo al  ci-cd.yml :
 

Nota: Esto invocara el scrip de Python que creamos con anterioridad.

Explicación del script
Este script de Python realiza verificaciones básicas de seguridad en los archivos de una aplicación web:
Archivo HTML:
Busca scripts maliciosos en el HTML mediante expresiones regulares.
Identifica referencias a recursos externos sospechosos (por ejemplo, enlaces a sitios externos).
Archivo CSS:
Examina el contenido del archivo CSS en busca de patrones maliciosos, como la presencia de la función eval().
Archivo JS:
Analiza el código JavaScript en busca de vulnerabilidades conocidas, como la presencia de la función alert().
Archivo nginx.conf:
Verifica si la configuración del servidor en el archivo nginx.conf incluye la directiva server_tokens off;, desactivando la divulgación de versiones de software, una práctica de seguridad recomendada.

 
También podemos verificar que nuestra imagen de Docker fue subida a DockerHub:
 
Se reciben correctamente Notificaciones, ante cambios al email(Asociado al Git):
 

Parte 4: Kubernetes
Iniciamos instalando Kubernetes:
Nota: Este paso puede agregarse en el archivo “Bootstrap.sh”, y así aprovisionar nuestra VM desde un inicio. 
$ sudo curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
$ sudo chmod +x ./kubectl
$ sudo mv ./kubectl /usr/local/bin/kubectl
 

Instala Minikube:
$ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
$ sudo dpkg -i minikube_latest_amd64.deb

Después de la instalación, puedes iniciar Minikube con:
$ minikube start
 
NOTA: Para la utilización de “minukube” se recomienda una VM de 2Gb de ram mínimo, si no fue contemplado se puede realizar los siguientes pasos:
 1- $ vantant halt
 2 -Cambia el tamaño de la Ram desde VirtualBox.(2GB minimo)
1 - $ vagrant up --provision

Configura kubectl para apuntar a Minikube:
Después de iniciar Minikube, necesitas configurar kubectl para apuntar al clúster Minikube:
$ kubectl config use-context minikube

Verifica la configuración:
Puedes verificar que kubectl esté configurado correctamente ejecutando:
$ kubectl config view
 
Nota: Asegúrate de que la salida incluya el contexto de Minikube.

Aplica los recursos de Kubernetes:
$ kubectl apply -f kubernetes/deployment.yaml
$ kubectl apply -f kubernetes/service.yaml
 
Si los archivos están bien configurados y su contenido es correcto debes obtener la salida de la imagen.
Configurar Port Forwarding para Acceder a la Aplicación
$ kubectl port-forward svc/my-app-service 8080:80

 
Nota: Si necesitas actualizar la imagen de Docker, edita deployment.yaml y cambia la etiqueta de la imagen. Luego, aplicamos la actualización con el comando:
$ kubectl apply -f deployment.yaml
Kubernetes realizará una actualización sin interrupciones, creando nuevos pods antes de eliminar los antiguos.

