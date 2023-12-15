import matplotlib.pyplot as plt

# Models and their corresponding performance metrics
models = ['CNN-LSTM', 'ARIMA', 'Linear Regression', 'Random Forest', 'kNN', 'SVR', 'ANN']
mape_values = [2.67, 8.63, 6.52, 2.48, 6.04, 3.77, 3.74]
mse_values = [1.1480, 9.5322, 6.5650, 1.0179, 5.0732, 2.6228, 2.4028]
rmse_values = [1.0714, 3.0874, 2.5622, 1.0089, 2.2524, 1.6195, 1.5501]
mae_values = [0.7537, 2.4199, 1.8776, 0.6967, 1.6737, 1.0465, 1.0586]

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Performance Comparison of Forecasting Models')

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
