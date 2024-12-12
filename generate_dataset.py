import pandas as pd
import numpy as np

# Create synthetic dataset
data = {
    "Title": [f"Book {i}" for i in range(1, 101)],
    "Author": [f"Author {i}" for i in range(1, 101)],
    "Genre": np.random.choice(["Fiction", "Non-Fiction", "Sci-Fi", "Biography"], 100),
    "PublishedYear": np.random.randint(1980, 2023, 100),
    "Price": np.random.uniform(5.0, 50.0, 100).round(2),
    "Rating": np.random.uniform(1.0, 5.0, 100).round(1),
    "Target": np.random.choice([0, 1], 100),
}

df = pd.DataFrame(data)
df.to_csv("sample_dataset.csv", index=False)
print("Synthetic dataset saved as sample_dataset.csv")
