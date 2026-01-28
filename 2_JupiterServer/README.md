# Jupyter Notebook Server Dockerized

Questo progetto configura un server Jupyter Notebook in esecuzione all'interno di un container Docker, utilizzando un utente non-root per una maggiore sicurezza.

## Building the Image

Per creare l'immagine Docker, esegui il seguente comando dalla cartella `2_JupiterServer`:

```bash
docker build -t jupyter-server .
```

## Running the Container

Per creare il container, avviare il server, e mappare la directory corrente (così i tuoi notebook verranno salvati sul tuo Mac), usa:

```bash
docker run --name jupiter-server -p 8888:8888 -v $(pwd)/shared:/app jupyter-server
```

Se preferisci avviarlo in **modalità detached** (in background), aggiungi il parametro `-d`:

```bash
docker run -d --name jupiter-server -p 8888:8888 -v $(pwd)/shared:/app jupyter-server
```

Per vedere l'output del log quando è in background, puoi usare:

```bash
docker logs -f jupiter-server
```

## Restarting, Stopping and Removing the Container

Se il container esiste già ma è fermo, puoi semplicemente farlo ripartire con:

```bash
docker start jupiter-server
```

Per fermare il container in esecuzione:

```bash
docker stop jupiter-server
```

Per rimuovere il container (necessario se vuoi riavviarlo con lo stesso nome):

```bash
docker rm jupiter-server
```

### Accesso al Server
 
 Una volta avviato, il server sarà accessibile direttamente al seguente indirizzo:
 
 http://127.0.0.1:8888
 
 Non è richiesto alcun token di accesso.

## Note sulla sicurezza
Il server gira come utente `jupyteruser` (non-root). Tutti i file creati nella cartella `/app` all'interno del container verranno sincronizzati con la cartella locale `shared` grazie al volume (`-v`).
