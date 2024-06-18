# Face Authentication App

This project is a Flask-based web application that uses facial recognition for user authentication. Users can register by providing their username, password, email, phone number, and a photo taken from their laptop camera. The application stores user data in a MongoDB database and authenticates users using facial recognition.

## Features

- User Registration with photo capture
- User Login with facial authentication
- Data stored in MongoDB
- Dockerized for easy deployment

## Technologies Used

- Python
- Flask
- MongoDB
- Docker
- deepface (for facial recognition)
- OpenCV (for handling camera input)

## Directory Structure

face_auth_app/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
├── README.md
├── templates/
│ ├── landing.html
│ ├── register.html
│ └── login.html
└── static/
├── styles.css
└── background.jpg


## Setup and Installation

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/face_auth_app.git
    cd face_auth_app
    ```

2. **Build and run the Docker containers**:
    ```sh
    docker-compose up --build
    ```

3. **Access the application**:
    Open your web browser and go to `http://localhost:5000/`.

### Manual Setup (without Docker)

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/face_auth_app.git
    cd face_auth_app
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```sh
    flask run
    ```

5. **Access the application**:
    Open your web browser and go to `http://localhost:5000/`.

## Usage

### Register

1. Go to the [Register Page](http://localhost:5000/register).
2. Fill in the username, password, email, and phone number.
3. Take a photo using your laptop camera.
4. Submit the form.

### Login

1. Go to the [Login Page](http://localhost:5000/login).
2. Fill in the username and password.
3. Authenticate using the facial recognition feature.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [deepface](https://github.com/serengil/deepface)
- [OpenCV](https://opencv.org/)
- [Docker](https://www.docker.com/)
- [MongoDB](https://www.mongodb.com/)
