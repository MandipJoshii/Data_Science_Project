# Student Marks Analysis & Prediction

A machine learning project that predicts student final grades (G3)
using the UCI Student Performance Dataset (395 students, Math subject).

## Models Used
- Linear Regression → R²: 0.797
- Decision Tree Regressor → R²: 0.871
- Random Forest Regressor → R²: 0.85

## Features Used for Prediction
G1 (first period grade), G2 (second period grade),
Medu (mother's education), studytime

## Project Structure
- eda/ → exploratory data analysis (heatmap, histogram, boxplot, scatter, barplot, countplot)
- experiment/ → model training and evaluation
- dashboard/ → interactive Plotly Dash dashboard

## Dataset
UCI Machine Learning Repository — Student Performance Dataset
https://archive.ics.uci.edu/dataset/320/student+performance
## Tech Stack
Python, Pandas, Scikit-learn, Matplotlib, Seaborn, Plotly Dash