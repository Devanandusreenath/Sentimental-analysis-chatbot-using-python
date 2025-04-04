# Sentiment Analysis Chatbot

## Overview
This project is a chatbot that responds to user input based on sentiment analysis. It utilizes TextBlob for sentiment analysis and generates responses accordingly. The chatbot is implemented in both a command-line interface (CLI) and a Flask-based web application.

## Features
- **Sentiment Analysis:** Determines whether user input is Positive, Negative, or Neutral.
- **Chatbot Response:** Selects a response based on the sentiment.
- **Command-Line Interface (CLI):** Runs in a terminal for quick testing.
- **Web Interface:** Built using Flask for real-time interaction.

## Technologies Used
- **Backend:** Flask
- **Natural Language Processing:** TextBlob
- **Machine Learning Models (Optional):** Hugging Face's `microsoft/DialoGPT-medium`
- **Libraries:**
  - `Flask`: For the web server
  - `TextBlob`: For sentiment analysis
  - `random`: For selecting random responses

## Installation
### Prerequisites
- Python installed (version 3.7 or later)
- `pip` installed

### Steps to Run the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/sentiment-chatbot.git
   cd sentiment-chatbot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the command-line chatbot:
   ```sh
   python chatbot.py
   ```
4. Run the Flask-based chatbot:
   ```sh
   python app.py
   ```
5. Open `http://127.0.0.1:5000/` in your browser.

## Usage
### CLI Chatbot
1. Run the script: `python chatbot.py`
2. Type a message to chat.
3. Type "quit" to exit.

### Web Chatbot
1. Open the browser and navigate to `http://127.0.0.1:5000/`
2. Type a message and send it.
3. The chatbot will respond based on sentiment.

## Folder Structure
```
sentiment-chatbot/
│── static/
│── templates/
│   └── chatbot.html   # HTML template for the web UI
│── app.py             # Flask application
│── chatbot.py         # CLI chatbot script
│── textana.py         # Sentiment analysis module
│── userrespond.py     # Response generator
│── responses.py       # Predefined responses
│── requirements.txt   # Required dependencies
```
