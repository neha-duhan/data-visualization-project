# Supermarket Sales Data Visualization

## Project Overview

This project focuses on Data Visualization using Python. The goal is to transform raw supermarket sales data into meaningful visual insights using charts and graphs. The project demonstrates how businesses can analyze sales trends, product performance, customer demographics, and customer ratings through visual analytics.

## Tools and Libraries Used

* Python
* Pandas
* Matplotlib
* Seaborn
* KaggleHub

## Dataset

Dataset: Supermarket Sales Dataset

The dataset contains information about:

* Sales transactions
* Product categories
* Customer demographics
* Payment methods
* Ratings
* Revenue and taxes

## Project Tasks

### 1. Data Loading

* Downloaded the dataset using KaggleHub.
* Loaded the CSV file into a Pandas DataFrame.

### 2. Data Cleaning

* Checked for missing values.
* Filled missing values in:

  * Product line
  * Customer type
* Converted the Date column to datetime format.

### 3. Data Visualization

#### Monthly Sales Trend (Line Chart)

* Created a line chart showing total sales across different months.
* Helps identify sales trends over time.

#### Product Category Analysis (Bar Chart)

* Created a bar chart to compare sales across product categories.
* Identifies the most popular product line.

#### Gender Distribution (Pie Chart)

* Visualized the percentage of male and female buyers.
* Helps understand customer demographics.

#### Customer Rating Distribution (Histogram)

* Displayed the distribution of customer ratings.
* Shows overall customer satisfaction levels.

## Key Findings

* Monthly sales trends provide insights into business performance over time.
* Product categories can be compared to identify top-selling items.
* Customer gender distribution helps understand the target audience.
* Most customer ratings are concentrated in the higher range, indicating positive customer experiences.

## How to Run

1. Install required libraries:

```bash
pip install pandas matplotlib seaborn kagglehub
```

2. Run the Python script:

```bash
python task2.py
```

3. The charts will be displayed automatically.

## Project Structure

```text
sales-data-visualization/
│
├── task2.py
├── README.md
└── requirements.txt
```

## Author
Neha Duhan 
Created as part of a Data Visualization Project using Python.
