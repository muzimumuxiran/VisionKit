import pyiqa
import numpy as np
from PIL import Image

def detect_blurry_images(file_path, metric_name='niqe'):
    """
    Detect blurry images in a dataset
    """
    metric = pyiqa.create_metric(metric_name)
    #blurry_images = []
    image = Image.open(file_path).convert('RGB')
    
    # Compute blur score
    score = metric(image)

    return score
