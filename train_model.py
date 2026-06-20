import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#--- LOAD DATA---
df = pd.read_csv("churn.csv")

#--- DATA CLEANING---
df.drop("customerID", axis=1, inplace=True)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors="coerce")
df["TotalCharges"].fillna(df["TotalCharges"].median(),inplace=True)

#--- ENCODE CATEGORICAL COLUMNS---
label_encoders = {}
for col in df.columns:
    if df[col].dtype == "object":
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

#--- FEATURES & TARGET---
X = df.drop("Churn", axis=1)
y = df["Churn"]

#--- TRAIN TEST SPLIT---
X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=42,stratify=y)

#--- TRAIN MODEL---
model = RandomForestClassifier(n_estimators=200,max_depth=10,random_state=42)
model.fit(X_train, y_train)

#--- EVALUATE---
pred = model.predict(X_test)
accuracy = accuracy_score(y_test,pred)
print(f"Accuracy: {accuracy:.4f}")

#--- SAVE MODEL---
joblib.dump(model,"model.pkl")
joblib.dump(label_encoders, "encoders.pkl")

print("✅ model.pkl saved successfully!")