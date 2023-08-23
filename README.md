# Superstore Data Analysis

This repository contains a dataset named "Superstore_dataset.csv" that provides information about products sold from 2014 to 2017 in a superstore located in the US. 
Additionally, we have used a "geo_location.csv" dataset to obtain the latitude and longitude of each city.

## Essential Steps of EDA
We will perform the 3 essential steps of Exploratory Data Analysis using the Pandas library:

### 1. Data Exploration
We initially recommend exploring the variables in Excel to get a good understanding of the dataset.
Next, we import the dataset using the Python Pandas library and use various key exploration commands to gain insights into the data.

### 2. Data Cleaning
If necessary, we remove any rows that have missing values to ensure the dataset is complete and ready for analysis.
Please note that we have decided not to remove any outliers at this stage, further investigation is required before making decisions on outlier treatment.

### 3. Data Analysis
In this step, we answer some specific questions related to the dataset using appropriate graphs and visualisations to provide meaningful insights.
We have used Matplotlib, Seaborn and Plotly.

## Application

I have created an application with two of the visualisations from the analysis above:
- Quantity of products sold by US state
- Quantity of products sold in California cities

## Instructions
To run the analysis code, open the file "Superstore_project" on google colab and follow the steps.

Follow these steps to see the web application page (MacBook users):
- download the repository and upload it in VS Code
- right click on the "App" folder and choose "Open in integrated terminal"
- to create the virtual environment, type: python3 -m venv myenv
- to activate the environment, type: source myenv/bin/activate
- to install the libraries from the requirements file, type: pip install -r requirements.txt
- run the code in the file "app-python.py"
- on your browser, copy the link where Dash is running (the link is given in the terminal when you run the python code)

## Contributions
This project was realised during a course at TechTalent Academy.
We welcome contributions to this repository. If you find any issues or improvements, please create a pull request, and we will be happy to review it.
