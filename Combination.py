import matplotlib.pyplot as plt

# Metrics for the Combination model
mape_combination = 2.32
mse_combination = 0.9002
rmse_combination = 0.9488
mae_combination = 0.6525

# Labels for the metrics
metrics = ['MAPE', 'MSE', 'RMSE', 'MAE']

# Values for the Combination model
combination_values = [mape_combination, mse_combination, rmse_combination, mae_combination]

# Plotting the metrics for the Combination model
plt.figure(figsize=(8, 5))
plt.bar(metrics, combination_values, color=['blue', 'orange', 'green', 'red'])
plt.title('Performance Metrics for Combination Model')
plt.xlabel('Metrics')
plt.ylabel('Values')
plt.show()
