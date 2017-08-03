# URL-To-Image-Converter-AWS-LAMBDA

This project takes any URL and takes the screenshot of the webpage and loads into s3 bucket and gives it as result.

This can be used in scenarios where you need to display an image as result from alexa in the alexa cards app.

This is an AWS Lambda deployment package.

PREREQ:
======
S3- BUCKET NAME: alexa-image-store
BUCKET-SUBFOLDER-NAME: alexa-location-annotator

API-DOCS:
========
REQUEST BODY
{
  "url" : "https://myatlascms.maps.asu.edu/map/?id=120&s=p&reference=MU#!sbc/",
  "max_page_load_time" : 4,
  "window_size_width" (OPTIONAL) : 1024,
  "window_size_height" (OPTIONAL) : 768
}



How is packaging done ?
=======================

phantomjs/
selenium/
selenium-3.4.3.dist-info/
lambda_function.py



