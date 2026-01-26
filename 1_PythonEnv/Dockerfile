# Utilizza l'immagine ufficiale di Python 3.11
FROM python:3.11-slim

# Directory di lavoro
WORKDIR /app

# Copia e installa requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice
COPY app.py .

# Comando di avvio
CMD ["python", "app.py"]
