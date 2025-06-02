# face-emotion-recognition
This project presents a face emotion recognition system developed using the FER-2013 dataset and YOLO object detection architecture. The aim is to detect human faces in images and classify their emotional expressions into predefined categories.
______________
Overview
The system uses computer vision and deep learning techniques to preprocess facial image data, detect faces, and convert them into a format compatible with the YOLO model. The final objective is to enable robust training and accurate emotion classification using real-time or static input.
______________
Dataset
Source: FER-2013 from Kaggle

Content: The dataset contains grayscale facial images labeled with one of seven emotional expressions:

Angry
Disgust
Fear
Happy
Neutral
Sad
Surprise


______________
Methodology

1-) Downloaded the FER-2013 dataset using the opendatasets Python library.

2-) Loaded the dataset and structured it according to YOLO requirements.

3-) Detected faces in each image using OpenCV’s Haar Cascade classifier.

4-) Converted bounding box coordinates to YOLO format (normalized values).

5-) Organized images and label files into training and testing directories under YOLO structure.

6-) Prepared the dataset for training a YOLO model by creating:

-Image directories: /images/train and /images/test

-Label directories: /labels/train and /labels/test

7-) Verified the conversion process and confirmed dataset readiness for YOLO training.


______________
Tools and Libraries

Python

OpenCV

Ultralytics YOLO

Pandas

Matplotlib

TQDM

Opendatasets



______________
Model Notes

-The YOLO model used is yolo11n.pt, which must be present in the working directory.

-Face detection is performed before classification to ensure emotion labels are applied only to facial regions.
