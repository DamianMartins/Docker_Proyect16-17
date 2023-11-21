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
PASSWORD=$(cat server_password.txt)
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
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Agregar el usuario "vagrant" al grupo "docker"
sudo groupadd docker
sudo usermod -aG docker vagrant

# Activar los cambios
newgrp docker

