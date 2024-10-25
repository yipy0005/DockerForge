
# DockerForge: A User-Friendly Dockerfile Generator

Welcome to **DockerForge**, a simple and intuitive web-based tool designed to help you generate Dockerfiles without any prior experience with Docker. This app is perfect for beginners who want to create Docker containers quickly and easily.

## 📖 Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Setting Up the Environment](#setting-up-the-environment)
4. [Running the Application](#running-the-application)
5. [Contributing](#contributing)
6. [Issues](#issues)

## 📝 Introduction
DockerForge is a Streamlit-based application that guides you step-by-step to create a customized Dockerfile. You can select a base image, add system dependencies, choose programming languages, set environment variables, and define entrypoints—all with a few clicks.

## 🚀 Getting Started
To get the DockerForge app running on your local machine, follow the steps below. These instructions are geared towards beginners, so no prior knowledge is needed!

### Prerequisites
- Make sure you have [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) installed on your system. If not, follow the instructions on the Conda website to install it.

## 🛠 Setting Up the Environment

To ensure that you have all the necessary packages and dependencies, we will use a `conda` environment. Follow the steps below:

### Step 1: Create a Conda Environment
Open your terminal (or Anaconda Prompt on Windows) and navigate to the directory where your project files are located. Use the following command to create a new Conda environment:

```bash
conda env create -f environment.yaml
```

This command will read the `environment.yaml` file and set up a new environment named `dockerforge` with all the required dependencies.

### Step 2: Activate the Environment
Once the environment is created, activate it using the following command:

```bash
conda activate dockerforge
```

### Step 3: Install Additional Dependencies (if needed)
If you need to install any additional Python packages, you can do so using:

```bash
pip install <package-name>
```

## 🎮 Running the Application

Now that the environment is set up, you can run the DockerForge app using Streamlit:

1. Make sure you are in the correct directory where the `DockerForge.py` file is located.
2. Run the following command:

```bash
streamlit run DockerForge.py
```

3. A new browser window should open automatically. If not, open your web browser and navigate to the address displayed in the terminal (typically `http://localhost:8501`).

## 🤝 Contributing
If you want to contribute to the project, feel free to fork the repository and submit a pull request. Contributions, suggestions, and improvements are always welcome!

## 🐞 Issues
If you encounter any problems or have questions, please [raise an issue](https://github.com/your-repository-name/issues) in the GitHub repository. We are here to help!

Happy containerizing! 🚢
