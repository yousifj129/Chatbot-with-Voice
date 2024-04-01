# Chatbot with Voice

This repository contains a chatbot application that allows users to interact with the chatbot using speech input and output. The chatbot is powered by the Llama language model, providing intelligent responses to user queries.

## Features

- Speech recognition: Convert user's speech into text input for the chatbot.
- Text-to-speech: Generate speech output for the chatbot's responses.
- Real-time chat history: Display conversation history between the user and the chatbot.
- Graphical user interface (GUI): Intuitive interface for interacting with the chatbot.
- Multithreading: Simultaneous speech recognition and text-to-speech functionality.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/yousifj129/Chatbot-with-Voice.git
   ```

2. Navigate to the project directory:

   ```shell
   cd Chatbot with Voice
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. (Optional) Model Selection:

   - By default, the chatbot uses the Llama language model provided in the repository. If you want to change the model, follow the steps below:
     - Download the desired Llama model in the `.gguf` format.
     - Replace the existing model file (`llama-2-7b-chat.Q4_K_M.gguf`) and place your own model with the path of your downloaded model.

## Usage

1. Run the `chatbot_with_voice.py` script:

   ```shell
   python main.py
   ```

2. Graphical User Interface (GUI):

   - The chatbot application window will appear.
   - Enter text input in the chatbox or click the "Listen" button to provide voice input.
   - The chatbot will generate responses based on the input and display them in the chat history.
   - Scroll the chat history to view the conversation.

3. Exiting the Application:
   - Close the chatbot window.
   - The speech recognition and text-to-speech engines will be stopped automatically.
     Note: the application doesnt close sometimes when the windows is closed, check your task manager and see the ram usage.

## Customization

Feel free to customize the chatbot application to suit your needs. Some possible enhancements include:

- Modifying the GUI design and layout.
- Adding additional features or functionalities.
- Integrating with other APIs or services.
- Implementing different speech recognition or text-to-speech engines.
