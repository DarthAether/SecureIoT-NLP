import os


data_path = r"D:\3_2_AD\SecureIoT-NLP\data\House_A"
files = os.listdir(data_path)
print(f"Files in {data_path}: {files[:5]}")  # Show the first 5 files
