# Uber Trip Base Predictor

![Uber Trip Base Predictor](https://github.com/YourUsername/Uber-Trip-Base-Predictor/blob/main/assets/uber_trip_base_predictor.png)

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Results](#results)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Overview

The **Uber Trip Base Predictor** is a machine learning application designed to predict the base location of an Uber trip using features such as latitude, longitude, weekday, and hour of the trip. By analyzing historical Uber trip data, this project aims to provide accurate predictions that can help optimize operational efficiency and improve decision-making processes for ride-sharing platforms.

## Features

- **Real-time Prediction:** Enter trip details such as latitude, longitude, weekday, and hour, and get the predicted base location instantly.
- **Data Visualization:** Explore insightful visualizations to understand trip patterns, geographical distribution, and temporal trends.
- **User-friendly Interface:** A Streamlit-powered web application for seamless interaction and prediction.
- **Model Training and Evaluation:** Train a RandomForestClassifier on historical data and evaluate it using relevant metrics.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/YourUsername/Uber-Trip-Base-Predictor.git
    cd Uber-Trip-Base-Predictor
    ```

2. **Create a Virtual Environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the Dataset:**
    - Download the Uber trip data files and place them in the `Uber-dataset` directory.

## Usage

To run the Streamlit application:

```bash
streamlit run uber.py
