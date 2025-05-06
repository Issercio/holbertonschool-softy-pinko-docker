FROM nginx:latest

# Copy front-end files to nginx's serving directory
COPY softy-pinko-front-end/ /var/www/html/softy-pinko-front-end/

# Copy Nginx configuration
COPY softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf