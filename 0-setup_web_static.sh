#!/usr/bin/env bash
#Prepare your web servers

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School 
  </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

config_path=/etc/nginx/sites-available/default
if ! grep -q "location /hbnb_static/ {" "$config_path"; then
	sudo sed -i "s@^\tlocation / {@\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;}\n\n\tlocation / {@g" $config_path
fi

sudo service nginx restart
