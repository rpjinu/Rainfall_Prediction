# Rainfall_Prediction
"Interactive rainfall prediction app using a trained machine learning model, built with Streamlit for real-time weather parameter inputs and predictions."

# Rainfall Prediction Project 🌦️

This project is an interactive rainfall prediction application built with Python and Streamlit. It uses a machine learning model to predict the likelihood of rain based on various weather parameters.

## Features

*   **Interactive Interface:** Input key weather parameters such as pressure, humidity, cloud cover, and wind speed.
*   **Real-Time Predictions:** Receive instant results on the likelihood of rainfall.
*   **Machine Learning Model:** A trained model ensures accurate and reliable predictions.
*   **User-Friendly Design:** Built with Streamlit for a seamless and intuitive user experience.

## Dataset

The model was trained using a weather dataset containing the following features:

| Feature       | Description                                              |
|---------------|----------------------------------------------------------|
| pressure      | Atmospheric pressure in hPa                              |
| dewpoint      | Dew point temperature in °C                             |
| humidity      | Relative humidity in percentage                         |
| cloud         | Cloud cover in percentage                               |
| rainfall      | Indicator of rainfall (1 for rain, 0 for no rain)         |
| sunshine      | Sunshine duration in hours                                |
| winddirection | Wind direction in degrees                                 |
| windspeed     | Wind speed in km/h                                        |

The dataset contains 366 rows and 8 columns, offering diverse weather scenarios for robust model training.

## Model Creation Workflow

1.  **Data Preprocessing:** Loading, handling missing values, normalizing features, and encoding the target variable.
2.  **Exploratory Data Analysis (EDA):** Visualizing feature distributions and examining correlations.
3.  **Feature Selection:** Selecting relevant features based on their importance.
4.  **Model Training:** Training various models (Logistic Regression, Random Forest, Gradient Boosting) and evaluating their performance.
5.  **Model Evaluation:** Analyzing predictions, fine-tuning hyperparameters, and achieving a final model accuracy of **[Insert your accuracy here, e.g., 90%]**.
6.  **Model Deployment:** Saving the trained model for deployment.

## Technologies Used

*   Python
*   Pandas
*   Matplotlib & Seaborn
*   Scikit-learn
*   Streamlit
*   Pickle

## Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/your-username/rainfall-prediction.git](https://github.com/your-username/rainfall-prediction.git)
    cd rainfall-prediction
    ```

2.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Usage

1.  Open the app in your browser (usually http://localhost:8501).
2.  Input weather parameters.
3.  Click "Predict Rainfall."

## Example Prediction

**Input:**

*   Pressure: 1020.0 hPa
*   Dewpoint: 14.5 °C
*   Humidity: 85%
*   Cloud Cover: 80%
*   Sunshine: 2.5 hours
*   Wind Direction: 70°
*   Wind Speed: 12.3 km/h

**Output:** Rainfall is likely

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
