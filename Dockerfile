# Utilisez l'image officielle de Python comme image de base
FROM python:3.11-slim

# Définissez le répertoire de travail
WORKDIR /app

# Copiez les fichiers de dépendances vers le conteneur
COPY requirements.txt .

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Install the GNU OpenMP library
RUN apt-get update && apt-get install -y libgomp1

# Copiez le reste du code de l'application dans le conteneur
COPY . .

# Exposez le port sur lequel l'application va tourner
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
