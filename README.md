# Cool Twilio Project

This repository contains the source code for a project that uses Twilio and OpenAI to build a food recognition chatbot. It also give the nutritional information about the food.

## Prerequisites

* Twilio Account and Phone Number
* OpenAI Account
* USDA API Key
* Google Cloud Account

## Setup

1. Clone the repository and cd into it
2. Create a `.env` file and add your Twilio and OpenAI credentials
    * Twilio account SID, auth token and phone number
    * OpenAI API key
    * USDA API key
3. Download the Google Cloud Vision API JSON file as cloud.json
4. Create a virtual environment and activate it
5. Install the requirements with `pip install -r requirements.txt`
6. Run the app with `python app.py`
7. In another terminal, run `ngrok http 8080`
8. In Twilio console, add the URL, "https://5bad813c2718.ngrok.io/summary" as a Webhook when “A Message Comes In”.

## Usage

Once the app is running, you can send a picture of a food item to the Twilio number and it will respond with the nutritional information about the food