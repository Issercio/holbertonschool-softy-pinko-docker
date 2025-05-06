FROM ubuntu:latest

# Mise à jour des paquets
RUN apt-get update && apt-get upgrade -y

# Installation de Python3 et pip3
RUN apt-get install -y python3 python3-pip

# Contourner l'erreur "This environment is externally managed"
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED || true

# Installer Flask via pip3
RUN pip3 install flask

# Définir le répertoire de travail
WORKDIR /app

# Copier le script Python
COPY ./api.py /app/api.py

# Commande pour lancer le serveur Flask
CMD ["python3", "api.py"]
