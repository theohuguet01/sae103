import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

def enregistrer_signal(duration, frequence_ech):
    # Enregistre le signal avec la carte son
    enregistrement = sd.rec(int(duration * frequence_ech), samplerate=frequence_ech, channels=2, device=1)
    sd.wait()
    return enregistrement

def afficher_signal(enregistrement, periode_ech):
    # Crée un vecteur temps pour l'affichage
    t_enr = np.arange(0, len(enregistrement) * periode_ech, periode_ech)

    # Crée une figure et des axes pour l'affichage
    fig, ax = plt.subplots(figsize=(20, 6))

    # Affiche le signal enregistré
    ax.plot(t_enr, enregistrement[:, 1])
    ax.set_xlim(0, 0.1)
    ax.set_xlabel('Temps (s)')
    plt.show()

def calculer_frequence(enregistrement, duration):
    # Compte le nombre de passages à zéro pour déterminer la fréquence reçue
    count = 0
    for idex in range(len(enregistrement) - 1):
        if (enregistrement[idex][1] < 0) and (enregistrement[idex + 1][1] > 0):
            count += 1
    # Calcule et renvoie la fréquence reçue
    return count / duration

def calculer_amplitude(enregistrement, amplitude_function):
    # Calcule et renvoie l'amplitude du signal reçu
    return amplitude_function(enregistrement)

def calculer_rep_freq(amplitude_value, rep_freq_function):
    # Calcule et renvoie la réponse en fréquence
    return rep_freq_function(amplitude_value)

def main():
    duration = 5
    frequence_ech = 44100
    periode_ech = 1 / frequence_ech

    # Appelle les différentes fonctions
    enregistrement = enregistrer_signal(duration, frequence_ech)
    afficher_signal(enregistrement, periode_ech)

    frequence_recue = calculer_frequence(enregistrement, duration)
    print("La fréquence reçue est : ", frequence_recue)

    amplitude_value = calculer_amplitude(enregistrement, amplitude)
    print("L'amplitude du signal reçu est : ", amplitude_value)

    rep_freq_value = calculer_rep_freq(amplitude_value, rep_freq)
    print("La réponse en fréquence est : ", rep_freq_value)

if __name__ == "__main__":
    main()
