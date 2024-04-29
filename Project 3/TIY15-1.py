import matplotlib.pyplot as plt
# Setting the style to grayscale
plt.style.use('grayscale')
# list of first five cubic numbers
numbers_5 = list(range(1, 6))
cubes_5 = [num ** 3 for num in numbers_5]
# listing  5000 cubic numbers
numbers_5000 = list(range(1, 5001))
cubes_5000 = [num ** 3 for num in numbers_5000]
fig, ax = plt.subplots()
ax.plot(numbers_5, cubes_5, label='First Five Cubic Numbers', marker='o')
ax.plot(numbers_5000, cubes_5000, label='First 5000 Cubic Numbers')
ax.set_xlabel('Number')
ax.set_ylabel('Cube')
ax.set_title('Cubic Numbers')
# Adding legend so that we know which line is which
ax.legend()
plt.show()
