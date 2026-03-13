import os
from imagededup.methods import PHash

def remove_dup_PHash(image_dir):
    # Initialize perceptual hash algorithm
    phasher = PHash()
     # Generate hash dictionary
    encodings = phasher.encode_images(image_dir=image_dir)
    # Find duplicate images
    duplicates = phasher.find_duplicates(encoding_map=encodings)
    # Delete duplicates (keep only the first)
    for key, duplicate_list in duplicates.items():
        if len(duplicate_list) > 1:
            for duplicate_image in duplicate_list[1:]:  # Keep the first, delete the rest
                image_path = os.path.join(image_dir, duplicate_image)
                try:
                    os.remove(image_path)
                    print(f"Deleted {duplicate_image}")
                except FileNotFoundError:
                    continue
                    #print(f"File {duplicate_image} not found.")
                except PermissionError:
                    print(f"Permission denied to delete {duplicate_image}.")
                except Exception as e:
                    print(f"An error occurred while deleting {duplicate_image}: {e}")
