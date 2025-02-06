import numpy as np

file_path = "models/smplx/SMPLX_NEUTRAL.npz"
data = np.load(file_path)

print(data.files)

for key in data.files:
    print(f"{key}: {data[key].shape}")