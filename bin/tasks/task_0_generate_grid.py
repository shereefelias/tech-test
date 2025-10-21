import os
import random
import json
from typing import List, Literal

def generate_random_grid(
        rows: int,
        cols: int,
        max_value: int,
        output_format: Literal["list", "json"] = "list"
) -> List[List[int]]:
    """
    Generate and save a random grid (list of lists or JSON format) to /bin/data/.

    Args:
        rows (int): Number of rows.
        cols (int): Number of columns.
        max_value (int): Max integer value in grid.
        output_format (str): "list" for Python list format, "json" for JSON format.

    Returns:
        List[List[int]]: The generated grid.
    """
    # Generate the random grid
    grid = [[random.randint(0, max_value) for _ in range(cols)] for _ in range(rows)]

    # --- Ensure output folder exists ---
    # Use the script's location to build a reliable path to /bin/data
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, '..', 'data'))
    os.makedirs(base_dir, exist_ok=True)

    # --- Build file name ---
    file_ext = "json" if output_format == "json" else "txt"
    file_name = f"grid_{rows}x{cols}.{file_ext}"
    file_path = os.path.join(base_dir, file_name)

    # --- Write grid to file ---
    if output_format == "json":
        with open(file_path, "w") as f:
            json.dump({"grid": grid}, f, indent=4)
    else:
        with open(file_path, "w") as f:
            f.write("grid = [\n")
            for row in grid:
                f.write(f"    {row},\n")
            f.write("]\n")

    # --- Console summary ---
    print(f"\nGenerated Grid ({rows}x{cols}, max={max_value})")
    print(f"Output format: {output_format}")
    print(f"File saved to: {file_path}\n")

    return grid


# Example usage
if __name__ == "__main__":
    # Example 1: Large 1000x1000 grid saved to /bin/data/grid_1000x1000.txt
    generate_random_grid(10000, 1000, 100, output_format="list")
