from extract_food import process_image

pic_url = "https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg"
nutritional_value = process_image(pic_url)
print(nutritional_value) #no need to connect to twilio