def lambda_handler(event, context):
    from selenium import webdriver
    from selenium.common.exceptions import TimeoutException
    import os

    # input
    url = str(event['url'])

    # FIXME
    try:
        IMAGE_NAME = str(event['image_name'])
    except KeyError as ke:
        IMAGE_NAME = 'img.png'
    try:
        MAX_PAGE_LOAD_TIME = int(event['max_page_load_time'])
    except KeyError as ke:
        MAX_PAGE_LOAD_TIME = 4
    try:
        WINDOW_SIZE_WIDTH = int(event['window_size_width'])
    except KeyError as ke:
        WINDOW_SIZE_WIDTH = 1024
    try:
        WINDOW_SIZE_HEIGHT = int(event['window_size_height'])
    except KeyError as ke:
        WINDOW_SIZE_HEIGHT = 768

    # function
    driver = webdriver.PhantomJS(service_log_path=os.path.devnull, executable_path="./phantomjs/bin/phantomjs")
    driver.set_window_size(WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT) # set the window size that you need 
    driver.get(url)
    load_page_completely(MAX_PAGE_LOAD_TIME)
    image = driver.get_screenshot_as_base64()
    import base64
    url = load_image_to_s3(base64.b64decode(image), IMAGE_NAME)
    return {"imageurl" : url}

def load_page_completely(page_load_time):
    import time
    time.sleep(page_load_time)

def load_image_to_s3(image, name):
    import boto3
    bucket_name = "alexa-image-store"
    folder_name = "alexa-location-annotator" # can be used in future
    object_name = name # for now 
    key = folder_name + '/' + object_name
    s3_client = boto3.client('s3')
    s3_client.put_object(ACL='public-read', 
                         Body=image, 
                         Key=key, 
                         Bucket=bucket_name,
                         Metadata={"Content-Type" :"image/png"},
                         ContentEncoding="base64")
    url = '{}/{}/{}'.format(s3_client.meta.endpoint_url, bucket_name, key)
    return url
# run
#S event = { "url" : 'https://myatlascms.maps.asu.edu/map/?id=120&s=p&reference=MU#!sbc/' }
#S lambda_handler(event, "context")
#event = { "url" : 'https://myatlascms.maps.asu.edu/map/?id=120&s=p&reference=MU#!sbc/' }
#lambda_handler(event, "context")
