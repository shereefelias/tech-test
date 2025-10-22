
def find_greatest_product_of_contiguous_integers(grid: list[list[int]], contiguous_integers: int) -> int:
    rows, cols = len(grid), len(grid[0])
    max_product = 0 # default always to zero

    # Calculate possible combinations in each direction
    horizontal_combos = rows * (cols - contiguous_integers + 1)
    vertical_combos = cols * (rows - contiguous_integers + 1)
    diagonal_down_right = (rows - contiguous_integers + 1) * (cols - contiguous_integers + 1)
    diagonal_down_left = (rows - contiguous_integers + 1) * (cols - contiguous_integers + 1)
    total_combos = horizontal_combos + vertical_combos + diagonal_down_right + diagonal_down_left

    for i in range(rows):
        for j in range(cols):
            # Horizontal right
            if j + contiguous_integers <= cols:
                product = 1
                for k in range(contiguous_integers):
                    product *= grid[i][j + k]
                if product > max_product:
                    max_product = product

            # Vertical down
            if i + contiguous_integers <= rows:
                product = 1
                for k in range(contiguous_integers):
                    product *= grid[i + k][j]
                if product > max_product:
                    max_product = product

            # Diagonal right
            if i + contiguous_integers <= rows and j + contiguous_integers <= cols:
                product = 1
                for k in range(contiguous_integers):
                    product *= grid[i + k][j + k]
                if product > max_product:
                    max_product = product

            # Diagonal left
            if i + contiguous_integers <= rows and j - contiguous_integers >= -1:
                product = 1
                for k in range(contiguous_integers):
                    product *= grid[i + k][j - k]
                if product > max_product:
                    max_product = product

    # print summary
    print(f"Grid size: {rows}x{cols}, Contiguous = {contiguous_integers}")
    print(f"Total combinations:      {total_combos}")
    return max_product