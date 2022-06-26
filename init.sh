# Create nessesary folders for static
mkdir uploads
mkdir -p public/{css,img,js}

# Configure and run NGINX
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

# Run hello-world app as wsgi
gunicorn --bind='0.0.0.0:8080' hello:wsgi_application

# Create Django project "ask" and application "qa" then start it
django-admin startproject ask
cd ask
python manage.py startapp qa
gunicorn --bind='0.0.0.0:8000' ask.wsgi