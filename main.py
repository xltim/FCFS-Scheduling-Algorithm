class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid  #Die ID des Prozesses
        self.arrival_time = arrival_time  #Die Ankunftszeit des Prozesses
        self.burst_time = burst_time  #Die Ausführungszeit (Burst-Zeit) des Prozesses
        self.waiting_time = 0  #Die Wartezeit des Prozesses, standardmäßig auf 0 gesetzt
        self.turnaround_time = 0  #Die Umlaufzeit des Prozesses, standardmäßig auf 0 gesetzt

def fcfs_scheduling(processes):
    current_time = 0  #Die aktuelle Systemzeit, zu Beginn 0
    total_waiting_time = 0  #Die Gesamtwartezeit aller Prozesse, zu Beginn 0
    total_turnaround_time = 0  #Die Gesamtumlaufzeit aller Prozesse, zu Beginn 0

    print("Reihenfolge der Prozessausführung:")
    for process in processes:
        #Berechnung der Wartezeit des aktuellen Prozesses
        #Die Wartezeit ist entweder die Differenz zwischen der aktuellen Zeit und der Ankunftszeit des Prozesses
        #ODER 0, wenn die aktuelle Zeit kleiner oder gleich der Ankunftszeit ist
        process.waiting_time = max(current_time - process.arrival_time, 0)

        #Berechnung der Umlaufzeit des aktuellen Prozesses
        #Die Umlaufzeit ist die Summe aus Wartezeit und Burst-Zeit des Prozesses
        process.turnaround_time = process.waiting_time + process.burst_time

        #Aktualisierung der Gesamtwartezeit und Gesamtumlaufzeit
        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time

        #Ausgabe der Ausführungsreihenfolge des aktuellen Prozesses
        print(f"Prozess {process.pid} wird von {current_time} bis {current_time + process.burst_time} ausgeführt")

        #Aktualisierung der aktuellen Zeit durch Hinzufügen der Burst-Zeit des aktuellen Prozesses
        current_time += process.burst_time

    #Berechnung der durchschnittlichen Wartezeit und Umlaufzeit
    durchschnittliche_wartezeit = total_waiting_time / len(processes)
    durchschnittliche_umlaufzeit = total_turnaround_time / len(processes)

    #Ausgabe der durchschnittlichen Wartezeit und Umlaufzeit
    print("\nDurchschnittliche Wartezeit:", durchschnittliche_wartezeit)
    print("Durchschnittliche Umlaufzeit:", durchschnittliche_umlaufzeit)


if __name__ == "__main__":
    #Beispielprozesse erstellen
    processes = [
        Process(1, 0, 10),
        Process(2, 6, 4),
        Process(3, 8, 2),
        Process(4, 9, 5)
    ]

    #FCFS-Scheduling durchführen
    fcfs_scheduling(processes)
