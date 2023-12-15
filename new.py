#Random Forest - CNN/LSTM Merge
import matplotlib.pyplot as plt

# Metrics for each model
mape_rf = 2.476
mape_cnn_lstm = 2.673
mape_combination = 2.321

# Labels for the models
models = ['Random Forest', 'CNN-LSTM', 'Combination']

# Values for the performance metric (e.g., MAPE)
mape_values = [mape_rf, mape_cnn_lstm, mape_combination]

# Plotting the comparison graph
plt.figure(figsize=(8, 5))
plt.bar(models, mape_values, color=['blue', 'orange', 'green'])
plt.title('Performance Comparison of Models')
plt.xlabel('Models')
plt.ylabel('MAPE (%)')
plt.ylim(0, max(mape_values) + 1)  # Adjust the y-axis limit if needed
plt.show()
