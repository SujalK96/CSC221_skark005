from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create two D8 dice.
die_1 = Die(num_sides=8)
die_2 = Die(num_sides=8)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results using Plotly.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
layout = Layout(title='Results of rolling two D8 dice 1000 times',
                xaxis=dict(title='Result', dtick=1),  # Adjusting x-axis configuration
                yaxis=dict(title='Frequency of Result'))
fig = dict(data=data, layout=layout)
offline.plot(fig, filename='two_d8_visual.html')
