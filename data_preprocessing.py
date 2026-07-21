# ================================
# STEP 1: Import Libraries
# ================================
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ================================
# STEP 2: Upload Dataset
# ================================
from google.colab import files
uploaded = files.upload()
df = pd.read_csv(io.BytesIO(uploaded[list(uploaded.keys())[0]]))


# ================================
# STEP 4: Data Cleaning
# ================================
df["District"] = df["District"].str.strip().str.upper()
df.dropna(inplace=True)
df = df.sort_values(["District", "Year"])

# ================================
# STEP 5: Feature Engineering
# ================================
df["growth_rate"] = df.groupby("District")["Total_Cases"].pct_change()
df["cases_per_female"] = df["Total_Cases"] / df["female_total"]
df["year_diff"] = df["Year"] - df["Year"].min()
df.fillna(0, inplace=True)

# ================================
# STEP 5.1: Trend Calculation
# ================================
trend_df = df.groupby("District")["growth_rate"].mean().reset_index()

def get_trend(val):
    if val > 0.05:
        return "Increasing"
    elif val < -0.05:
        return "Decreasing"
    else:
        return "Stable"

trend_df["Trend"] = trend_df["growth_rate"].apply(get_trend)

# ================================
# STEP 5.2: Age Group Analysis
# ================================
age_cols = [
    "Below_6_years",
    "6_12_years",
    "12_16_years",
    "16_18_years",
    "18_30_years",
    "30_45_years",
    "45_60_years",
    "60_plus_years"
]

age_df = df.groupby("District")[age_cols].sum().reset_index()

age_df["Most_Affected_Age"] = age_df[age_cols].idxmax(axis=1)

# ================================
# STEP 6: Create Target (Risk Level)
# ================================
def classify_risk(x):
    if x > df["Total_Cases"].quantile(0.66):
        return "High"
    elif x > df["Total_Cases"].quantile(0.33):
        return "Medium"
    else:
        return "Low"

df["Risk_Level"] = df["Total_Cases"].apply(classify_risk)

# ================================
# 📊 GRAPH 1: Top Districts (Only useful graph)
# ================================
district_cases = df.groupby("District")["Total_Cases"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
district_cases.head(10).plot(kind="bar")
plt.title("Top Districts by Total Cases")
plt.xlabel("District")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.show()

# ================================
# STEP 7: Prepare Features (NO Total_Cases)
# ================================
X = df[
    [
        "female_total",
        "growth_rate",
        "cases_per_female",
        "year_diff"
    ]
]

y = df["Risk_Level"]

# ================================
# STEP 8: Train-Test Split
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
