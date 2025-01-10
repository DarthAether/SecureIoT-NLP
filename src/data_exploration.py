import os

# Set the path to the data
data_path = r"D:\3_2_AD\SecureIoT-NLP\data\House_A"

# List the files in the directory
files = os.listdir(data_path)
print(f"Files in {data_path}: {files[:5]}")  # Show the first 5 files

# Read and inspect a single file
file_path = os.path.join(data_path, "DAY_1.txt")
with open(file_path, 'r') as file:
    for line in file.readlines()[:10]:  # Display the first 10 lines
        print(line.strip())
