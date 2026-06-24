import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
import os

# Download dataset
path = kagglehub.dataset_download("abhilashakumari100/supermarket-sales")
print("Dataset Path:", path)

# Show files in the dataset folder
print("Files:")
print(os.listdir(path))

# Load Dataset
csv_file = os.path.join(path, "supermarket_sales.csv")
df = pd.read_csv(csv_file)
 
# Data Cleaning
print("Missing Values:")
print(df.isnull().sum())

# Fill missing categorical values
df["Product line"] = df["Product line"].fillna("Unknown")
df["Customer type"] = df["Customer type"].fillna("Unknown")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# 1. Line Chart - Monthly Sales

df["Month"] = df["Date"].dt.month_name()
monthly_sales = (
    df.groupby("Month")["Total"]
    .sum()
)
month_order = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
]
monthly_sales = monthly_sales.reindex(
    [m for m in month_order if m in monthly_sales.index]
)
plt.figure(figsize=(10,5))
plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    color="blue"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

# 2. Bar Chart - Product Line
plt.figure(figsize=(10,5))

sns.countplot(
    data=df,
    x="Product line",
    palette="viridis"
)

plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Number of Sales")
plt.xticks(rotation=30)
plt.show()
 
# 3. Pie Chart - Gender
gender_counts = df["Gender"].value_counts()

plt.figure(figsize=(7,7))

plt.pie(
    gender_counts,
    labels=gender_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Male vs Female Buyers")
plt.show()

# 4. Histogram - Ratings
plt.figure(figsize=(8,5))

plt.hist(
    df["Rating"],
    bins=10,
    color="orange"
)

plt.title("Customer Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()
 
# Summary
print("\nTop Selling Category:")
print(df["Product line"].value_counts().head(1))
print("\nGender Distribution:")
print(df["Gender"].value_counts())