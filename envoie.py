import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# Définition des variables
frq_ech = 1/100000
frq = 1000

# Définition de la fonction pour générer une fréquence
def frequency(frq, debut=0, fin=10, precision=0.01):
    # Création du vecteur temps
    temps = np.arange(debut, fin, frq_ech)
    
    # Calcul de l'angle en radian
    omega = 2 * np.pi * frq
    
    # Création du signal sinusoïdal
    cosinus = np.sin(omega * temps)

    # Création de la figure et des axes pour l'affichage
    fig, ax = plt.subplots(figsize=(20, 6))

    # Affichage du signal sinusoïdal
    ax.plot(temps, cosinus)
    ax.set_xlim(0,precision)
    ax.set_xlabel('Temps (s)')
    plt.show()

    # Lecture du signal avec la carte son
    sd.play(cosinus, samplerate=100000)
    sd.wait()
    
    # Affichage de la fréquence envoyée et de l'amplitude émise
    print("La fréquence envoyée est :", frq)
    print("L'amplitude émise est : ", np.max(cosinus)*2)

# Appel de la fonction pour générer une fréquence
frequency(frq)
