# Student Performance Prediction using Support Vector Machine (SVM)

[Heroku Deployment URL](https://ana680-mt-626c1dc6a887.herokuapp.com/)

## Overview

This project is developed by Elijah C Walker for the ANA680 course at National University. It employs a Support Vector Machine (SVM), a supervised machine learning model, to predict the race/ethnicity of students based on their performance in math, reading, and writing exams. The model's prediction accuracy is approximately 34%, indicating the complex nature of the task and the non-deterministic relationship between academic scores and race/ethnicity. The primary goal of this project is to demonstrate the process of model training and deployment rather than deriving a high-accuracy predictive system.

## Features Used for Prediction

The model leverages the following features from the Student Performance Dataset to make predictions:

-   Math Score (`math_score`)
-   Reading Score (`reading_score`)
-   Writing Score (`writing_score`)

These scores are pivotal quantitative features in the dataset utilized as indicators for predicting the students' race/ethnicity classifications.

## Tools and Libraries

The construction of the model involved the following tools and libraries:

-   Jupyter Notebook: For scripting and testing Python code interactively.
-   Support Vector Machine (SVM) from scikit-learn: For classification purposes, known for its effectiveness in high-dimensional spaces.
-   Pandas: For structured data operations and manipulations.
-   scikit-learn (`sklearn`): For data preprocessing, model training, and evaluation.
-   Flask: For web application creation, serving as the interface for model deployment.
-   Heroku: For hosting the Flask application, making it publicly accessible.

## Model Training

The SVM classifier was selected for its effectiveness in classification problems, especially in cases where the relationship between features and classes is not linearly separable. The Student Performance Dataset underwent rigorous preprocessing, including scaling of features and encoding of target classes. The dataset was then divided into a training set and a test set to both train and evaluate the model's performance.

Feature selection was grounded on the premise that certain trends in academic performance might be discernible and predictable for different racial/ethnic groups. Despite the model's moderate accuracy, it serves as a proof of concept for the deployment of machine learning models.

## Deployment

The SVM model was serialized and deployed through a Flask web application. The application offers an intuitive interface where users can enter student scores and obtain race/ethnicity predictions. Hosted on Heroku, the application is available for public access to showcase the deployment process and for educational purposes.

Please note that the use of race/ethnicity in predictive models is a sensitive topic and should be approached with caution. This model is for educational use only and does not promote or endorse the use of such predictive systems in real-world scenarios where they may contribute to biases or discrimination.

[Note: Always ensure sensitive and personal data is handled according to ethical standards and legal requirements.]
