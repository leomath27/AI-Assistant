## AI-Assistant

A simple voice-activated assistant that can perform various tasks such as searching Wikipedia, computing answers using Wolfram Alpha, and taking notes.

## Features

- **Speech Recognition**: Listens for voice commands and processes them.
- **Text-to-Speech**: Responds using a natural-sounding voice.
- **Wikipedia Search**: Fetches summaries from Wikipedia articles.
- **Wolfram Alpha Integration**: Computes answers to queries and provides information.
- **Note-Taking**: Allows users to log notes with a timestamp.
- **Web Browsing**: Opens URLs in a web browser.

## Requirements

To run this project, you need to have the following installed:

- Python 3.x
- Libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `wikipedia-api`
  - `wolframalpha`
  - `webbrowser`
    
NOTE: pyttsx3 has not been updated since python version 3.9.0 and recommend using this version or lower

You can install the required libraries using pip:

```bash
pip install SpeechRecognition pyttsx3 wikipedia-api wolframalpha
