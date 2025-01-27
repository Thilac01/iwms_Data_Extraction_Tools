# iwms_Data_Extraction_Tools

This repository contains tools for extracting data using Python. Follow the steps below to set up and run the project.

## Prerequisites

Make sure your system has the following installed:

1. **Git**: If Git is not installed, [download and install Git](https://git-scm.com/).
2. **Python**: Install Python from the [official Python website](https://www.python.org/downloads/).
3. **VS Code**: Download and install Visual Studio Code from [here](https://code.visualstudio.com/).

## Setup Instructions

### Step 1: Clone the Repository

1. Create a folder where you want to store the project.
2. Open the folder, click on the address bar at the top, type `cmd`, and press Enter.
3. In the command prompt, type the following command to clone the repository:
   ```bash
   git clone https://github.com/Thilac01/iwms_Data_Extraction_Tools
   ```

### Step 2: Open the Project in VS Code

1. Navigate to the `iwms_Data_Extraction_Tools` folder.
2. Click on the address bar at the top, type `cmd`, and press Enter.
3. In the command prompt, type the following command to open the project in VS Code:
   ```bash
   code .
   ```

### Step 3: Install Required Packages

1. Open the terminal in VS Code by selecting `Terminal > New Terminal` from the menu.
2. In the terminal, type the following command to install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Step 4: Configure SSL Connection

1. Go to your Google Account security settings and enable "App Passwords."
   - Generate an app password for SSL connection.
   - Copy the generated password.
2. Open the `main.py` file in the project.
3. Replace the placeholder for the SSL connection password with the password you generated.

### Step 5: Run the Project

1. After completing the setup, run the following command in the terminal to execute the script:
   ```bash
   python main.py
   ```

## Notes

- Ensure all the dependencies in `requirements.txt` are installed successfully.
- If you encounter any issues during setup or execution, double-check your Python and VS Code installations.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
