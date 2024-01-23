import pydicom
import matplotlib.pyplot as plt

# Load the DICOM file
dicom_file_path = '0002.DCM'
dataset = pydicom.dcmread(dicom_file_path)

print(dataset)

print("/n")

print("Patient ID: ", dataset.PatientID)
print("Patient name: ", dataset.PatientName)
print("Modality: ", dataset.Modality)
print("Image dimensions: ", dataset.pixel_array)
print("Pixel data: ", dataset.PixelData)

