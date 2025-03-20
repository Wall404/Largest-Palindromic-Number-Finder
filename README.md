# Largest Palindromic Number Finder

This Python application finds the largest palindromic number strictly between two given numbers.

## Features

- Finds the largest palindromic number between two numbers (exclusive).
- Includes unit tests to ensure the correctness of the core functionality.
- Can be run directly or within a Docker container.

## Requirements

- Python 3.x
- `pipenv` for managing dependencies
- Docker and Docker Compose (optional, for containerization)

## Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/Largest-Palindromic-Number-Finder.git
cd Largest-Palindromic-Number-Finder
```

2. Install Dependencies Using pipenv

pipenv is used for managing project dependencies. You need to install pipenv if you haven't already:

    Install pipenv globally (if you don't have it):

pip install pipenv

Install the project's dependencies:

    pipenv install

This will create a virtual environment and install the necessary dependencies.

4. Running the Application

Once you have the environment set up, you can run the application. The application will prompt you to enter the starting and ending numbers, and it will return the largest palindromic number strictly between them.

Run the application with:

```bash
python app.py
```

Example:

```code
Enter the starting number: 100
Enter the ending number: 200
The largest palindromic number between 100 and 200 is: 191
```

Docker Setup (Optional)

If you prefer to run the application inside a Docker container, you can use the provided Dockerfile and docker-compose.yml files.
1. Build the Docker Image

To build the Docker image, run the following command:

```bash
docker-compose build
```

2. Running the Application in Docker

After building the image, you can start the application using Docker Compose:

```bash
docker-compose up
```

This will run the application inside a container, and you will be able to interact with it as you would locally.
Stopping the Docker Container

To stop the container, press CTRL + C or use:

```bash
docker-compose down
```

Testing

The application includes unit tests to validate the core functionality. To run the tests:
1. Activate the Virtual Environment (If Using pipenv)

```bash
pipenv shell
```

2. Run Unit Tests

To run the tests, use the following command:

```bash
python -m unittest test_app.py
```

This will execute the unit tests and validate the core functionality of the application.
3. Test Output

You should see output similar to this if the tests pass:

```bash
....
----------------------------------------------------------------------
Ran 4 tests in 0.004s

OK
```

Code Overview
app.py

This file contains the core functionality of the application. It defines the function largest_palindrome_in_range() that finds the largest palindromic number strictly between two numbers. The function also includes a helper function is_palindrome() that checks whether a number is a palindrome.
test_app.py

This file contains unit tests that verify the core functionality of the application. It uses the unittest module to test different ranges and ensure that the function largest_palindrome_in_range() behaves as expected.
Dockerfile

This file sets up the application in a Docker container. It defines the image based on python:3.9-slim, installs dependencies via pipenv, and runs the application inside the container.
docker-compose.yml

This file defines the services used by Docker Compose. It specifies how the Docker container is built and run, as well as the ports and volumes to be used.
requirements.txt (Optional)

Although the project primarily uses pipenv to manage dependencies, you may also have a requirements.txt file in case you want to use pip to install dependencies directly.
Project Structure

Largest-Palindromic-Number-Finder/
├── app.py                # Main application code
├── test_app.py           # Unit tests
├── Dockerfile            # Docker configuration to run the app
├── docker-compose.yml    # Docker Compose configuration
├── Pipfile               # Pipenv file to manage dependencies
├── Pipfile.lock          # Pipenv lock file to ensure reproducible builds
├── requirements.txt      # Optional, for pip-based installs
└── README.md             # Project documentation