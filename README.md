# Data Visualization with Python

## Project Overview
This project is part of the Codecademy **Data Visualization with Python** course. It explores various techniques to visualize health-related data using **Pandas**, **Matplotlib**, and **Seaborn**. The dataset used is `updated_version.csv`, which contains numerical continuous and binary variables related to health indicators.I solely created plots since this project only wanted me to do so. 

## Dataset Description
The dataset includes the following types of variables:

- **Binary Variables:**
  - `sex`
  - `smoking`
  - `diabetes`
  - `heart_attack`

- **Numerical Variables:**
  - `total_cholesterol`
  - `ldl`
  - `hdl`
  - `systolic_bp`
  - `diastolic_bp`
  
## Visualizations
The project includes several types of data visualizations to better understand the relationships within the dataset:

1. **Histograms**
   - Distribution of numerical variables.
   - Visualized using `plt.hist()` with different colors for clarity.

2. **Line Plots (Age vs. Health Indicators)**
   - Relationship between `age` and numerical variables.
   - Created using `sns.lineplot()`.

3. **Faceted Histograms**
   - Distribution of numerical variables grouped by categorical variables.
   - Implemented using `sns.histplot()` with a `hue` argument.

4. **Scatter Plots**
   - Relationship between `total_cholesterol` and `systolic_bp`.
   - Differentiated by categorical variables using `sns.scatterplot()`.

5. **Box Plots**
   - Comparison of numerical variables across categorical variables.
   - Created using `sns.boxplot()`.

## Requirements
To run the code, ensure you have the following Python libraries installed:

```sh
pip install pandas matplotlib seaborn
```

## How to Run
1. Clone this repository:
   ```sh
   git clone https://github.com/aydineymen22/heart_attack.git
   ```
2. Navigate to the project folder:
   ```sh
   cd heart_attack
   ```
3. Run the script:
   ```sh
   python heart_attack.py
   ```

## Contact
For any questions or suggestions, feel free to reach out or open an issue on GitHub.

---
**Author:**  Eymen AYDIN  
**Date:** February 2025

