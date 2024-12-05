#!/usr/bin/python3
""" defining the island perimeter's  finding function """


def island_perimeter(grid):
    """ returning perimiter of island
    grid ids representing the water by 0 and land by 1
    args=
        grid (list)-> list of the list of integers which is representing island
    returns=
        perimeter of the island which is defined in grid
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edges += 1
    return size * 4 - edges * 2
