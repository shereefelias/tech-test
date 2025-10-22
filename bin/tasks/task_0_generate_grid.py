import os
import random
import json

def generate_random_grid(
        rows: int,
        cols: int,
        max_value: int,
        output_format: ["list", "json"] = "list"
) -> list[list[int]]:

    grid = [[random.randint(0, max_value) for _ in range(cols)] for _ in range(rows)]

    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, '..', 'data'))
    os.makedirs(base_dir, exist_ok=True)

    file_ext = "json" if output_format == "json" else "txt"
    file_name = f"grid_{rows}x{cols}.{file_ext}"
    file_path = os.path.join(base_dir, file_name)

    if output_format == "json":
        with open(file_path, "w") as f:
            json.dump({"grid": grid}, f, indent=4)
    else:
        with open(file_path, "w") as f:
            f.write("[")
            for row in grid:
                f.write(f"    {row},\n")
            f.write("]")

    print(f"Generated Grid ({rows}x{cols}, max={max_value})")
    print(f"Output format: {output_format}")
    print(f"File saved to: {file_path}")

    return grid

generate_random_grid(3, 3, 100, output_format="list")
