# Vetty-Python-API-Technical-Exercise

# Crypto Market Dashboard

## Overview

The **Crypto Market Dashboard** is a simple web application that allows users to fetch cryptocurrency market data using the GeckoTerminal API. The project consists of a Flask backend that serves API requests and a frontend built with HTML, CSS, and JavaScript.

## Features

- Fetch a list of supported networks.
- Retrieve token prices based on network and token address.
- Get detailed information about specific tokens.
- Fetch the top pools for a selected network.
- Simple and interactive user interface.

## Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **API Source:** GeckoTerminal API

## Installation

### Prerequisites

Ensure you have the following installed:

- Python (>=3.6)
- Flask
- Requests library

### Setup Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/Aryan-dsa-coder/Vetty-Python-API-Technical-Exercise.git
   cd Vetty-Python-API-Technical-Exercise
   ```
2. Install dependencies:
   ```sh
   pip install flask requests
   ```
3. Run the Flask server:
   ```sh
   python app.py
   ```
4. Open `http://127.0.0.1:5000/` in your browser.

## API Endpoints

- `GET /networks` - Fetch a list of supported networks.
- `GET /networks/<network>/token_price/<addresses>` - Get token price for a given network and token address.
- `GET /networks/<network>/tokens/<address>` - Get token details.
- `GET /networks/<network>/pools` - Fetch top pools for a network.
- `GET /health` - Check server health.
- `GET /version` - Get the current version of the application.

## Usage

1. Open the web application in your browser.
2. Click buttons to retrieve network, token, and pool data.
3. Enter network names and token addresses when prompted.
4. View the response data displayed on the screen.

## Contributing

Feel free to fork this repository and submit pull requests.

## License

This project is licensed under the MIT License.

## Contact

For questions or suggestions, open an issue or reach out via GitHub.

---



