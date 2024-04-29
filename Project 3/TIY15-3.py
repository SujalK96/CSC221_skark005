import matplotlib.pyplot as plt
from random_walk import RandomWalk
# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(5000)  # Using 5k instead of 50k points
    rw.fill_walk()
    plt.style.use('classic')
    
    # Setting the size for plot window
    plt.figure(dpi=128, figsize=(10, 6))
    
    # Plotting the path with plt.plot()
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)
        
    # Remove the axes.
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
