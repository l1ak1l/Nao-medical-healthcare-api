# Medical Translation API

## Description

The Medical Translation API is a FastAPI application designed to translate medical texts between different languages. It utilizes advanced transcription and translation services to provide accurate medical translations while preserving clinical context and terminology.

## Features

- Transcribes audio files to text.
- Translates medical texts between specified source and target languages.
- Generates audio from translated text using text-to-speech services.
- Supports multiple languages and maintains clinical context.

## Requirements

- Python 3.8 or higher
- FastAPI
- Uvicorn
- Pydantic
- Groq API
- Eleven Labs API

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/l1ak1l/medical-translation-api.git
   cd medical-translation-api
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   Create a `.env` file in the root directory of the project and add your API keys:

   ```plaintext
   GROQ_API_KEY=your_groq_api_key
   ELEVENLABS_API_KEY=your_elevenlabs_api_key
   ```

## Running the Project

1. **Start the FastAPI server**:

   You can run the application using Uvicorn. Make sure you are in the project directory and your virtual environment is activated (if you created one):

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 2000 --reload
   ```

   - `main:app` refers to the `app` instance in the `main.py` file.
   - The `--reload` flag enables auto-reload for development.

2. **Access the API**:

   Open your browser and navigate to `http://localhost:2000/docs` to access the interactive API documentation provided by FastAPI. Here, you can test the endpoints directly.

## Testing the API

To test the API, you can use the provided test script:

1. **Run the test script**:

   ```bash
   python test/test.py --api-url http://localhost:2000 --audio-path path_to_your_audio_file.mp3 --source-lang en-US --target-lang hi-IN --output-dir test
   ```

   Replace `path_to_your_audio_file.mp3` with the path to an actual audio file you want to test.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.