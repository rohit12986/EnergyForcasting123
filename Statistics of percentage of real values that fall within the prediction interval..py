import matplotlib.pyplot as plt

# Prediction Interval Zone and corresponding percentage of real values
intervals = ['± 20 %', '± 10 %', '± 5 %']
percentage_within_interval = [99.82, 97.51, 87.61]

# Plotting
plt.bar(intervals, percentage_within_interval, color='skyblue')
plt.xlabel('Prediction Interval Zone')
plt.ylabel('% Real Values within Prediction Interval')
plt.title('Real Values within Prediction Intervals')
plt.ylim(0, 100)  # Set y-axis limits to 0-100 for percentage

# Display percentage values on top of the bars
for i, value in enumerate(percentage_within_interval):
    plt.text(i, value + 1, f'{value:.2f}%', ha='center')

# Show the plot
plt.show()
