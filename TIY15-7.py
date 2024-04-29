from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create three D6 dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results using Plotly.
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
layout = Layout(title='Results of rolling three D6 dice 1000 times',
                xaxis=dict(title='Result'),
                yaxis=dict(title='Frequency of Result'))
fig = dict(data=data, layout=layout)
offline.plot(fig, filename='three_d6_visual.html')
