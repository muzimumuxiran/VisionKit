import cv2
import os
from imutils import paths
from fuzzy import laplacian
from fuzzy import niqe

def remove_fuzzy_picture(out_path, lapacian_threshold, niqe_threshold):
    
    for imagePath in paths.list_images(out_path):
        # Read image
        image = cv2.imread(imagePath)
        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Compute variance of the grayscale image
        fm = laplacian.variance_of_laplacian(gray)
        # Compute NIQE score
        score = niqe.detect_blurry_images(imagePath)

        if fm < lapacian_threshold or score > niqe_threshold:
            print(f"Deleting blurry image: {imagePath}, Variance: {fm:.2f}, Score: {score:.2f}")
            os.remove(imagePath)
