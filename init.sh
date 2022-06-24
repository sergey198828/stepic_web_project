mkdir uploads
mkdir -p public/{css,img,js}

sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo rm /etc/gunicorn.d/wsgi.example
sudo rm /etc/gunicorn.d/django.example
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test.conf
sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
