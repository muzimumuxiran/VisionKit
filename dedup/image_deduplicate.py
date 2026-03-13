from dedup import cnn
from dedup import hash

def img_deduplicate(function, img_dir, similarity_threshold):

    if function == "CNN":
        cnn.remove_dup_CNN(img_dir, similarity_threshold)
    
    if function == "PHash":
        hash.remove_dup_PHash(img_dir, similarity_threshold)