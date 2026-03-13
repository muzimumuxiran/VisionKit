from imagededup.methods import CNN
from scipy.spatial.distance import cosine
import os
import shutil

target_features = {}

# Extract image features
def extract_features(image_path):
    cnn = CNN()
    
    feature = cnn.encode_image(image_path)  # Get feature vector
    return feature.flatten()  # Flatten feature vector to 1D

def get_cosine_similarity(target_folder, oringal_folder, receive_folder, similarity_threshold):

    target_paths = [os.path.join(target_folder, f) for f in os.listdir(target_folder) if f.endswith(('jpg', 'png', 'jpeg'))]
    oringal_paths = [os.path.join(oringal_folder, f) for f in os.listdir(oringal_folder) if f.endswith(('jpg', 'png', 'jpeg'))]

    # Extract feature vectors for all target images
    for target_path in target_paths:
        target_features[target_path] = extract_features(target_path)
    
    # Compute similarity between target and original images
    for oringal_path in oringal_paths:
        oringal_feature = extract_features(oringal_path)

        for target_path, feature in target_features.items():
            # Compute cosine similarity
            similarity = 1 - cosine(oringal_feature, feature)
            if similarity > similarity_threshold:
                shutil.copy(target_path,receive_folder)
