# Configure git
git config --global user.email "sergey198828@gmail.com"
git config --global user.name "Sergey Kiyan"

# Create nessesary folders for static
mkdir uploads
mkdir -p public/{css,img,js}

# Configure and run NGINX
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

# Run hello-world app as wsgi
gunicorn --bind='0.0.0.0:8080' hello:wsgi_application &

# Create Django project "ask" and application "qa" then start it
cd ask
gunicorn --bind='0.0.0.0:8000' ask.wsgi &

# Setup and run database
sudo /etc/init.d/mysql start
mysql -u root -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'P@ssw0rd';"
mysql -u root -e "CREATE DATABASE IF NOT EXISTS ask_qa;"
mysql -u root -e "GRANT ALL ON ask_qa.* TO 'django'@'localhost';"
python manage.py check
python manage.py makemigrations
python manage.py migrate