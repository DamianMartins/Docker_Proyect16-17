# Sincronizar hora del sistema
# Instalar ntp
sudo apt install -y ntp
sudo systemctl start ntp
sudo systemctl enable ntp

# Instalar ntpdate
sudo apt install -y ntpdate

# Activar la sincronización
sudo ntpdate -s time.nist.gov

# Obtener la contraseña del archivo server_password.txt
#PASSWORD=$(cat server_password.txt)
PASSWORD='test'
# Establecimiento de la contraseña
echo "vagrant:$PASSWORD" | sudo chpasswd
echo "Script de aprovisionamiento ejecutado" >> /home/vagrant/provision.log

# Instalación de SSH Server
sudo apt install -y openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh

# Firewall
sudo ufw allow ssh

# Habilitar la autenticación por contraseña en SSH
sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config

# Reiniciar el servicio SSH
sudo systemctl restart ssh

# Instalar Docker
#curl -fsSL https://get.docker.com -o get-docker.sh
#sudo sh get-docker.sh

# Agregar el usuario "vagrant" al grupo "docker"
#sudo groupadd docker
#sudo usermod -aG docker vagrant

# Activar los cambios
#newgrp docker

#instalar python
sudo apt install python3
python3 --version

#Kubernetes Instalacion
#sudo curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
#sudo chmod +x ./kubectl
#sudo mv ./kubectl /usr/local/bin/kubectl

#minikube
#curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
#sudo dpkg -i minikube_latest_amd64.deb


# Descargar la última versión de Helm
#curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
# Dar permisos de ejecución al script
#chmod +x get_helm.sh
# Ejecutar el script para instalar Helm
#./get_helm.sh

#instalar Helm
#sudo snap install helm --classic

#instalar microk8s
#sudo snap install microk8s --classic

#Instalar Argocd
# Descargar el binario de ArgoCD
#wget https://github.com/argoproj/argo-cd/releases/download/v2.0.3/argocd-linux-amd64 -O argocd

# Dar permisos de ejecución al binario
#chmod +x argocd

# Mover el binario a un directorio en tu PATH
#sudo mv argocd /usr/local/bin/

# Verificar la instalación
#argocd version
