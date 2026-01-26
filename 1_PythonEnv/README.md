docker build -t 1_pythonenv_img .
# -t tagga l'immagine
# . indica la directory corrente

docker run --rm --name 1_pythonenv 1_pythonenv_img
# --rm rimuove l'immagine quando si esce
# --name nome del container
