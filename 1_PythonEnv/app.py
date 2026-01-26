import numpy as np

def calcola_medie():
    """
    Calcola medie usando NumPy con dati embedded
    """
    print("=" * 50)
    print("CALCOLO MEDIE CON NUMPY")
    print("=" * 50)
    
    # Dati embedded - vendite giornaliere di 5 prodotti in una settimana
    vendite = np.array([
        [45, 52, 48, 61, 55, 49, 58],  # Laptop
        [78, 82, 75, 88, 91, 84, 79],  # Mouse
        [62, 58, 65, 70, 68, 63, 61],  # Tastiera
        [34, 38, 31, 42, 39, 35, 40],  # Monitor
        [91, 88, 95, 92, 89, 94, 90]   # Webcam
    ])
    
    prodotti = ['Laptop', 'Mouse', 'Tastiera', 'Monitor', 'Webcam']
    giorni = ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom']
    
    print("\nDati vendite settimanali:")
    print(f"\n{'Prodotto':<12} {' '.join(f'{g:>6}' for g in giorni)}")
    print("-" * 60)
    for i, prodotto in enumerate(prodotti):
        print(f"{prodotto:<12} {' '.join(f'{v:6d}' for v in vendite[i])}")
    
    # 1. Media totale di tutte le vendite
    media_totale = np.mean(vendite)
    print(f"\n1. Media totale vendite: {media_totale:.2f} unità")
    
    # 2. Media per prodotto (media su ogni riga)
    media_per_prodotto = np.mean(vendite, axis=1)
    print("\n2. Media vendite per prodotto:")
    for prodotto, media in zip(prodotti, media_per_prodotto):
        print(f"   {prodotto:<12}: {media:.2f} unità")
    
    # 3. Media per giorno (media su ogni colonna)
    media_per_giorno = np.mean(vendite, axis=0)
    print("\n3. Media vendite per giorno:")
    for giorno, media in zip(giorni, media_per_giorno):
        print(f"   {giorno}: {media:.2f} unità")
    
    # 4. Prodotto con vendite medie più alte
    idx_max = np.argmax(media_per_prodotto)
    print(f"\n4. Prodotto con media più alta: {prodotti[idx_max]} ({media_per_prodotto[idx_max]:.2f} unità)")
    
    # 5. Giorno con vendite medie più basse
    idx_min = np.argmin(media_per_giorno)
    print(f"\n5. Giorno con media più bassa: {giorni[idx_min]} ({media_per_giorno[idx_min]:.2f} unità)")
    
    # 6. Deviazione standard
    std_totale = np.std(vendite)
    print(f"\n6. Deviazione standard: {std_totale:.2f}")
    
    # 7. Mediana
    mediana = np.median(vendite)
    print(f"\n7. Mediana vendite: {mediana:.2f} unità")
    
    print("\n" + "=" * 50)
    print("ANALISI COMPLETATA")
    print("=" * 50)

if __name__ == "__main__":
    calcola_medie()
