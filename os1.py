def fcfs_scheduler():
    num_processes = int(input("Enter the number of processes: "))
    
    arrival_time = []
    burst_time = []
    
    for i in range(num_processes):
        arrival = int(input(f"Enter arrival time for process {i+1}: "))
        arrival_time.append(arrival)
        
        burst = int(input(f"Enter burst time for process {i+1}: "))
        burst_time.append(burst)
    
    completion_time = [0] * num_processes
    waiting_time = [0] * num_processes
    turnaround_time = [0] * num_processes
    
    completion_time[0] = burst_time[0]
    
    for i in range(1, num_processes):
        completion_time[i] = completion_time[i-1] + burst_time[i]
    
    for i in range(num_processes):
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]
    
    average_waiting_time = sum(waiting_time) / num_processes
    average_turnaround_time = sum(turnaround_time) / num_processes
    
    print("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    
    for i in range(num_processes):
        print(f"{i+1}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")


def sjf_scheduler():
    num_processes = int(input("Enter the number of processes: "))
    
    arrival_time = []
    burst_time = []
    
    for i in range(num_processes):
        arrival = int(input(f"Enter arrival time for process {i+1}: "))
        arrival_time.append(arrival)
        
        burst = int(input(f"Enter burst time for process {i+1}: "))
        burst_time.append(burst)
    
    completion_time = [0] * num_processes
    waiting_time = [0] * num_processes
    turnaround_time = [0] * num_processes
    processed = [False] * num_processes
    
    total_time = 0
    remaining_processes = num_processes
    
    while remaining_processes > 0:
        shortest_burst = float('inf')
        shortest_process = -1
        
        for i in range(num_processes):
            if arrival_time[i] <= total_time and not processed[i] and burst_time[i] < shortest_burst:
                shortest_burst = burst_time[i]
                shortest_process = i
        
        if shortest_process == -1:
            total_time += 1
        else:
            completion_time[shortest_process] = total_time + burst_time[shortest_process]
            waiting_time[shortest_process] = total_time - arrival_time[shortest_process]
            turnaround_time[shortest_process] = completion_time[shortest_process] - arrival_time[shortest_process]
            
            total_time = completion_time[shortest_process]
            processed[shortest_process] = True
            remaining_processes -= 1
    
    average_waiting_time = sum(waiting_time) / num_processes
    average_turnaround_time = sum(turnaround_time) / num_processes
    
    print("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    
    for i in range(num_processes):
        print(f"{i+1}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")


def srtf_scheduler():
    num_processes = int(input("Enter the number of processes: "))

    arrival_time = []
    burst_time = []
    remaining_time = []

    for i in range(num_processes):
        arrival = int(input(f"Enter arrival time for process {i+1}: "))
        arrival_time.append(arrival)

        burst = int(input(f"Enter burst time for process {i+1}: "))
        burst_time.append(burst)
        remaining_time.append(burst)

    completion_time = [0] * num_processes
    waiting_time = [0] * num_processes
    turnaround_time = [0] * num_processes

    total_time = 0
    completed_processes = 0

    while completed_processes != num_processes:
        shortest_burst = float('inf')
        shortest_process = -1

        for i in range(num_processes):
            if arrival_time[i] <= total_time and remaining_time[i] < shortest_burst and remaining_time[i] > 0:
                shortest_burst = remaining_time[i]
                shortest_process = i

        if shortest_process == -1:
            total_time += 1
        else:
            remaining_time[shortest_process] -= 1

            if remaining_time[shortest_process] == 0:
                completed_processes += 1
                completion_time[shortest_process] = total_time + 1
                waiting_time[shortest_process] = completion_time[shortest_process] - arrival_time[shortest_process] - burst_time[shortest_process]
                turnaround_time[shortest_process] = completion_time[shortest_process] - arrival_time[shortest_process]

        total_time += 1

    average_waiting_time = sum(waiting_time) / num_processes
    average_turnaround_time = sum(turnaround_time) / num_processes

    print("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")

    for i in range(num_processes):
        print(f"{i+1}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")


def round_robin_scheduler():
    num_processes = int(input("Enter the number of processes: "))
    time_quantum = int(input("Enter the time quantum: "))

    arrival_time = []
    burst_time = []
    remaining_time = []

    for i in range(num_processes):
        arrival = int(input(f"Enter arrival time for process {i+1}: "))
        arrival_time.append(arrival)

        burst = int(input(f"Enter burst time for process {i+1}: "))
        burst_time.append(burst)
        remaining_time.append(burst)

    completion_time = [0] * num_processes
    waiting_time = [0] * num_processes
    turnaround_time = [0] * num_processes

    total_time = 0
    completed_processes = 0

    while completed_processes != num_processes:
        for i in range(num_processes):
            if remaining_time[i] > 0:
                if remaining_time[i] <= time_quantum:
                    total_time += remaining_time[i]
                    completion_time[i] = total_time
                    remaining_time[i] = 0
                    completed_processes += 1
                else:
                    total_time += time_quantum
                    remaining_time[i] -= time_quantum

        for i in range(num_processes):
            if remaining_time[i] > 0:
                waiting_time[i] = total_time - arrival_time[i]

    for i in range(num_processes):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    average_waiting_time = sum(waiting_time) / num_processes
    average_turnaround_time = sum(turnaround_time) / num_processes

    print("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")

    for i in range(num_processes):
        print(f"{i+1}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")


def priority_queue_scheduler():
    num_processes = int(input("Enter the number of processes: "))

    arrival_time = []
    burst_time = []
    priority = []

    for i in range(num_processes):
        arrival = int(input(f"Enter arrival time for process {i+1}: "))
        arrival_time.append(arrival)

        burst = int(input(f"Enter burst time for process {i+1}: "))
        burst_time.append(burst)

        prio = int(input(f"Enter priority level for process {i+1}: "))
        priority.append(prio)

    completion_time = [0] * num_processes
    waiting_time = [0] * num_processes
    turnaround_time = [0] * num_processes

    processed = [False] * num_processes
    remaining_processes = num_processes
    total_time = 0

    while remaining_processes > 0:
        highest_priority = min(priority)
        shortest_burst = float('inf')
        process_index = -1

        for i in range(num_processes):
            if priority[i] == highest_priority and arrival_time[i] <= total_time and not processed[i]:
                if burst_time[i] < shortest_burst:
                    shortest_burst = burst_time[i]
                    process_index = i

        if process_index != -1:
            completion_time[process_index] = total_time + burst_time[process_index]
            waiting_time[process_index] = total_time - arrival_time[process_index]
            turnaround_time[process_index] = completion_time[process_index] - arrival_time[process_index]

            total_time = completion_time[process_index]
            processed[process_index] = True
            remaining_processes -= 1
        else:
            total_time += 1

    average_waiting_time = sum(waiting_time) / num_processes
    average_turnaround_time = sum(turnaround_time) / num_processes

    print("\nProcess\tArrival Time\tBurst Time\tPriority\tCompletion Time\tWaiting Time\tTurnaround Time")

    for i in range(num_processes):
        print(f"{i+1}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{priority[i]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")


n=1
while n:
    print("Please choose from the following scheduling algorithms:")
    print("1. First come first serve")
    print("2. Shortest job first")
    print("3. Shortest remaining time first")
    print("4. Round Robin")
    print("5. Priority queue")
    n=int(input('Enter your choice: '))
    if n==1:
        fcfs_scheduler()
    elif n==2:
        sjf_scheduler()
    elif n==3:
        srtf_scheduler()
    elif n==4:
        round_robin_scheduler()
    elif n==5:
        priority_queue_scheduler()
    else:
        print('you entered wrong choice')
    n=int(input("enter any value to run again otherwise enter 0 to exit"))