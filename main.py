class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0  #Wartezeit des Prozesses
        self.turnaround_time = 0  #Umlaufzeit des Prozesses

def fcfs_scheduling(processes):
    current_time = 0  #Aktuelle Systemzeit
    total_waiting_time = 0  #Gesamtwartezeit aller Prozesse
    total_turnaround_time = 0  #Gesamtumlaufzeit aller Prozesse

    print("Reihenfolge der Prozessausführung:")
    for process in processes:
        #Wartezeit des aktuellen Prozesses berechnen
        process.waiting_time = max(current_time - process.arrival_time, 0)
        #Umlaufzeit des aktuellen Prozesses berechnen
        process.turnaround_time = process.waiting_time + process.burst_time

        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time

        #Ausgabe der Ausführungsreihenfolge des Prozesses
        print(f"Prozess {process.pid} wird von {current_time} bis {current_time + process.burst_time} ausgeführt")

        current_time += process.burst_time

    #Durchschnittliche Wartezeit berechnen
    durchschnittliche_wartezeit = total_waiting_time / len(processes)
    #Durchschnittliche Umlaufzeit berechnen
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
