sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/nginx.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test-wsgi
sudo /etc/init.d/gunicorn restart
