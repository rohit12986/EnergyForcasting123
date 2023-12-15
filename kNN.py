import matplotlib.pyplot as plt

# Metrics for the kNN model
mape_knn = 6.04
mse_knn = 5.0732
rmse_knn = 2.2524
mae_knn = 1.6737

# Labels for the metrics
metrics = ['MAPE', 'MSE', 'RMSE', 'MAE']

# Values for the kNN model
knn_values = [mape_knn, mse_knn, rmse_knn, mae_knn]

# Plotting the metrics for the kNN model
plt.figure(figsize=(8, 5))
plt.bar(metrics, knn_values, color=['blue', 'orange', 'green', 'red'])
plt.title('Performance Metrics for kNN Model')
plt.xlabel('Metrics')
plt.ylabel('Values')
plt.show()
