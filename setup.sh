# Firewall
sudo systemctl enable firewalld && sudo systemctl start firewalld
sudo firewall-cmd --get-active-zones
'<?xml version="1.0" encoding="utf-8"?>
<service>
  <short>Terraria</short>
  <description>Open TCP port 7777 for incoming Terraria client connections.</description>
  <port protocol="tcp" port="7777"/>
</service>' > /etc/firewalld/services/terraria.xml
sudo firewall-cmd --zone=public --permanent --add-service=terraria
sudo firewall-cmd --reload
sudo firewall-cmd --zone=public --permanent --list-services

sudo apt install ufw
sudo ufw allow ssh
sudo ufw allow 7777/tcp
sudo ufw enable
sudo ufw delete 4

sudo iptables -A INPUT -p tcp --dport 7777 -j ACCEPT
sudo iptables -vL

# Screen
sudo apt install screen

# Terraria Server install
cd /opt && sudo curl -O http://terraria.org/server/terraria-server-1344.zip # CHANGE FOR JOURNEYS END WHEN IT RELEASES
sudo apt install unzip
sudo unzip terraria-server-1344.zip
sudo mv /opt/Dedicated\ Server/Linux /opt/terraria
sudo rm -rf Dedicated\ Server/
sudo chown -R root:root /opt/terraria
sudo chmod +x /opt/terraria/TerrariaServer.bin.x86_64
sudo useradd -r -m -d /srv/terraria terraria
'[Unit]
Description=server daemon for terraria

[Service]
Type=forking
User=terraria
KillMode=none
ExecStart=/usr/bin/screen -dmS terraria /bin/bash -c "/opt/terraria/TerrariaServer.bin.x86_64 -config /opt/terraria/serverconfig.txt"
ExecStop=/usr/local/bin/terrariad exit

[Install]
WantedBy=multi-user.target' > /etc/systemd/system/terraria.service