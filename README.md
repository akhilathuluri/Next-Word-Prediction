# Next-Word-Prediction

## Overview

The Next Word Text Generation App is a Flask-based web application that uses a pre-trained model to generate text based on user input. This documentation provides information on the application's structure, usage, and dependencies.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [Acknowledgments](#Acknowledgments)
- [Outputs](#Outputs)
- [License](#license)

## Installation

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- Pip (Python package installer)

### Steps

1. Clone the repository:
```
git clone https://github.com/akhilathuluri/Next-Word-Prediction.git
```
2. Navigate to the project directory:
```
cd next-word-app
```
3. Create a virtual environment (optional but recommended):
```
python -m venv venv
```
4. Activate the virtual environment:
   - On Windows:
     ```
      .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Install dependencies:
```
pip install -r requirements.txt
```

### Usage
1. Run the Flask application:
```
python app.py
```
2. Open your browser and navigate to http://localhost:5000.
3. Use the input form to enter text and specify the number of words to generate.
4. Click the "Generate" button to see the generated text.

### Project Structure
The project follows the following structure:

- `app.py`: Flask application script.
- `static/`: Static files (CSS, JS, images).
- `templates/`: HTML templates.
- `next-word.h5`: Pre-trained model file.
- `tokenizer.pkl`: Tokenizer file.

### Dependencies

- Flask
- TensorFlow
- NumPy
For a complete list of dependencies, refer to the `requirements.txt` file.

### Contributing
If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Create a pull request.

### Generating Text
1. Enter a starting text in the "Enter Your Text" field.
2. Specify the number of words to generate.
3. Click the "Generate" button.
4. The generated text will be displayed below the input form.


### Acknowledgments
1. This project was developed as part of MRU CSE App Development Project.

### Outputs
1. ![image](https://github.com/akhilathuluri/Next-Word-Prediction/assets/89147384/8ab3167d-b1ec-41f2-9a28-8bcfff27f5e7)
2. ![image](https://github.com/akhilathuluri/Next-Word-Prediction/assets/89147384/f3c555bc-0bf6-4bed-b638-418f33b927b2)

### License
This project is licensed under the MIT License - see the LICENSE file for details.
