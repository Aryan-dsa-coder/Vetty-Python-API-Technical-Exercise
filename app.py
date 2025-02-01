from flask import Flask, request, jsonify, send_from_directory
import os
import requests

app = Flask(__name__)

GECKOTERMINAL_API_URL = "https://api.geckoterminal.com/api/v2"

# Serve the HTML file
@app.route("/")
def serve_html():
    return send_from_directory(os.getcwd(), "index.html")

# API to get the list of networks
@app.route("/networks", methods=["GET"])
def list_networks():
    response = requests.get(f"{GECKOTERMINAL_API_URL}/networks")
    return jsonify(response.json())

# API to get token price
@app.route("/networks/<network>/token_price/<addresses>", methods=["GET"])
def get_token_price(network, addresses):
    response = requests.get(f"{GECKOTERMINAL_API_URL}/simple/networks/{network}/token_price/{addresses}")
    return jsonify(response.json())

# API to get token information
@app.route("/networks/<network>/tokens/<address>", methods=["GET"])
def get_token_info(network, address):
    response = requests.get(f"{GECKOTERMINAL_API_URL}/networks/{network}/tokens/{address}")
    return jsonify(response.json())

# API to get top pools
@app.route("/networks/<network>/pools", methods=["GET"])
def get_top_pools(network):
    response = requests.get(f"{GECKOTERMINAL_API_URL}/networks/{network}/pools")
    return jsonify(response.json())

# Health check route
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"})

# Version info route
@app.route("/version", methods=["GET"])
def version_info():
    return jsonify({"version": "1.0"})

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)
