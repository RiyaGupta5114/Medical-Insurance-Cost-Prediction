# Medical-Insurance-Cost-Prediction

This project predicts medical insurance charges using user inputs such as age, gender, BMI, smoking status, and region. It uses machine learning (Random Forest Regression) and is deployed via a Flask-based web interface for real-time predictions.

# Overview

The goal is to estimate an individual’s insurance cost based on health and demographic attributes. The project includes complete stages: data preprocessing, model training, evaluation, and deployment using Flask for user interaction.

# Features

- Predicts medical charges based on 6 key input features
- Trained using Random Forest Regression (R² ≈ 0.85)
- Web interface built with Flask and HTML
- Input data scaled using StandardScaler
- Evaluated using MAE, RMSE, and R² Score

# Model Evaluation

- MAE: ~2500
- RMSE: ~3700
- R² Score: ~0.85
  
Evaluation may vary depending on the data split and the random state.

# Tools & Technologies

- Python, NumPy, Pandas, Matplotlib
- Scikit-learn (RandomForestRegressor, StandardScaler)
- Flask (for backend deployment)
- HTML (for frontend input form)

# Future Enhancements

- Improve UI with Bootstrap or React
- Deploy the app on platforms like Heroku or Render
- Implement form validation and error handling
- Add login functionality and database integration
