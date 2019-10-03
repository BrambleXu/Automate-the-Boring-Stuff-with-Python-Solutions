grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def plot_grid(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    for col in range(num_cols):        
        for row in range(num_rows):
            print (grid[row][col], end='')
        print()

if __name__ == '__main__':
    plot_grid(grid)
