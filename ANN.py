import matplotlib.pyplot as plt

# Metrics for the ANN model
mape_ann = 3.74
mse_ann = 2.4028
rmse_ann = 1.5501
mae_ann = 1.0586

# Labels for the metrics
metrics = ['MAPE', 'MSE', 'RMSE', 'MAE']

# Values for the ANN model
ann_values = [mape_ann, mse_ann, rmse_ann, mae_ann]

# Plotting the metrics for the ANN model
plt.figure(figsize=(8, 5))
plt.bar(metrics, ann_values, color=['blue', 'orange', 'green', 'red'])
plt.title('Performance Metrics for ANN Model')
plt.xlabel('Metrics')
plt.ylabel('Values')
plt.show()
