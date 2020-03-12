# Geschichtliches
Leitfrage: Welche Entwicklungen hat das Neuronale Netz von damals zu heute durchgemacht?

![roadmap](./img/roadmap.png)
[link](https://medium.com/analytics-vidhya/brief-history-of-neural-networks-44c2bf72eec)


## McCulloch-Pitts-Neuron
[towardsdatascience.com - link](https://towardsdatascience.com/mcculloch-pitts-model-5fdf65ac5dd1)
![Mcculloch-Pitts Neuron](./img/mpNeuron01.png)
* 1943 - Warren McCulloch (Neurowissenschaftler) & Walter Pitts
* Erstes Modell realer Vorgänge in neuronalen Strukturen
* Modell kann beliebig viele Inputwerte aufweisen
    * Werte sind boolescher Natur (nur wahr oder falsch / 1 vs. 0)
* Neuron besteht aus zwei Teilen
    * 1. Eingabewerte werden zusammengefasst / aufaddiert 
    * 2. Es wird geschaut ob das Ergebnis einen größeren Wert als Theta ausweist
        * Theta: 0 mit horizontalem Strich durch die Mitte
        * beliebige Zahl, siehe Beispiele

![mp Neuron - and](./img/mpNeuron_and.png)
![mp Neuron - nor](./img/mpNeuron_nor.png)
![mp Neuron - not](./img/mpNeuron_not.png)
![mp Neuron - or](./img/mpNeuron_or.png)
![mp Neuron - tautologie](./img/mpNeuron_tautologie.png)

* Nachteile des Modells
    * Nur boolesche Eingabewerte / Ausgabewert möglich
    * Schwelle (Theta) stets manuel bestimmen
        * Es gibt keine "fertigen" Operationen
    * Keine Gewichte für einzelne Eingabewerte
        * Alle Werte haben gleiche Priorität
    * Nicht möglich "gedeckelte" logische Funktionen abzubilden
        * Xor mit Obergrenze, max einer von beiden Inputs true

