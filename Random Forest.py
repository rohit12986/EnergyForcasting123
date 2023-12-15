import matplotlib.pyplot as plt

# Metrics for the Random Forest model
mape_rf = 2.48
mse_rf = 1.0179
rmse_rf = 1.0089
mae_rf = 0.6967

# Labels for the metrics
metrics = ['MAPE', 'MSE', 'RMSE', 'MAE']

# Values for the Random Forest model
rf_values = [mape_rf, mse_rf, rmse_rf, mae_rf]

# Plotting the metrics for the Random Forest model
plt.figure(figsize=(8, 5))
plt.bar(metrics, rf_values, color=['blue', 'orange', 'green', 'red'])
plt.title('Performance Metrics for Random Forest Model')
plt.xlabel('Metrics')
plt.ylabel('Values')
plt.show()
