import math
import pytest

from bin.tasks import task_1_main_code as t2
from bin.tasks import task_2_alt_code as t3
from bin.tasks import task_3_alt_code as t4


def brute_force_max_product(grid, k):
    rows = len(grid)
    cols = len(grid[0])
    max_prod = 0
    # directions: right, down, diag_dr, diag_dl
    dirs = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for i in range(rows):
        for j in range(cols):
            for dx, dy in dirs:
                end_x = i + dx * (k - 1)
                end_y = j + dy * (k - 1)
                if not (0 <= end_x < rows and 0 <= end_y < cols):
                    continue
                prod = 1
                for s in range(k):
                    prod *= grid[i + dx * s][j + dy * s]
                if prod > max_prod:
                    max_prod = prod
    return max_prod


@pytest.mark.parametrize("grid,k", [
    (
        [
            [8, 2, 22, 97, 38, 15, 0, 40, 0, 75],
            [49, 49, 99, 40, 17, 81, 18, 57, 60, 87],
            [81, 49, 31, 73, 55, 79, 14, 29, 93, 71],
            [52, 70, 95, 23, 4, 60, 11, 42, 69, 24],
            [22, 31, 16, 71, 51, 67, 63, 89, 41, 92],
            [24, 47, 32, 60, 99, 3, 45, 2, 44, 75],
            [32, 98, 81, 28, 64, 23, 67, 10, 26, 38],
            [67, 26, 20, 68, 2, 62, 12, 20, 95, 63],
            [24, 55, 58, 5, 66, 73, 99, 26, 97, 17],
            [21, 36, 23, 9, 75, 0, 76, 44, 20, 45],
        ],
        3,
    ),
    (
        [[1,2,3,4],[5,6,7,8],[9,1,2,3]],
        3,
    ),
])
def test_all_solutions_match_bruteforce(grid, k):
    expected = brute_force_max_product(grid, k)

    # task_2 returns int
    res2 = t2.find_greatest_product_of_contiguous_integers(grid, k)
    assert isinstance(res2, int), "task_2 should return an int"
    assert res2 == expected

    # task_3 returns (prod, pos)
    res3 = t3.find_greatest_product_of_contiguous_integers(grid, k)
    assert isinstance(res3, tuple) and len(res3) >= 1
    assert res3[0] == expected

    # task_4 returns (prod, pos)
    res4 = t4.find_greatest_product_of_contiguous_integers(grid, k)
    assert isinstance(res4, tuple) and len(res4) >= 1
    assert res4[0] == expected


def test_consistency_between_solutions_small_random():
    import random
    random.seed(0)
    grid = [[random.randint(0, 20) for _ in range(7)] for _ in range(6)]
    k = 3
    expected = brute_force_max_product(grid, k)

    assert t2.find_greatest_product_of_contiguous_integers(grid, k) == expected
    assert t3.find_greatest_product_of_contiguous_integers(grid, k)[0] == expected
    assert t4.find_greatest_product_of_contiguous_integers(grid, k)[0] == expected

