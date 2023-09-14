import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def normalDistribution(positions, height):
    xmin, xmax = min(positions), max(positions)
    mean = (xmin + xmax) / 2
    std_dev = np.std(positions)
    x_range = np.linspace(xmin, xmax, 1000)

    curve = stats.norm.pdf(x_range, mean, std_dev)  

    current_max_height = np.max(curve)
    scaling_factor = height / current_max_height
    scaled_bell_curve = curve * scaling_factor

    plt.axvline(x=mean, color='red', linestyle='--', linewidth=2)
    plt.plot(x_range, scaled_bell_curve)

def simulateGaltonBoard(rows, beads):
    positions = np.zeros(beads)

    for i in range(rows):
        directions = np.random.randint(0, 2, beads) + 1
        positions += directions

    return positions


if __name__ == "__main__":
    rows = 1000
    beads = 100000
    positions = simulateGaltonBoard(rows, beads)

    hist, bin_edges, _ = plt.hist(positions, bins=np.arange(min(positions), max(positions) + 2, 1), density=True, align='left', rwidth=0.8)

    max_count_bin = np.argmax(hist)
    max_count = hist[max_count_bin]

    normalDistribution(positions, max_count)
    plt.show()
