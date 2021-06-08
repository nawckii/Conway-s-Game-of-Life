import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
values = [ON, OFF]


def random_grid(n):
    return np.random.choice(values, n * n, p=[0.2, 0.8]).reshape(n, n)


def update(frame_num, img, grid, size):
    new_grid = grid.copy()
    for i in range(size):
        for j in range(size):
            total = int((grid[i, (j - 1) % size] + grid[i, (j + 1) % size] +
                         grid[(i - 1) % size, j] + grid[(i + 1) % size, j] +
                         grid[(i - 1) % size, (j - 1) % size] + grid[(i - 1) % size, (j + 1) % size] +
                         grid[(i + 1) % size, (j - 1) % size] + grid[(i + 1) % size, (j + 1) % size]) / 255)

            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = OFF
            else:
                if total == 3:
                    new_grid[i, j] = ON

    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,


if __name__ == '__main__':
    grid_size = 100
    updateInterval = 50

    grid = random_grid(grid_size)

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')

    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, grid_size,),
                                  frames=10,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show()
