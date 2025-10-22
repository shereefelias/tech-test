

def find_greatest_product_of_contiguous_integers(grid: list[list[int]], contiguous_integers: int = 3) -> int:
    rows, cols = len(grid), len(grid[0])
    max_product = 0

    directions = {
        'right': (0, 1),
        'down': (1, 0),
        'diag_dr': (1, 1),
        'diag_dl': (1, -1)
    }

    k = contiguous_integers
    for i in range(rows):
        # Find max value and use it to calcualte all arund it
        max_val = max(grid[i])
        anchors = [j for j, val in enumerate(grid[i]) if val == max_val]
        for j in anchors:
            for name, (dx, dy) in directions.items():
                end_x = i + dx * (k - 1)
                end_y = j + dy * (k - 1)
                if not (0 <= end_x < rows and 0 <= end_y < cols):
                    continue
                prod = 1
                for s in range(k):
                    x = i + dx * s
                    y = j + dy * s
                    prod *= grid[x][y]
                if prod > max_product:
                    max_product = prod

    horizontal = rows * (cols - k + 1) if cols >= k else 0
    vertical = (rows - k + 1) * cols if rows >= k else 0
    diagonal = 2 * (rows - k + 1) * (cols - k + 1) if rows >= k and cols >= k else 0
    total_combos = horizontal + vertical + diagonal

    # print summary
    print(f"Grid size: {rows}x{cols}")
    print(f"Total combinations checked: {total_combos}")
    return max_product
