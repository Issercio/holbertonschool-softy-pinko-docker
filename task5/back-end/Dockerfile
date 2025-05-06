# Utilisation de l'image de base d'Ubuntu
FROM ubuntu:latest

# Mise à jour et installation des dépendances nécessaires
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip python3-venv

# Créer un environnement virtuel Python
RUN python3 -m venv /venv

# S'assurer que l'environnement virtuel est activé avant d'installer les dépendances
RUN /venv/bin/pip install --upgrade pip
RUN /venv/bin/pip install flask flask-cors

# Configuration du dossier de travail
WORKDIR /app

# Copier le fichier api.py dans l'image Docker
COPY ./api.py /app/api.py

# Exposer le port 5252 pour permettre à l'extérieur d'accéder à l'API
EXPOSE 5252

# Commande pour exécuter l'application Flask
CMD ["/venv/bin/python", "api.py"]
