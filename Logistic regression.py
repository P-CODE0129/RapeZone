# ================================
# STEP 9: Logistic Regression
# ================================
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# ================================
# STEP 10: Prediction
# ================================
y_pred = model.predict(X_test)

# ================================
# STEP 11: Evaluation
# ================================
print("\n🔹 MODEL PERFORMANCE 🔹")
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

# ================================
# 📊 GRAPH 2: Confusion Matrix (Clean)
# ================================
plt.figure(figsize=(6,5))

sns.heatmap(cm,
            annot=True,
            fmt='d',
            cmap='Blues',
            xticklabels=["H", "M", "L"],
            yticklabels=["H", "M", "L"])

plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.title("Confusion Matrix (H=High, M=Medium, L=Low)")
plt.savefig("Confusion Matrix of Logistics Regression.png")
files.download("Confusion Matrix of Logistics Regression.png")
plt.show()

# ================================
# STEP 12: Better District Classification
# ================================
district_result = df.groupby("District").agg({
    "Total_Cases": "mean"   # 🔥 change from sum → mean
}).reset_index()

# Correct classification (fixed)
q1 = district_result["Total_Cases"].quantile(0.4)
q2 = district_result["Total_Cases"].quantile(0.7)

def classify_district(x):
    if x > q2:
        return "High"
    elif x > q1:
        return "Medium"
    else:
        return "Low"

district_result["Risk_Level"] = district_result["Total_Cases"].apply(classify_district)

print(district_result["Risk_Level"].value_counts())

# Sort
district_result = district_result.sort_values(by="Total_Cases", ascending=False)

# ================================
# STEP 12.1: Merge Trend + Age
# ================================
district_result = district_result.merge(
    trend_df[["District", "Trend"]],
    on="District"
)

district_result = district_result.merge(
    age_df[["District", "Most_Affected_Age"]],
    on="District"
)

# ================================
# STEP 13: Smart Safety Advice
# ================================
def smart_advice(row):
    risk = row["Risk_Level"]
    trend = row["Trend"]
    age = row["Most_Affected_Age"]

    if risk == "High":
        if trend == "Increasing":
            return f"🔴 HIGH ALERT: Cases rising fast, situation worsening. Most affected age: {age}"
        else:
            return f"🔴 HIGH ALERT: Stay alert. Most affected age: {age}"

    elif risk == "Medium":
        if trend == "Increasing":
            return f"🟡 MEDIUM ALERT: Cases increasing, may turn HIGH. Most affected age: {age}"
        elif trend == "Decreasing":
            return f"🟡 MEDIUM ALERT: Situation improving. Most affected age: {age}"
        else:
            return f"🟡 MEDIUM ALERT: Stay cautious. Most affected age: {age}"

    else:
        return f"🟢 LOW ALERT: Area relatively safe. Most affected age: {age}"

district_result["Safety_Advice"] = district_result.apply(smart_advice, axis=1)

# ================================
# STEP 14: Final Output
# ================================

pd.set_option('display.max_colwidth', None)

print("\n🔹 FINAL DISTRICT RISK 🔹\n")
print(district_result.to_string())

print("\nTotal districts:", len(district_result))

print("\nSorted by Risk Level:\n")
print(district_result.sort_values("Risk_Level").to_string())


# ================================
# STEP 15: Export to Excel
# ================================

# Save file
district_result.to_excel("District_Risk_Output.xlsx", index=False)

# Download (for Google Colab)
from google.colab import files
files.download("District_Risk_Output.xlsx")

# ================================
# 📊 FINAL GRAPH: Improved Version
# ================================
# ================================
# 📊 FINAL GRAPH (CLEAN + VALUES)
# ================================
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Color mapping
color_map = {"High": "red", "Medium": "gold", "Low": "green"}
colors = district_result["Risk_Level"].map(color_map)

# Create figure
plt.figure(figsize=(16,7))

bars = plt.bar(
    district_result["District"],
    district_result["Total_Cases"],
    color=colors
)

# Titles and labels
plt.title("District Risk Levels (Color Coded)", fontsize=16, fontweight='bold')
plt.xlabel("District", fontsize=12)
plt.ylabel("Total Cases", fontsize=12)

# X-axis formatting
plt.xticks(rotation=60, ha='right', fontsize=9)

# Grid for clarity
plt.grid(axis='y', linestyle='--', alpha=0.5)

# 🔥 Add values above bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + (height * 0.02),  # auto spacing
        int(height),
        ha='center',
        va='bottom',
        fontsize=8
    )

# Legend
plt.legend(handles=[
    mpatches.Patch(color='red', label='High Risk'),
    mpatches.Patch(color='gold', label='Medium Risk'),
    mpatches.Patch(color='green', label='Low Risk')
])

# Adjust layout
plt.tight_layout()

# Save (high quality)
plt.savefig("District_Risk_Final.png", dpi=300)

# Download (for Colab)
from google.colab import files
files.download("District_Risk_Final.png")

plt.show()

