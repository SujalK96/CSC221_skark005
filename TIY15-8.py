from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)
    
# Here, multiplying the results instead of adding
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]
    
# Visualize the results using Plotly.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
layout = Layout(title='Results of multiplying two D6 dice 1000 times',
                xaxis=dict(title='Result'),
                yaxis=dict(title='Frequency of Result'))
fig = dict(data=data, layout=layout)
offline.plot(fig, filename='Multiplication_visual.html')
