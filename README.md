# AirBnB Clone Project

Welcome to the AirBnB Clone Project! This project aims to build a simplified version of the AirBnB website by covering fundamental concepts of higher-level programming. The project will be developed step by step, focusing on different aspects of web development, including data manipulation, front-end design, database storage, and API implementation.

## Project Steps

The AirBnB clone project is divided into multiple steps, each corresponding to a specific concept. These steps include:

1. **The Console**: Creating a command interpreter to manipulate data and validate the storage engine's functionality.

2. **Web Static**: Learning HTML/CSS, creating static HTML files, and implementing basic templates.

3. **MySQL Storage**: Replacing file storage with database storage and using an Object-Relational Mapping (ORM) library to map models to database tables.

4. **Web Framework and Templating**: Building a web server in Python, making static HTML files dynamic, and rendering data from the database.

5. **RESTful API**: Creating a RESTful API to expose data via a JSON web interface, allowing users to manipulate objects.

6. **Web Dynamic**: Learning JQuery, loading objects using the RESTful API, and enhancing the user experience.

## Project Structure

- The `models` directory contains classes representing various objects in the application.
- The `tests` directory contains unit tests for the project.
- The `console.py` file serves as the entry point for the command interpreter.
- The `models/base_model.py` file defines the base class for all models, including common attributes and methods.

## Storage System

The project introduces a storage system that separates the storage and retrieval of objects. This separation allows easy switching between storage types (e.g., file and database) without modifying the codebase.

## Data Persistence

Objects are serialized to JSON format and stored in files on disk.

## Contributions

Contributions to the project are highly encouraged! You can contribute by following the provided code style guidelines, writing thorough unit tests, and enhancing the existing codebase. Your contributions will help improve the functionality and performance of the application.
