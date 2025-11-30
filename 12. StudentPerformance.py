import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

url = "student_data.csv"
data = pd.read_csv(url)

data["pass"] = (data["G3"] >= 10).astype(int)

features = ["studytime", "failures", "absences"]
X = data[features]
y = data["pass"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

importance = model.feature_importances_
sns.barplot(x=features, y=importance)
plt.title("Feature Importance")
plt.show()
