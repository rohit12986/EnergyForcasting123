import matplotlib.pyplot as plt

# Metrics for the Linear Regression model
mape_lr = 6.52
mse_lr = 6.5650
rmse_lr = 2.5622
mae_lr = 1.8776

# Labels for the metrics
metrics = ['MAPE', 'MSE', 'RMSE', 'MAE']

# Values for the Linear Regression model
lr_values = [mape_lr, mse_lr, rmse_lr, mae_lr]

# Plotting the metrics for the Linear Regression model
plt.figure(figsize=(8, 5))
plt.bar(metrics, lr_values, color=['blue', 'orange', 'green', 'red'])
plt.title('Performance Metrics for Linear Regression Model')
plt.xlabel('Metrics')
plt.ylabel('Values')
plt.show()
