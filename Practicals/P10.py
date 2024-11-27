class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0


def shortest_job_remaining_first(processes):
    n = len(processes)
    processes.sort(key=lambda x: x.arrival_time)  # Sort by arrival time
    completed = 0
    current_time = 0
    min_remaining_process = None
    global process_index 
    total_waiting_time = 0
    total_turnaround_time = 0

    while completed < n:
        # Find the process with the shortest remaining time at the current time
        for i in range(n):
            if (processes[i].arrival_time <= current_time and
                    processes[i].remaining_time > 0 and
                    (min_remaining_process is None or processes[i].remaining_time < min_remaining_process.remaining_time)):
                min_remaining_process = processes[i]
                process_index = i

        if min_remaining_process is None:
            # No process is ready; increment time
            current_time += 1
            continue

        # Execute the process for 1 unit of time
        min_remaining_process.remaining_time -= 1
        current_time += 1

        # If the process is complete
        if min_remaining_process.remaining_time == 0:
            completed += 1
            min_remaining_process.completion_time = current_time
            min_remaining_process.turnaround_time = min_remaining_process.completion_time - min_remaining_process.arrival_time
            min_remaining_process.waiting_time = min_remaining_process.turnaround_time - min_remaining_process.burst_time

            total_waiting_time += min_remaining_process.waiting_time
            total_turnaround_time += min_remaining_process.turnaround_time

            # Reset min_remaining_process for next selection
            min_remaining_process = None

    
    print("Process Execution Details:")
    for p in processes:
        print(f"Process ID: {p.process_id}, Arrival Time: {p.arrival_time}, Burst Time: {p.burst_time}, "
              f"Completion Time: {p.completion_time}, Turnaround Time: {p.turnaround_time}, Waiting Time: {p.waiting_time}")

    
    print("\nAverage Waiting Time:", total_waiting_time / n)
    print("Average Turnaround Time:", total_turnaround_time / n)


def main():
    
    processes = [
        Process("P1", 0, 8),
        Process("P2", 1, 4),
        Process("P3", 2, 2),
        Process("P4", 3, 1),
        Process("P5", 4, 3),
        Process("P6", 5, 2),
    ]

    shortest_job_remaining_first(processes)


if __name__ == "__main__":
    main()
