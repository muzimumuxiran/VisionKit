from search_duplicate import cosine
from search_duplicate import hamming


def search_duplicate_img(function, target_folder, oringal_folder, receive_folder, similarity_threshold):

    if function == "cosine":
        cosine.get_cosine_similarity(target_folder, oringal_folder, receive_folder, similarity_threshold)

    if function == "hamming":
        hamming.get_hamming_similarity(target_folder, oringal_folder, receive_folder, similarity_threshold)