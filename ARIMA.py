import matplotlib.pyplot as plt

# Metrics for the ARIMA model
mape_arima = 8.63
mse_arima = 9.5322
rmse_arima = 3.0874
mae_arima = 2.4199

# Labels for the metrics
metrics = ['MAPE', 'MSE', 'RMSE', 'MAE']

# Values for the ARIMA model
arima_values = [mape_arima, mse_arima, rmse_arima, mae_arima]

# Plotting the metrics for the ARIMA model
plt.figure(figsize=(8, 5))
plt.bar(metrics, arima_values, color=['blue', 'orange', 'green', 'red'])
plt.title('Performance Metrics for ARIMA Model')
plt.xlabel('Metrics')
plt.ylabel('Values')
plt.show()
