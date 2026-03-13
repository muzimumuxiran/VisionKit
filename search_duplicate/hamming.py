from imagededup.methods import PHash
import os
import shutil



def get_hamming_similarity(target_folder, oringal_folder, receive_folder, similarity_threshold):

    phash = PHash()

    target_paths = [os.path.join(target_folder, f) for f in os.listdir(target_folder) if f.endswith(('jpg', 'png', 'jpeg'))]
    oringal_paths = [os.path.join(oringal_folder, f) for f in os.listdir(oringal_folder) if f.endswith(('jpg', 'png', 'jpeg'))]

    target_hashes = {target_path: phash.encode_image(target_path) for target_path in target_paths}

    # Compare each image in the original folder against the encoded target set
    for oringal_path in oringal_paths:

        # Compute hash of the original image
        oringal_hash = phash.encode_image(oringal_path)

        for target_path, target_hash in target_hashes.items():
            # Compute Hamming distance between hashes
            hamming_dis = phash.hamming_distance(oringal_hash, target_hash)
            similarity = 1 - (hamming_dis / 64)
            if similarity > similarity_threshold:
                shutil.copy(target_path,receive_folder)
