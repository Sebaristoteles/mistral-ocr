# Mistral OCR Project

This project utilizes the Mistral OCR API to process documents listed in a CSV file. The application reads an API key from an environment file, processes each document, and saves the output in a designated folder. Then another script can be used to create HTML previews of the processed markdown documents.


## Recommended Tech Stack

- Visual Studio Code (VS Code) as the IDE
- Anaconda for managing Python environments
- Python 3.10 or later
- Quarto for compiling markdown files into HTML (optional, but recommended for HTML previews)



## Running the Application

- run python file button in VS Code with the main.py file open, or
- use the terminal to navigate to the project directory and run:
  ```
  python code/main.py
  ```

- without adjustments this will reprocess the examples (if you have an API key)
- to process your own documents, get an API key and create your own input CSV file and the input folder as described below.


## Adjustments for your use

- get the API key from https://mistral.ai/news/mistral-ocr, create .env file in the root directory of the project and add your Mistral OCR API key:
  ```
  API_KEY=your_api_key_here
  ```
- The input CSV must have columns: `input_folder`, `document_name`, and `document_class`
- Input files should be placed in `data/input/<input_folder>/`.
- Output files will be saved in `data/output/<input_folder>/` with the same base name as the input, but with a `.md` extension.  
    - The script extracts the main content from the API response and saves it as a markdown file.
- in code/main.py adjust input_csv = "data/input_examples.csv" to the path of your input CSV file.
- for compiling the markdown files into HTML, adjust the path in code/create_html.py to point to your output directory.



## Setup Instructions

1. **Clone the Repository**
   Clone this repository to your local machine using:
   ```
   git clone <repository-url>
   ```

2. **Prepare Virtual Environment**

- open a terminal (like anaconda prompt) or VS Code terminal (if you have prepated it to use Anaconda)

```
conda create -n mistral-ocr python=3.10
```

- close VS Code and reopen it again (otherwis the installation will go to your main Python environment what is not recommended)
- after reoponing, open on one of the Python files in the code folder
- then, you can click in the right bottom corner of VS Code, select the interpreter of the newly created environment (mistral-ocr)

- then in the terminal, activate the environment and install the dependencies:

```
conda activate mistral-ocr
pip install -r requirements.txt
```

- if you do not see a (base) and then (mistral-ocr) in the terminal line at the beginning, you need to prepare the VS Code terminal to use Anaconda (please use some AI tool to assist you with this). Alternatively, you can use the terminal of Anaconda prompt directly, to install the packages mentioned in the requirements.txt, reopen VS Code and select the Python Interpreter.


3. **Set Up Environment Variables**
   Create a `.env` file in the root directory of the project and add your Mistral OCR API key from https://mistral.ai/news/mistral-ocr:
   ```
   API_KEY=your_api_key_here
   ```

4. **Prepare Input Data**
   Create your `data/input.csv` file to include the documents you want to process. The CSV should have the following columns:
   - `input_folder`: Folder name that resides in `data/input/` containing the documents.
   - `document_name`: The name of the document.

5. **Run the Application**
   Execute the main script by pressing the button in your IDE or start processing the documents from the root directory with:
   ```
   python code/main.py
   ```

6. **Create HTML preview**
   You can create simple HTML previews of the markdown files by running the script `code/create_html.py`. This script will read the markdown files from the output directory and generate HTML files for each document.
   You need to adjust the markdown folder path in the script to point to your output directory.
   
   In addition, you need to have Quarto installed and prepared for the use in VS Code. You can install it from https://quarto.org/docs/get-started/installation.html. After installation, add the Quarto and markdown extensions from the VS Code marketplace to your VS Code setup. You might need to add the Quarto path to your system PATH variable, so that it can be used in the terminal. (Please ask an LLM of your choice to help you with excuting this.)
   
   After the processing is complete, check the `data/output/<name of your input_folder>` folder for the results from the Mistral OCR API.

