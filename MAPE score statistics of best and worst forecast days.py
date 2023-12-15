import matplotlib.pyplot as plt
import pandas as pd

# Data for the lowest and highest MAPE values
data = {
    'Date': ['2019-09-25', '2019-12-25', '2019-06-14', '2019-08-03', '2019-12-24', '2019-09-23', '2019-05-01', '2019-07-21', '2019-01-01'],
    'MAPE': [0.51, 20.95, 0.55, 0.68, 19.60, 0.74, 0.75, 13.46, None]
}

# Create a DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])  # Convert Date to datetime format

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(df['Date'], df['MAPE'], color=['green' if x == df['MAPE'].min() else 'red' for x in df['MAPE']])
plt.xlabel('Date')
plt.ylabel('MAPE (%)')
plt.title('Dates with Lowest and Highest MAPE Values (2019)')
plt.xticks(rotation=45, ha='right')

# Display the plot
plt.show()
