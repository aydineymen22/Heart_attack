import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('updated_version.csv')

# print(df.head())
# print(df.columns)
# print(df.describe())
print(df.info())

# Distinguishing columns according to the type
facet_categories = ["sex", "smoking", "diabetes", "heart_attack"]
numeric_vars = ["total_cholesterol", "ldl", "hdl", "systolic_bp", "diastolic_bp"]

# Define a list of colors for the charts
colors = ['blue', 'green', 'red', 'purple', 'orange']


plt.figure(figsize=(15, 10))  

# Creating Histogram plots for each numerical columns 
for i, (column_name, color) in enumerate(zip(numeric_vars, colors), 1):  
    plt.subplot(2, 3, i)  
    plt.hist(df[column_name], bins=30, edgecolor='black', color=color)  
    plt.title(f"Histogram of {column_name}")  
    plt.xlabel(column_name)  
    plt.ylabel('Count')  

plt.tight_layout()

plt.show()

plt.clf()


#Creating plots for undertstanding how numerical columns and age related
for i, (column_name, color) in enumerate(zip(numeric_vars, colors), 1):
    plt.subplot(2,3,i)
    axplot = sns.lineplot(data=df, x='age', y=column_name, color=color, errorbar=None)
    plt.title(f'Age_vs_{column_name}')
    plt.subplots_adjust(wspace=0.9)
plt.tight_layout()
plt.show()    


sns.set_style("whitegrid")


fig, axes = plt.subplots(len(facet_categories), len(numeric_vars), figsize=(20, 16))
fig.suptitle("Faceted Distributions of Health Indicators", fontsize=16)

for i, facet in enumerate(facet_categories):
    for j, var in enumerate(numeric_vars):
        sns.histplot(data=df, x=var, hue=facet, multiple="stack", bins=30, ax=axes[i, j])
        axes[i, j].set_title(f"{var} by {facet}")
        axes[i, j].tick_params(axis="x", rotation=45)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.subplots_adjust(hspace=0.6, wspace=0.4)
plt.show()




# Scatter Plots: Systolic BP vs Total Cholesterol
fig, axes = plt.subplots(len(facet_categories), 1, figsize=(10, 20))
fig.suptitle("Scatter Plots: Systolic BP vs Total Cholesterol", fontsize=16)

for i, facet in enumerate(facet_categories):
    sns.scatterplot(data=df, x="total_cholesterol", y="systolic_bp", hue=facet, alpha=0.7, ax=axes[i])
    axes[i].set_title(f"Systolic BP vs Total Cholesterol by {facet}")
    axes[i].tick_params(axis="x", rotation=45)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.subplots_adjust(hspace=0.6)
plt.show()



fig, axes = plt.subplots(len(numeric_vars), len(facet_categories), figsize=(20, 20))
fig.suptitle("Box Plots of Health Indicators by Categorical Variables", fontsize=16)

for i, var in enumerate(numeric_vars):
    for j, facet in enumerate(facet_categories):
        sns.boxplot(data=df, x=facet, y=var, ax=axes[i, j])
        axes[i, j].set_title(f"{var} by {facet}")
        axes[i, j].tick_params(axis="x", rotation=45)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.subplots_adjust(hspace=0.6, wspace=0.4)
plt.show()