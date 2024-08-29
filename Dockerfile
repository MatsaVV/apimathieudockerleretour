# Dockerfile for Streamlit App

# Utiliser l'image Python officielle comme base
FROM python:3.10.6-buster

# Copier les fichiers nécessaires dans le conteneur
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
COPY iris_regressor.pkl /app/iris_regressor.pkl

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer les dépendances à partir du fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel Streamlit sera accessible
EXPOSE 8501

# Commande pour exécuter l'application Streamlit, en utilisant le port spécifié ou 8501 par défaut
CMD ["streamlit", "run", "app.py", "--server.port=${PORT:-8501}", "--server.enableCORS=false"]
