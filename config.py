# config.py
MAX_WEB_IMAGES = 20  # Number of cartoon/celebrity images to fetch
IMAGE_SIZE = (224, 224)  # ResNet50 input size

CARTOON_QUERY = "famous cartoon character face"
CELEB_QUERY = "celebrity headshot"

TEMP_FOLDER = "downloaded_images"
CARTOON_FOLDER = f"{TEMP_FOLDER}/cartoons"
CELEB_FOLDER = f"{TEMP_FOLDER}/celebs"
