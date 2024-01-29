import pydicom
import matplotlib.pyplot as plt
import os
from collections import Counter

# Directory containing DICOM files
dicom_dr = './files'

# Get a list of all DICOM files in the directory
dicom_files = [os.path.join(dicom_dr, file) for file in os.listdir(dicom_dr) if file.endswith('.DCM')]

# List to store all VR tags
all_vr_tags = []

# Iterate over each DICOM file
for dicom_file_path in dicom_files:
    # Load the DICOM file
    dataset = pydicom.dcmread(dicom_file_path)

    # Extract VR tags from the DICOM file and add them to the list
    vr_tags = [data_element.VR for data_element in dataset]
    all_vr_tags.extend(vr_tags)

# Count the occurrences of each VR tag
vr_tags_counter = Counter(all_vr_tags)


# Extract unique VR tags and their corresponding counts
unique_vr_tags = list(vr_tags_counter.keys())
occurrences = list(vr_tags_counter.values())

# Plotting the histogram
plt.bar(unique_vr_tags, occurrences)
plt.xlabel('VR Tags')
plt.ylabel('Number of Occurrences')
plt.title('Occurrences of Unique VR Tags in DICOM Files')
plt.show()

    # Print information about the DICOM file
    # print("File:", dicom_file_path)
    # print("Patient ID: ", dataset.PatientID)
    # print("Patient name: ", dataset.PatientName)
    # print("Modality: ", dataset.Modality)
    # print("Image dimensions: ", dataset.pixel_array)
    # print("Pixel data: ", dataset.PixelData)
    # print("\n")
