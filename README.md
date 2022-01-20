# shopify challenge
submission for shopify intern challenge question.


# requirements
dependencies: django, pytest-django, pytest-factoryboy, pytest-factoryboy, pyteset-selenium, elasticsearch, pillow
chrome webdriver: must have webdriver for your chrome version (for testing with selenium) (can find in chrome -> settings -> about chrome)

# about the project
Image gallery built using a django server. Has sorting functionality for images, additional images can be uploaded from Django admin panel.

# features

Users can sort the images by different tags. the ability to add images from the client is also available. images are currently stored locally but could be migrated to an s3 bucket if neccessary.
application is also built with testing in mind, with some selenium tests for the admin panel configured. This testing can be expanded in the future.

# How to run
Navigate to the root folder of the project (folder containing manage.py), and enter 'python manage.py runserver' to run the development server.
In your web browser of choice, go to http://127.0.0.1:8000/ to access the project demo.
