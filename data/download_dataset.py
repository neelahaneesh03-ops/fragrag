import pandas as pd
# Load the dataset from Kaggle
pd_dataset = pd.read_csv("/Users/haneesh/Documents/fragrag/data/fra_perfumes.csv")

#Drop values with empty description
pd_dataset = pd_dataset.dropna(subset=["Description"])

#Fill the empty values in the "Rating Value" column with the zero
pd_dataset["Rating Value"] = pd_dataset["Rating Value"].fillna(0)
pd_dataset["Rating Count"] = pd_dataset["Rating Count"].fillna(0)

#Need to remove names with are not english characters
pd_dataset = pd_dataset[pd_dataset["Name"].str.match(r'^[\x00-\x7F]*$', na=False)]

#Remove gender from perfume names
pd_dataset['Name'] = pd_dataset['Name'].str.replace(r'for women and men|for women|for men', '', regex=True).str.strip()

#Remove commas from the "Rating Count" column and convert it to integer
pd_dataset["Rating Count"] = pd_dataset["Rating Count"].astype(str).str.replace(",", "").str.strip().fillna(0)
pd_dataset["Rating Count"] = pd.to_numeric(pd_dataset["Rating Count"], errors='coerce').fillna(0).astype(int)

#Save the cleaned dataset to a new CSV file
pd_dataset.to_csv("/Users/haneesh/Documents/fragrag/data/cleaned_fra_perfumes.csv", index=False)

print(len(pd_dataset))