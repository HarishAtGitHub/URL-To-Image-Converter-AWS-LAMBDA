# URL-To-Image-Converter-AWS-LAMBDA

This project takes any URL and takes the screenshot of the webpage and loads into s3 bucket and gives it as result.

This can be used in scenarios where you need to display an image as result from alexa in the alexa cards app.

This is an AWS Lambda deployment package.

PREREQ:
======

S3- BUCKET NAME: alexa-image-store

Access to read the object from s3 : public-read permission so that image url can be made public

API-DOCS:
========

REQUEST BODY
```js
{
  "url" : "https://myatlascms.maps.asu.edu/map/?id=120&s=p&reference=MU#!sbc/",
  "max_page_load_time" : 4,
  "window_size_width" (OPTIONAL) : 1024,
  "window_size_height" (OPTIONAL) : 768
}
```

For example with the above values and URL, the s3-image will look like below

![img](https://user-images.githubusercontent.com/5524260/28939227-749ac728-7845-11e7-9988-aa38de521cd0.png)



How is packaging done ?
=======================

Just zip the following folders and files and give the lambda name as lambda_function.handler

phantomjs/

selenium/

selenium-3.4.3.dist-info/

lambda_function.py



