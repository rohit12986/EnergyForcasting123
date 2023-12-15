import matplotlib.pyplot as plt

# Metrics for the SVR model
mape_svr = 3.77
mse_svr = 2.6228
rmse_svr = 1.6195
mae_svr = 1.0465

# Labels for the metrics
metrics = ['MAPE', 'MSE', 'RMSE', 'MAE']

# Values for the SVR model
svr_values = [mape_svr, mse_svr, rmse_svr, mae_svr]

# Plotting the metrics for the SVR model
plt.figure(figsize=(8, 5))
plt.bar(metrics, svr_values, color=['blue', 'orange', 'green', 'red'])
plt.title('Performance Metrics for SVR Model')
plt.xlabel('Metrics')
plt.ylabel('Values')
plt.show()
