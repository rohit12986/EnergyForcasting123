import matplotlib.pyplot as plt

# Models and their corresponding performance metrics
models = ['CNN-LSTM', 'Random Forest', 'Combination']
mape_values = [2.67, 2.48, 2.32]
mse_values = [1.1480, 1.0179, 0.9002]
rmse_values = [1.0714, 1.0089, 0.9488]
mae_values = [0.7537, 0.6967, 0.6525]

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Performance of the combined Random Forest - CNN-LSTM model')

# Plot MAPE
axs[0, 0].bar(models, mape_values, color='skyblue')
axs[0, 0].set_title('MAPE')

# Plot MSE
axs[0, 1].bar(models, mse_values, color='lightcoral')
axs[0, 1].set_title('MSE')

# Plot RMSE
axs[1, 0].bar(models, rmse_values, color='lightgreen')
axs[1, 0].set_title('RMSE')

# Plot MAE
axs[1, 1].bar(models, mae_values, color='lightsalmon')
axs[1, 1].set_title('MAE')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Show the plot
plt.show()
