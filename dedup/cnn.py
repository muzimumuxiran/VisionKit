from imagededup.methods import CNN
import os

def remove_dup_CNN(image_dir, similarity_threshold):
    cnn = CNN()
    duplicates = cnn.find_duplicates_to_remove(image_dir=image_dir, min_similarity_threshold = similarity_threshold)

    for duplicate_image in duplicates[1:]:  # Keep the first, delete the rest
        image_path = os.path.join(image_dir, duplicate_image)
        try:
            os.remove(image_path)
            print(f"Deleted {duplicate_image}")
        except FileNotFoundError:
            continue
        except PermissionError:
            print(f"Permission denied to delete {duplicate_image}.")
        except Exception as e:
            print(f"An error occurred while deleting {duplicate_image}: {e}")
