import matplotlib.pyplot as plt

# Monthly MAPE data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
mape_values = [3.42, 2.34, 1.75, 3.01, 2.74, 2.04, 1.97, 2.59, 2.29, 2.42, 2.30, 5.15]

# Overall MAPE
overall_mape = 2.67

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(months, mape_values, marker='o', linestyle='-', color='b', label='Monthly MAPE')
plt.axhline(y=overall_mape, linestyle='--', color='r', label='Overall MAPE')

# Adding labels and title
plt.xlabel('Months')
plt.ylabel('MAPE (%)')
plt.title('Monthly MAPE (2019) and Overall MAPE')
plt.legend()

# Display the plot
plt.show()
