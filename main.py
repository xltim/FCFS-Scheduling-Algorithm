class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0


def fcfs_scheduling(processes):
    #Sort processes based on arrival time
    processes.sort(key=lambda x: x.arrival_time)

    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    print("Process Execution Order:")
    for process in processes:
        #Calculate waiting time for current process
        process.waiting_time = current_time - process.arrival_time if current_time > process.arrival_time else 0

        #Calculate turnaround time for current process
        process.turnaround_time = process.waiting_time + process.burst_time

        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time

        print(f"Process {process.pid} executes from {current_time} to {current_time + process.burst_time}")

        current_time += process.burst_time

    average_waiting_time = total_waiting_time / len(processes)
    average_turnaround_time = total_turnaround_time / len(processes)

    print("\nAverage Waiting Time:", average_waiting_time)
    print("Average Turnaround Time:", average_turnaround_time)


if __name__ == "__main__":
    #Example processes: [pid, arrival_time, burst_time]
    processes = [
        Process(1, 0, 10),
        Process(2, 6, 4),
        Process(3, 8, 2),
        Process(4, 9, 5)
    ]

    fcfs_scheduling(processes)
