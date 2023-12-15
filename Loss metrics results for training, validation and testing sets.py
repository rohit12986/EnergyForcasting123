import matplotlib.pyplot as plt

# Metrics data
metrics = {
    'MAPE': [1.69, 2.71, 2.67],
    'MSE': [0.4466, 1.3095, 1.1480],
    'RMSE': [0.6683, 1.1443, 1.0714],
    'MAE': [0.4787, 0.7836, 0.7537]
}

# Data for training, validation, and testing
labels = ['Training', 'Validation', 'Testing']

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Performance Metrics')

# Plot MAPE
axs[0, 0].bar(labels, metrics['MAPE'], color='blue')
axs[0, 0].set_title('MAPE')

# Plot MSE
axs[0, 1].bar(labels, metrics['MSE'], color='orange')
axs[0, 1].set_title('MSE')

# Plot RMSE
axs[1, 0].bar(labels, metrics['RMSE'], color='green')
axs[1, 0].set_title('RMSE')

# Plot MAE
axs[1, 1].bar(labels, metrics['MAE'], color='red')
axs[1, 1].set_title('MAE')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Show the plot
plt.show()
