import matplotlib.pyplot as plt

# Data for prediction accuracy for each day
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mape_values = [2.65, 3.17, 2.93, 2.41, 2.74, 2.12, 2.69]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(days, mape_values, color='skyblue')
plt.xlabel('Day')
plt.ylabel('MAPE (%)')
plt.title('Prediction Accuracy for Each Day of the Week')

# Display the plot
plt.show()
