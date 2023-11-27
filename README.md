


https://github.com/arjunprakash027/Story_Teller/assets/72484657/1c756dd8-9889-420d-a30e-13dbe137a2f0


# Story Teller

Story Teller is a Streamlit application that generates a story based on an input image. It utilizes the Hugging Face Transformers library and the Salesforce BLIP Image Captioning model.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Token](#api-token)
- [Models](#models)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)

## Installation

To install the necessary dependencies, run the following command:

```shell
pip install -r requirements.txt
```

Make sure you have the required dependencies specified in the `requirements.txt` file.

## Usage

To use the application, follow the steps below:

1. Run the Streamlit application by executing the following command:

   ```shell
   streamlit run app.py
   ```

2. Access the application through the provided URL in the console.

3. The application interface will appear with the title "Story Teller" and an instruction to "Upload an image and get a story".

4. Click on the "Upload your file here..." button to select an image file (supported formats: PNG, JPEG, JPG).

5. Once the image is uploaded, it will be displayed on the page.

6. The application will process the uploaded image using the Salesforce BLIP Image Captioning model and generate a textual description of the image.

7. The generated text will then be passed to the Hugging Face API to generate a story based on the text.

8. The application will display the generated story on the page.

9. If any errors occur during the process, an error message will be shown on the page, and you can try again.

## API Token

The application requires an API token from Hugging Face to access the story generation model. To obtain an API token, follow these steps:

1. Sign up or log in to your Hugging Face account at [https://huggingface.co/](https://huggingface.co/).

2. Once logged in, go to your account settings and navigate to the "API token" section.

3. Generate a new API token, copy it, and replace the `"your api key"` placeholder in the `Models` class of `text_model.py` with your actual API token.

## Models

The `Models` class in `text_model.py` encapsulates the functionality of the application. It contains the following methods:

- `__init__()`:
    - Initializes the class and sets the API token and model ID.

- `img2text(url)`:
    - Takes an image URL as input and uses the Salesforce BLIP Image Captioning model to convert the image into text. It returns the generated text.

- `story(payload)`:
    - Takes a payload as input, which contains the generated text, and sends a request to the Hugging Face API to generate a story based on the text. It returns the generated story.

- `chain(payload, num=0)`:
    - This method acts as a recursive function that generates a chain of stories. It takes a payload as input, which initially contains the generated text. It recursively calls the `story()` method and updates the payload until the desired number of stories (50 in this case) is generated. The progress bar is also updated accordingly.

## Running the Application
If you are curious and want to just try the backend models
execute the following command:

```shell
python text_model.py
```

Make sure you have the required dependencies installed, as mentioned in the installation section.

## Contributing

Contributions to the Story Teller application are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
