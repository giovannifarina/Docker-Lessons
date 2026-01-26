# Utilizza l'immagine ufficiale di Python 3.11
FROM python:3.11-slim

# Crea un utente non-root per sicurezza
RUN useradd -m -s /bin/bash jupyteruser

# Imposta la directory di lavoro e ne cambia il proprietario
WORKDIR /app
RUN chown jupyteruser:jupyteruser /app

# Passa all'utente appena creato per le istruzioni successive
USER jupyteruser

# Installa Jupyter (verrà installato nella home dell'utente)
RUN pip install --no-cache-dir jupyter

# Aggiunge la directory dei binari dell'utente al PATH per trovare 'jupyter'
ENV PATH="/home/jupyteruser/.local/bin:${PATH}"

# Espone la porta ufficiale di Jupyter
EXPOSE 8888

# Comando per avviare Jupyter Notebook
# Nota: --allow-root non è più necessario né raccomandato qui
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser"]
