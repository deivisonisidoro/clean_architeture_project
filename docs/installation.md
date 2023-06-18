# Installation

This section provides instructions on how to set up and install the Clean Architecture Project.

## Prerequisites

Before you begin the installation process, ensure that you have the following prerequisites:

- Python 3.x: Make sure you have Python 3.x installed on your system. You can check the Python version by running the following command:

  ```bash
  python --version
  ```

- Poetry: The Clean Architecture Project utilizes Poetry for dependency management. If you don't have Poetry installed, you can install it by following the official Poetry documentation

## Step 1: Clone the Repository

Start by cloning the Clean Architecture Project repository from GitHub. Open your terminal or command prompt and run the following command:

```bash
git clone https://github.com/deivisonisidoro/clean_architeture_project.git
```

This will create a local copy of the project on your machine.

## Step 2: Install Dependencies

Navigate to the project's root directory in the terminal or command prompt:

```bash
cd clean-architecture-project
```

Once you are inside the project's root directory, create and activate a virtual environment using Poetry:

```bash
poetry shell
```

Next, install the project dependencies, including development dependencies, by running the following command:

```bash
poetry install
```

This will automatically install all the required packages and set up the project environment.

## Step 3: Style and Quality Checking

The project is already configured to use Flake8 and Black for style and code quality checking.

To check the Python code with Flake8, run the following command:

```bash
poetry run flake8
```

Flake8 will check the code for style issues and compliance with the PEP 8 guidelines.

To automatically format the Python code with Black, run the following command:

```bash
poetry run black .
```

Black will format the code, ensuring a consistent style.

Remember to adapt the above commands according to your project's structure.

## Step 4: Running Django Server and Database Migrations

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
    poetry run ./run_manage.sh makemigrations
    poetry run ./run_manage.sh migrate
    poetry run ./run_manage.sh createsuperuser
    poetry run ./run_manage.sh runserver
    ```

  - Remember to give execution permissions to the `run_manage.sh` file using the command `chmod +x run_manage.sh`.

Please note that these commands assume that you are in the project's root directory when executing them. Make sure to adjust the commands according to your project's structure if needed.

Thank you for installing the Clean Architecture Project! You are now ready to start working with it.
