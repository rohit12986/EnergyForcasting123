import matplotlib.pyplot as plt

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# MAPE scores for each day
mape_scores = [2.65, 3.17, 2.93, 2.41, 2.74, 2.12, 2.69]
44
# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(days, mape_scores, color='blue')
plt.title('MAPE Scores for Each Day of the Week')
plt.xlabel('Day')
plt.ylabel('MAPE (%)')
plt.ylim(0, max(mape_scores) + 1)  # Adjust the y-axis limit if needed
plt.show()
