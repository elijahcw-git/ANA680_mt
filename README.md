# Student Performance Prediction using Ensemble Learning

[Heroku Deployment URL Placeholder]

## Overview

This project is developed by [Your Name] for the [Your Course/Class Name] at [Your Institution]. It employs an ensemble learning technique, particularly an XGBoost classifier, to predict the race/ethnicity of students based on their performance in math, reading, and writing exams. Despite the challenging nature of predicting race/ethnicity from academic scores, this model strives to demonstrate the application of machine learning for educational data analysis. Please note, there is no correlation between the predictor variables, and thus, the model is not accurate. The purpose of this project is to perform model deployments on Heroku.

## Features Used for Prediction

The model makes predictions based on the following features extracted from the Student Performance Dataset:

-   Math Score (`math_score`)
-   Reading Score (`reading_score`)
-   Writing Score (`writing_score`)

These scores are the key numerical features available in the dataset that are used as predictors for the race/ethnicity of the students.

## Tools and Libraries

The model was constructed using the following tools and libraries:

-   Jupyter Notebook: For writing and executing Python code in an interactive environment.
-   XGBoost: An optimized gradient boosting library designed to be highly efficient, flexible, and portable.
-   Pandas: For data manipulation and analysis, particularly for handling structured data.
-   scikit-learn (`sklearn`): For pre-processing data and for dividing the dataset into training and testing sets.
-   Flask: For creating a web application to deploy the model.
-   Heroku: For deploying the web application so that it can be accessed publicly.

## Model Training

The XGBoost classifier was chosen due to its ability to handle the non-linear relationship between the scores and the race/ethnicity class. The model was trained using the Student Performance Dataset, and special care was taken to preprocess the data appropriately, including handling missing values and encoding categorical features. The dataset was split into training and test sets to evaluate the model's performance.

The features were selected based on the hypothesis that academic performance could have some patterns or trends with respect to different groups, which the model might be able to learn and predict. The ensemble method aggregates the results of multiple decision trees to improve the model's predictive accuracy and control over-fitting.

## Deployment

The trained model is serialized and deployed using a Flask web application. The application provides a simple and user-friendly interface for inputting the scores and receiving predictions of race/ethnicity. The Heroku platform hosts the application, ensuring it is accessible to users for practical demonstrations and further research.

[Note: Remember to replace placeholders with actual names and URLs before finalizing the documentation.]
