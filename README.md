# Mask Detection with YOLOv8

## Introduction
This project focuses on training a YOLOv8n model to detect whether someone is wearing a mask or not. The dataset used for training is the [Face Mask Dataset (YOLO Format)](https://www.kaggle.com/datasets/aditya276/face-mask-dataset-yolo-format/data) obtained from Kaggle. The YOLOv8n model is a lightweight version of YOLOv8, suitable for resource-constrained environments.

## Project Structure
- **datasets**: Contains the training and validation datasets in YOLO format.
- **runs**: Stores YOLO models and logs during training.
- **src**: Source code directory.
    - **utils.py**: Utility functions for training and inference.
- **main.ipynb**: Jupyter notebook containing the main workflow of the project.

## Steps
1. **Data Exploration**: Display some images and labels from the dataset.
2. **Data Preprocessing**: Resize images to 320x320 pixels for training.
3. **Data Visualization**: Display images after resizing.
4. **Model Training**: Train the YOLOv8n model using the resized dataset.
5. **Inference**: Make predictions using the trained model and display the result.

## Acknowledgments
- The [Face Mask Dataset (YOLO Format)](https://www.kaggle.com/datasets/aditya276/face-mask-dataset-yolo-format/data) on Kaggle.
- YOLOv8n model implementation provided by [YOLOv5](https://github.com/ultralytics/ultralytics).