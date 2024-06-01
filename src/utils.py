import cv2
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def display_images_with_bbox(image_files, label_files):
    # Get list of images in image directory

    for image_file, label_file in zip(image_files, label_files):
        # Read image
        image = cv2.imread(str(image_file))
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Read bounding box coordinates from label file
        with open(str(label_file), "r") as f:
            lines = f.readlines()

        # Plot image
        fig, ax = plt.subplots(1)
        ax.imshow(image_rgb)

        # Draw bounding boxes on image
        for line in lines:
            parts = line.strip().split(" ")
            class_id = int(parts[0])
            x_center = float(parts[1])
            y_center = float(parts[2])
            width = float(parts[3])
            height = float(parts[4])

            # Convert coordinates from normalized to absolute
            h, w = image.shape[:2]
            x_center *= w
            y_center *= h
            width *= w
            height *= h

            # Calculate bounding box coordinates
            x_min = x_center - width / 2
            y_min = y_center - height / 2
            rect_width = width
            rect_height = height

            # Create a Rectangle patch
            rect = patches.Rectangle(
                (x_min, y_min),
                rect_width,
                rect_height,
                linewidth=1,
                edgecolor="r",
                facecolor="none",
            )

            # Add the patch to the Axes
            ax.add_patch(rect)

        # Display image with bounding boxes
        plt.show()
