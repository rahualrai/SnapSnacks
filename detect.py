import io
import os
from google.cloud import vision
from google.oauth2 import service_account

def detect_food():
    print("detect_food")
    credentials = service_account.Credentials.from_service_account_file('cloud.json')
    client = vision.ImageAnnotatorClient(credentials=credentials)

    file_name = os.path.abspath('image.jpg')

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    if not texts:
        return "not food"
    return(texts[0].description)