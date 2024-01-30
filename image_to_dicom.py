import pydicom
from PIL import Image
import numpy as np

def jpeg_to_dicom(jpeg_path, dicom_path):
    # Load the JPEG image
    img = Image.open(jpeg_path)

    # Convert the image to a numpy array
    img_array = np.array(img)

    # Create a DICOM dataset
    ds = pydicom.Dataset()

    # Set DICOM attributes
    ds.PatientName = "Anonymous"
    ds.PatientID = "123456"
    ds.Modality = "OT"
    ds.SeriesInstanceUID = "1.2.3.4.5.6.7.8.9.10"
    ds.SOPInstanceUID = "1.2.3.4.5.6.7.8.9.11"
    ds.SOPClassUID = "1.2.840.10008.5.1.4.1.1.481.3"

    # Set transfer syntax
    ds.is_little_endian = True
    ds.is_implicit_VR = True

    # Set pixel data
    ds.PixelData = img_array.tobytes()

    # Save the DICOM file
    ds.save_as(dicom_path)

# Example usage
jpeg_file = "./files/image.jpg"
dicom_file = "./files/output.DCM"

jpeg_to_dicom(jpeg_file, dicom_file)
