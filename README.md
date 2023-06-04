# Chatbot with OpenAI and Line Messaging API

This is a chatbot application built using Flask, OpenAI, and Line Messaging API. It leverages OpenAI's text completion model to generate responses to user queries. The Line Messaging API is used to handle incoming messages and send replies to users.

## Prerequisites

Before running the application, make sure you have the following:

- Python 3.7 or higher installed
- OpenAI API key and organization key
- Line Messaging API credentials (access token and channel secret)
- A Line developer account

## Installation

1. Clone the repository: ```git clone <repository-url>```

2. Install the required dependencies: ```pip install -r requirements.txt```

3. Create a `.env` file and fill in the required credentials:
ORG_KEY = \<your-openai-organization-key>  
OPENAI_API_KEY = \<your-openai-api-key>
LINE_ACCESS_TOKEN = \<your-line-access-token>
CHANNEL_SECRET = \<your-channel-secret>

## Usage

1. Run the Flask server:  ```python app.py```

2. Make sure the server is up and running.

3. Set up the Line Messaging API webhook:

    - In your Line developer account, configure the webhook URL to point to your server's `/webhook` route.
    - Make sure the server is accessible from the internet.

4. Start chatting with the chatbot:

    - Send a message to your Line account that is connected to the chatbot.
    - The chatbot will reply with a generated response using the OpenAI text completion model.

## Customizing the Chatbot

- You can customize the behavior of the chatbot by modifying the `text_completion` function in `app.py`. This function defines the parameters for the OpenAI API request and processes the response.

## Contributing

Contributions are welcome! If you find any issues or want to add new features to the chatbot, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions, feel free to reach out to the project maintainers:

- [Walter Hsieh](mailto:dynamic.walter@gmail.com)
- [OpenAI](https://help.openai.com/en/)
- [Line Developers](https://developers.line.biz/en/)