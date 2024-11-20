def fcfs_scheduling(processes):
    
    processes.sort(key=lambda x: x['arrival_time'])
    
    
    current_time = 0
    for process in processes:
        
        if current_time < process['arrival_time']:
            current_time = process['arrival_time']
        
        
        process['completion_time'] = current_time + process['burst_time']
        
        current_time = process['completion_time']
        
        process['turnaround_time'] = process['completion_time'] - process['arrival_time']
        
        process['waiting_time'] = process['turnaround_time'] - process['burst_time']
    
    return processes


def display_process_table(processes):
    print(f"{'PID':<10}{'Arrival':<10}{'Burst':<10}{'Completion':<15}{'Turnaround':<15}{'Waiting':<10}")
    for p in processes:
        print(f"{p['pid']:<10}{p['arrival_time']:<10}{p['burst_time']:<10}{p['completion_time']:<15}{p['turnaround_time']:<15}{p['waiting_time']:<10}")
        

if __name__ == "__main__":
    
    processes = [
        {'pid': 1, 'arrival_time': 0, 'burst_time': 6},
        {'pid': 2, 'arrival_time': 2, 'burst_time': 4},
        {'pid': 3, 'arrival_time': 4, 'burst_time': 2},
        {'pid': 4, 'arrival_time': 6, 'burst_time': 5}
    ]
    
    
    scheduled_processes = fcfs_scheduling(processes)
    
    
    display_process_table(scheduled_processes)