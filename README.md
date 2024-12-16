# NASA Battery Dataset Analysis

This repository focuses on the analysis of the NASA Battery Dataset, which provides data on the aging process of Li-ion batteries through various operational profiles (charge, discharge, and impedance tests) under different temperature conditions. The dataset also includes electrochemical impedance spectroscopy (EIS) measurements to monitor internal battery parameters, such as impedance, electrolyte resistance (Re), and charge transfer resistance (Rct).

## Project Description

The goal is to visualize how key battery parameters change as the battery undergoes repeated charge and discharge cycles. We use Plotly to generate interactive plots that demonstrate these changes and provide insights into the battery aging process.

## Files Included

- nasa_battery_dataset.csv- A cleaned version of the raw dataset containing the necessary data for analysis.
- battery_analysis.py- Python script used for data cleaning, preprocessing, and visualizations.
- plotly_visualization.py- Script for generating interactive plots with Plotly.

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/username/repository-name.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the analysis script:
    ```bash
    python battery_analysis.py
    ```

## Requirements

- pandas
- plotly
- numpy
- matplotlib



