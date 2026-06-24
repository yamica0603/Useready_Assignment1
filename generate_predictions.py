import os
import pandas as pd

from src.document_processor import process_document


TEST_FOLDER = "data/test"

predictions = []

for filename in os.listdir(TEST_FOLDER):

    if filename.startswith("."):
        continue

    file_path = os.path.join(
        TEST_FOLDER,
        filename
    )

    try:

        result = process_document(file_path)

        print(result)

        row = {
            "filename": filename,
            **result["metadata"]
        }

        predictions.append(row)

    except Exception as e:

        print(f"ERROR processing {filename}")
        print(e)


df = pd.DataFrame(
    predictions
)

print("\n====================")
print("PREDICTIONS LIST")
print("====================")
print(predictions)

print("\n====================")
print("DATAFRAME")
print("====================")
print(df.head())

print("\nShape:", df.shape)

os.makedirs(
    "predictions",
    exist_ok=True
)

df.to_csv(
    "predictions/predictions.csv",
    index=False
)

print(
    "\nPredictions saved successfully!"
)

print("Files found:")

for filename in os.listdir(TEST_FOLDER):
    print(filename)

print("Current Working Directory:", os.getcwd())
print("Test Folder Exists:", os.path.exists(TEST_FOLDER))
print("Test Folder:", TEST_FOLDER)