# Jupyter Notebook Server Dockerized

Questo progetto configura un server Jupyter Notebook in esecuzione all'interno di un container Docker, utilizzando un utente non-root per una maggiore sicurezza.

## Building the Image

Per creare l'immagine Docker, esegui il seguente comando dalla cartella `2_JupiterServer`:

```bash
docker build -t jupyter-server .
```

## Running the Container

Per avviare il server e mappare la directory corrente (così i tuoi notebook verranno salvati sul tuo Mac), usa:

```bash
docker run -p 8888:8888 -v $(pwd):/app jupyter-server
```

### Accesso al Server

Una volta avviato, vedrai un output nel terminale simile a questo:

```text
[I 15:00:00.000 NotebookApp] http://127.0.0.1:8888/?token=abcdef123456...
```

Copia l'URL con il **token** e incollalo nel tuo browser per accedere all'interfaccia di Jupyter.

## Note sulla sicurezza
Il server gira come utente `jupyteruser` (non-root). Tutti i file creati nella cartella `/app` all'interno del container verranno sincronizzati con la cartella locale grazie al volume (`-v`).
