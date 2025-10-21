import numpy as np
from typing import Tuple, List

def find_greatest_product_of_contiguous_integers(grid: List[List[int]], contiguous_integers: int) -> int:
    g = np.array(grid, dtype=int)
    n, m = g.shape
    k = contiguous_integers
    max_product = 0 # default always to zero
    best_pos = None
    pivot_value = None

    #  Calculate possible combinations in each direction
    horizontal_combos = n * (m - k + 1)
    vertical_combos = m * (n - k + 1)
    diagonal_down_right = (n - k + 1) * (m - k + 1)
    diagonal_down_left = (n - k + 1) * (m - k + 1)
    total_combos = horizontal_combos + vertical_combos + diagonal_down_right + diagonal_down_left

    # Horizontal right
    for j in range(m - k + 1):
        prod = np.prod(g[:, j:j + k], axis=1)
        row_idx = int(np.argmax(prod))
        value = int(prod[row_idx])
        if value > max_product:
            max_product = value
            best_pos = (row_idx, j, 'right')
            pivot_value = int(g[row_idx, j])

    #  Vertical  down
    for i in range(n - k + 1):
        prod = np.prod(g[i:i + k, :], axis=0)
        col_idx = int(np.argmax(prod))
        value = int(prod[col_idx])
        if value > max_product:
            max_product = value
            best_pos = (i, col_idx, 'down')
            pivot_value = int(g[i, col_idx])

    # Diagonal right
    for i in range(n - k + 1):
        for j in range(m - k + 1):
            value = int(np.prod([g[i + d, j + d] for d in range(k)]))
            if value > max_product:
                max_product = value
                best_pos = (i, j, 'diag_dr')
                pivot_value = int(g[i, j])

    # Diagonal left
    for i in range(n - k + 1):
        for j in range(k - 1, m):
            value = int(np.prod([g[i + d, j - d] for d in range(k)]))
            if value > max_product:
                max_product = value
                best_pos = (i, j, 'diag_dl')
                pivot_value = int(g[i, j])

    # print summary
    print(f"Grid size: {n}x{m}, Contiguous = {k}")
    print(f"Total combinations:      {total_combos}")
    return max_product
