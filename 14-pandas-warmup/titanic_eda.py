import pandas as pd

df = pd.read_csv("train.csv")
print(df.shape)
print(df.head())
print(df.info())

print(df["Survived"].value_counts())
print(df["Sex"].value_counts())
print(df["Pclass"].value_counts())

survived_by_sex = df.groupby("Sex")["Survived"].agg(["mean", "count", "sum"])
survived_by_sex.columns = ["survived_rate", "survivors", "total"]
survived_by_sex["survived_rate"] = survived_by_sex["survived_rate"].round(2)

print(survived_by_sex)

survived_by_class = df.groupby("Pclass")["Survived"].agg(["mean", "count", "sum"])
survived_by_class.columns = ["survived_rate", "survivors", "total"]
survived_by_class["survived_rate"] = survived_by_class["survived_rate"].round(2)

print(survived_by_class)

print(df["Age"].describe())
print(f'Пропуски в Age: {df["Age"].isna().sum()}')

bins = [0,12,18,60,100]
labels = ["child", "teen", "adult", "senior"]

df['age_group'] = pd.cut(df['Age'], bins=bins, labels=labels)
print(df['age_group'].value_counts())

survived_by_age = df.groupby("age_group", observed=True)["Survived"].agg(["mean", "count", "sum"])
survived_by_age.columns = ["survived_rate", "survivors", "total"]
survived_by_age["survived_rate"] = survived_by_age["survived_rate"].round(2)

print(survived_by_age)

survived_by_class_sex = df.groupby(["Pclass", "Sex"])["Survived"].agg(["mean", "count", "sum"])
survived_by_class_sex.columns = ["survived_rate", "survivors", "total"]
survived_by_class_sex["survived_rate"] = survived_by_class_sex["survived_rate"].round(2)

print(survived_by_class_sex)