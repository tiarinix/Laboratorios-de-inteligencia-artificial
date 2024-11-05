import kagglehub

# Download latest version
path = kagglehub.dataset_download("apollo2506/landuse-scene-classification")

print("Path to dataset files:", path)