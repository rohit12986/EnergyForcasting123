### Description
This repository is part of my thesis on prediction of energy demand using LSTM based neural network models. The source code of this entire research project is available for public use under the **[MIT License](LICENSE.md)**. 

Included are python notebook files that account for every distinct stage of the implementation, including the **Visualization**, **Preprocessing** and **Feature Extraction**, **Experiments**, **Final Model** and **Results** phases.

### Results
The forecasting of the unseen testing data below shows the prediction performance of the proposed model in comparison to the actual load values (**MAPE 2.67%**).

### Notebooks
 **[Visualization](visualization.ipynb)**
The notebook reads the data (energy consumption, weather data) and illustrates the time series using various graphical representations.

**[Preprocessing & Feature Extraction](preprocessing.ipynb)**
Application of data cleaning, scaling, and augmentation to the original data. Feature extraction is performed here in order to create the input and output feature vectors, as well as splitting the data into training, validation, and testing sets. 

**[Experiments](experiments.ipynb)**
Multiple experiments are conducted including different configurations of neurons and layers, in order to converge to an efficient LSTM model architecture with low forecasting error.

**[Final Model & Results](results.ipynb)**
The training of the final model is performed and statistical results are calculated to evaluate the forecasting performance. Graphical figures are included containing the actual and forecasted load curves for visual comparison. 

**[Full Project](full_project.ipynb)**
The notebook represents all unique sections of the entire project in chronological order in terms of execution.

### Data
**[Consumption Data](data/consumption.csv)**
Contains the hourly electricity consumption data for Spain for the years 2015 - 2019. 

**[Weather Data](data/weather.csv)**
Contains hourly weather data of Spain for the years 1980 - 2019.

### Models
This is the directory where the files of the saved model weights will be stored for each trained artificial neural network, including the models from the experiments stage.

**[Model Weights](models/model_weights.h5)**
The saved weights of the final optimized CNN-LSTM load forecasting model.