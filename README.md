1.	Clone the repository: Start by cloning the repository containing the project onto your local machine. You can do this by running the following command in your terminal: git clone <repository-url>   
2.	Create a virtual environment: Once the repository has been cloned, create a new virtual environment to install the project's dependencies. You can use venv to create a virtual environment: python3 -m venv env   
3.	Activate the virtual environment: Activate the virtual environment using the following command: source env/bin/activate   
4.	Install project dependencies: Install the required dependencies for the project using pip. You can install the dependencies listed in requirements.txt using the following command:  pip install -r requirements.txt   
5.	Create the database: Create a new database for the project by running the following command: python manage.py migrate   
6.	Create a superuser: Create a superuser account that you can use to log into the Django admin interface using the following command: python manage.py createsuperuser   
7.	Launch the development server: Start the development server using the following command: python manage.py runserver   
8.	Test the API: Once the server is running, you can test the API by sending HTTP requests to the appropriate endpoints. You can use a tool like curl or an HTTP client like Postman to test the API. Here are some example endpoints that you can test:
•	POST /images/: Upload a new image to the server.
•	GET /images/: Retrieve a list of all the images uploaded by the current user.
•	GET /images/<image-id>/thumbnail_200/: Retrieve a thumbnail of the specified image with a height of 200 pixels.
•	GET /images/<image-id>/thumbnail_400/: Retrieve a thumbnail of the specified image with a height of 400 pixels.
•	GET /images/<image-id>/original/: Retrieve the original image.

