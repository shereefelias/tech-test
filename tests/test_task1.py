import os
import ast
from bin.tasks import task_0_generate_grid as gen


def test_generate_random_grid_writes_file_and_returns_shape(tmp_path):
    # Use small grid to keep test fast
    rows, cols, max_val = 5, 6, 10
    grid = gen.generate_random_grid(rows, cols, max_val, output_format="list")

    # Check returned shape
    assert len(grid) == rows
    assert all(len(r) == cols for r in grid)

    # Expected file path under bin/data
    script_dir = os.path.dirname(gen.__file__)
    data_dir = os.path.abspath(os.path.join(script_dir, '..', 'data'))
    file_path = os.path.join(data_dir, f"grid_{rows}x{cols}.txt")

    assert os.path.exists(file_path), f"Expected file at {file_path}"

    # Ensure file contains a Python list definition we can parse
    with open(file_path, 'r') as f:
        content = f.read()
    assert 'grid =' in content
    grid_str = content[content.find('['):]
    parsed = ast.literal_eval(grid_str)
    assert isinstance(parsed, list)
    assert len(parsed) == rows

    # Clean up the file created by the generator to avoid polluting repo
    try:
        os.remove(file_path)
    except OSError:
        pass

