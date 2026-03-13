import cv2

def variance_of_laplacian(image):
	'''
    Compute the variance of the Laplacian response of an image
    '''
	return cv2.Laplacian(image, cv2.CV_64F).var()

#def remove_fuzzy(out_path, threshold):
    #for imagePath in paths.list_images(out_path):
        # Read image
        #image = cv2.imread(imagePath)
        # Convert image to grayscale
        #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Compute variance of the grayscale image
        #fm = variance_of_laplacian(gray)
        #text = "Not Blurry"
        #if fm < threshold:
            #print(f"Deleting blurry image: {imagePath}, Variance: {fm:.2f}")
            #os.remove(imagePath)
