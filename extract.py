import zipfile

# Open and extract dataset ZIP file
with zipfile.ZipFile("data/titanic-dataset.zip", "r") as zip_ref:
    zip_ref.extractall("data")  # Extract inside 'data' folder

print("Dataset extracted successfully!")
 
