# Examen DVC et Dagshub

**Name:** Frank Lee

**Email:** lee.frank.david@gmail.com

**Repository:** https://dagshub.com/codeByFrank/examen_dvc

## Project Overview

This project implements a complete DVC pipeline for mineral processing analysis, specifically focusing on the flotation process to predict silica concentration.

### Pipeline Stages

1. **download** - Downloads raw data from AWS S3
2. **data_split** - Splits data into training (80%) and testing (20%) sets
3. **normalize** - Normalizes features using StandardScaler
4. **grid_search** - Performs GridSearchCV to find optimal hyperparameters
5. **train** - Trains RandomForestRegressor with best parameters
6. **evaluate** - Evaluates model performance and generates metrics
