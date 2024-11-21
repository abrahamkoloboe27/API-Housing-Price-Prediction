# Stage 1: Build stage
FROM python:3.10-slim AS builder

# Variables d’environnement pour désactiver le cache et améliorer la performance
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -U jax && \
    pip install --no-cache-dir -r requirements.txt


# Install the GNU OpenMP library
RUN apt-get update && apt-get install -y libgomp1

# Copier le code de l’application
COPY app.py /app


# Stage 2: Runtime stage
FROM python:3.10-slim

# Variables d’environnement
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Répertoire de travail
WORKDIR /app

# Copier uniquement les fichiers nécessaires depuis le builder
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app


# Ajouter un utilisateur non-root et lui attribuer les permissions nécessaires
RUN adduser --disabled-password appuser && \
    chown -R appuser:appuser /app

# Changer d’utilisateur pour éviter d’exécuter en tant que root
USER appuser

# Exposer le port de l’application
EXPOSE 7860

# Healthcheck pour surveiller l’état de l’application
HEALTHCHECK CMD curl --fail http://localhost:7860/health || exit 1

# Commande pour lancer l’application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860", "--workers", "4"]
