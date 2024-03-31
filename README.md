````
# Chatbot with Voice

This repository contains a chatbot application that allows users to interact with the chatbot using speech input and output. The chatbot is powered by the Llama language model, providing intelligent responses to user queries.

![Chatbot with Voice](chatbot_with_voice.png)

## Features

- Speech recognition: Convert user's speech into text input for the chatbot.
- Text-to-speech: Generate speech output for the chatbot's responses.
- Real-time chat history: Display conversation history between the user and the chatbot.
- Graphical user interface (GUI): Intuitive interface for interacting with the chatbot.
- Multithreading: Simultaneous speech recognition and text-to-speech functionality.

## Requirements

- Python 3.7 or above
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/chatbot-with-voice.git
````

2. Navigate to the project directory:

   ```shell
   cd chatbot-with-voice
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. (Optional) Model Selection:

   - By default, the chatbot uses the Llama language model provided in the repository. If you want to change the model, follow the steps below:
     - Download the desired Llama model in the `.gguf` format.
     - Replace the existing model file (`llama-2-7b-chat.Q4_K_M.gguf`) in the `AI` directory with your downloaded model.
     - Make sure the new model file has the same name and file extension.
     - Update the `LLM` initialization code in `chatbot_with_voice.py` to include the correct model path.

## Usage

1. Run the `chatbot_with_voice.py` script:

   ```shell
   python chatbot_with_voice.py
   ```

2. Graphical User Interface (GUI):

   - The chatbot application window will appear.
   - Enter text input in the chatbox or click the "Listen" button to provide voice input.
   - The chatbot will generate responses based on the input and display them in the chat history.
   - Scroll the chat history to view the conversation.

3. Exiting the Application:
   - Close the chatbot window or press `Ctrl+C` in the terminal to stop the application.
   - The speech recognition and text-to-speech engines will be stopped automatically.

## Customization

Feel free to customize the chatbot application to suit your needs. Some possible enhancements include:

- Modifying the GUI design and layout.
- Adding additional features or functionalities.
- Integrating with other APIs or services.
- Implementing different speech recognition or text-to-speech engines.

## License

This project is licensed under the [MIT License](LICENSE).

```

You can save this content in a file named `README.md` in the root directory of your project. Make sure to update the file paths, model information, and any other relevant details specific to your project.
```
