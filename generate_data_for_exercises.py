"""
2026_04_24

Script to generate data to be used in the exercises for the
Programmazione avanzata ed intelligenza artificiale [146179]
class at the University of Trento.

The data is supposed to simulate the results of the 'TPA 2025 – Dissipation' exercise,
i.e. data of execution time measurement
"""

import pandas as pd
import numpy as np

DEFAULT_PARAMS = {
    "matrix_sizes": [64, 128, 256, 512],
    "thread_counts": [1, 2, 4, 8, 16],
    "schedulers": ['static', 'dynamic', 'guided'],
    "iterations": 50,
}

def generate_heat_data(filename="ex2_execution_logs.csv", simulation_params: dict = DEFAULT_PARAMS):
    # Parameters to simulate
    matrix_sizes = simulation_params['matrix_sizes']
    thread_counts = simulation_params['thread_counts']
    schedulers = simulation_params['schedulers']
    iterations = simulation_params['iterations']
    
    data = []
    run_id = 1

    for n in matrix_sizes:
        for threads in thread_counts:
            for sched in schedulers:
                # Base complexity is O(N^2) for heat dissipation
                base_time = (n**2) / 1000 
                
                # Simulate parallel efficiency (Amdahl's Law)
                # It's never 100% efficient; overhead increases with threads
                efficiency = 0.95 if threads == 1 else (0.85 / (1 + 0.05 * np.log2(threads)))
                
                for _ in range(iterations):
                    # Add random noise and "Cold Start" outliers for the first few runs
                    noise = np.random.normal(0, base_time * 0.01)
                    cold_start = base_time * 0.2 if _ < 2 else 0
                    
                    # Scheduling Penalty (The "Tax")
                    if sched == 'static':
                        sched_penalty = 1.0  # Fastest, no extra overhead
                    elif sched == 'guided':
                        sched_penalty = 1.1  # ~10% slower due to chunk management
                    else: # dynamic
                        sched_penalty = 1.25 # ~25% slower due to high synchronization overhead

                    exec_time = (base_time / (threads * efficiency))*sched_penalty + noise + cold_start

                    # add outliers
                    if(run_id % 1001 == 0):
                        exec_time *= 15
                    if(run_id % 1551 == 0):
                        exec_time = -0.0001
                    
                    data.append({
                        'run_id': run_id,
                        'matrix_size': n,
                        'num_threads': threads,
                        'scheduling_type': sched,
                        'execution_time': round(max(0.1, exec_time), 4)
                    })
                    run_id += 1

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Successfully generated {len(df)} rows in '{filename}'")

if __name__ == "__main__":
    # data for exercise 2
    generate_heat_data()
    
    # train data for exercise 3
    train_set_params = {
        "matrix_sizes": [64, 128, 256, 512],
        "thread_counts": [1, 2, 4, 8, 16, 32],
        "schedulers": ['static', 'dynamic', 'guided'],
        "iterations": 80,
    }
    generate_heat_data(filename="ex3_execution_logs_train.csv", simulation_params=train_set_params)

    # test data for exercise 3
    test_set_params = {
        "matrix_sizes": [100, 200, 300, 400],
        "thread_counts": [1, 2, 4, 8, 16, 32],
        "schedulers": ['static', 'dynamic', 'guided'],
        "iterations": 20,
    }
    generate_heat_data(filename="ex3_execution_logs_test.csv", simulation_params=test_set_params)

