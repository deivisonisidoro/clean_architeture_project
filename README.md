# Clean Architecture Project

This is a Python project that follows the clean architecture, an approach to code organization that aims to separate responsibilities into different layers to achieve a more modular, testable, and scalable code.

## Tools Used

The project utilizes the following tools:

- [Poetry](https://python-poetry.org/): A dependency and virtual environment manager for Python that simplifies package management and project configurations.

- [Flake8](https://flake8.pycqa.org/): A Python static code analysis tool that checks for style and compliance with the guidelines defined in the PEP 8 style guide. It helps maintain clean and readable Python code.

- [Black](https://black.readthedocs.io/): A Python code formatter that follows a "one true style" approach to ensure consistent code style. Black automates code formatting, eliminating discussions about style and maintaining a uniform format.

## Configuration and Usage

Follow the instructions below to configure and use the tools in the project:

### Poetry

1. Make sure you have Poetry installed in your environment. If not, follow the instructions in the official Poetry documentation.

2. Navigate to the project's root directory in the terminal or command prompt.

3. Create and activate a virtual environment with Poetry using the following command:
   `poetry shell`

4. Install the project dependencies, including development dependencies, using the following command:
   `poetry install`

All dependencies, including Flake8 and Black, will be installed automatically.

### Style and Quality Checking

The project is already configured to use Flake8 and Black for style and code quality checking.

- To check the Python code with Flake8, run the following command:
  `poetry run flake8`

Flake8 will check the code for style issues and compliance with the PEP 8 guidelines.

- To automatically format the Python code with Black, run the following command:
  `poetry run black .`

Black will format the code, ensuring a consistent style.

Remember to adapt the above commands according to your project's structure.

Take advantage of Poetry, Flake8, and Black to ensure better organization, style, and code quality in this project.

### Running Django Server and Database Migrations

To start Django, the project follows the clean architecture approach by placing the Django framework in the "infrastructure" folder. This folder represents the infrastructure layer, responsible for handling the implementation details related to frameworks, databases, external services, and other technical components.

By placing Django in the "infrastructure" folder, it separates the technical aspects of the application from the core business logic. This separation allows for easier replacement of the framework if needed and ensures that changes in the underlying technology do not affect the core business logic.

To start Django, follow the steps below based on your operating system:

- **Windows**:

  - Execute the `run_manage.bat` file.
  - Use the following commands to perform database migrations, create a superuser, and start the Django development server:

    ```bash
    poetry run run_manage.bat makemigrations
    poetry run run_manage.bat migrate
    poetry run run_manage.bat createsuperuser
    poetry run run_manage.bat runserver
    ```

  - Ensure that the `run_manage.bat` file has execution permissions.

- **Linux**:

  - Execute the `run_manage.sh` file.
  - Use the following commands to perform database migrations, create a superuser, and start the Django development server:

    ```bash
    poetry run run_manage.sh makemigrations
    poetry run run_manage.sh migrate
    poetry run run_manage.sh createsuperuser
    poetry run run_manage.sh runserver
    ```

  - Remember to give execution permissions to the `run_manage.sh` file using the command `chmod +x run_manage.sh`.

Please note that these commands assume that you are in the project's root directory when executing them. Make sure to adjust the commands according to your project's structure if needed.

Take advantage of Poetry, Flake8, and Black to ensure better organization, style, and code quality in this project.
