# Cinema Management System

This Python script implements a basic cinema management system using MySQL database for storage. It provides functionalities for user registration, login, movie management, seating arrangement creation, seat booking, and more.

## Requirements

- Python 3.x
- MySQL Server
- MySQL Connector/Python

## Installation

1. Install Python 3.x from [Python Official Website](https://www.python.org/downloads/)
2. Install MySQL Server from [MySQL Official Website](https://dev.mysql.com/downloads/mysql/)
3. Install MySQL Connector/Python using pip:

    ```bash
    pip install mysql-connector-python
    ```

## Configuration

1. Create a MySQL database named `cinema`.
2. Modify the database connection parameters (`host`, `password`, `user`, `database`) in the script according to your MySQL configuration.

## Usage

1. Run the script using Python:

    ```bash
    python cinema_management.py
    ```

2. Follow the on-screen menu to perform various operations like user registration, login, movie management, seating arrangement creation, seat booking, etc.

## Functionality

- **User Registration & Login**: Users can register with a username and automatically generated password. Registered users can log in using their credentials.
- **Movie Management**: Admin users can add and delete movies along with details like name, duration, rating, and genre.
- **Seating Arrangement**: Admin users can create a seating arrangement for the theater, specifying the number of rows and columns.
- **Seat Booking**: Users can book available seats in the theater.
- **Display Seats**: Users can view the current seating arrangement and the status of each seat (booked or available).
- **Edit Seats**: Admin users can edit the booking status of seats.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License
This project is non-licensed.
