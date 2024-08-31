Here's a simple README content template for your Flask-based meme website:

---

# Meme Viewer

This is a simple Flask web application that displays a new meme from the [Meme API](https://meme-api.com/gimme) every few tens of seconds.

## Features

- Fetches random memes from the Meme API.
- Automatically refreshes the displayed meme every few tens of seconds.
- Built with Flask for the backend, HTML and CSS for the frontend.

## Requirements

- Python 3.x
- Flask
- Requests

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/xvlblo22/meme-viewer.git
   cd meme-viewer
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask app:

   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000` to view the application.

## File Structure

meme-viewer/
│
├── main.py # The main Flask application
├── templates/
│ └── index.html # The HTML template for displaying memes
├── static/
│ └── styles.css # The CSS file for styling the webpage
├── requirements.txt # List of dependencies
└── README.md # This file

## API

This application uses the [Meme API](https://meme-api.com/gimme) to fetch memes. The API is provided by the [Meme API project](https://github.com/D3vd/Meme_Api), created and maintained by [D3vd](https://github.com/D3vd).

## License

This project is licensed under the MIT License
