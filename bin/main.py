import time, os
import tasks.task_1_main_code as solve_1
import tasks.task_2_alt_code as solve_2
import tasks.task_3_alt_code as solve_3

import ast

# Example usage
if __name__ == "__main__":
    contiguous_integers = 3

    # --- Load grid from file ---
    # Using up to 10000x1000 grid for reasonable execution time. I tried to go over but performance is not that great
    # testing was done using Apple Air M3 with 16GB RAM
    grid_file_path = os.path.join(os.path.dirname(__file__), 'data', 'grid_10x10.txt') ## put the file as text under /bin/data/grid_10x10.txt

    try:
        with open(grid_file_path, 'r') as f:
            content = f.read()
            grid = ast.literal_eval(content)

    except FileNotFoundError:
        print(f"Error: Grid file not found at {grid_file_path}")
        exit()
    except (ValueError, SyntaxError):
        print(f"Error: Could not parse grid from {grid_file_path}")
        exit()

    # --- Solution 1: task_1_main_code --- brute force, standard loops
    start_time = time.perf_counter()
    product = solve_1.find_greatest_product_of_contiguous_integers(grid, contiguous_integers)
    end_time = time.perf_counter()
    print(f"Solution 1 (task_1):")
    print(f"  Greatest product of {contiguous_integers} adjacent numbers in the same direction: {product}")
    print(f"  Execution time: {end_time - start_time:.6f} seconds")
    print("-" * 20)

    # --- Solution 2: task_2_alt_code --- numpy best peformance and accurate
    start_time = time.perf_counter()
    product = solve_2.find_greatest_product_of_contiguous_integers(grid, contiguous_integers)
    end_time = time.perf_counter()
    print(f"Solution 2 (task_2):")
    print(f"  Greatest product of {contiguous_integers} adjacent numbers in the same direction: {product}")
    print(f"  Execution time: {end_time - start_time:.6f} seconds")
    print("-" * 20)

    # --- Solution 3: task_3_alt_code --- different approach but may not be accurate find max number within each row and anchor it and use
    #that to do the calucations. so it may miss some combinations.
    start_time = time.perf_counter()
    product = solve_3.find_greatest_product_of_contiguous_integers(grid, contiguous_integers)
    end_time = time.perf_counter()
    print(f"Solution 3 (task_3):")
    print(f"  Greatest product of {contiguous_integers} adjacent numbers in the same direction: {product}")
    print(f"  Execution time: {end_time - start_time:.6f} seconds")
    print("-" * 20)
