import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import ttk
from threading import Thread
from llama_cpp import Llama

LLM = Llama(
    model_path="../AI/llama-2-7b-chat.Q4_K_M.gguf", n_threads=2, n_ctx=2048, n_batch=2048,n_gpu_layers=-1,seed=1337
    )

# create a text prompt

# generate a response (takes several seconds)



# Global variables
chat_history = []
current_input = "blank"

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 135)
engine


def process_input(currentText):
    global current_input, chat_history

    # Get the current input and add it to the chat history
    input_text = currentText

    # Clear the input field
    input_entry.delete(0, tk.END)

    # Display the user's input in the chat history
    chat_history_text.config(state=tk.NORMAL)
    chat_history_text.insert(tk.END, "You: " + input_text + "\n")
    chat_history_text.config(state=tk.DISABLED)
    messages = [
        {
            "role": "system",
            "content": "you are a helpful assistant, help the user, keep it all short (1 line maximum)"+
            f"\nfor context, here is the history: {chat_history}"
        },
        {
            "role": "user",
            "content": input_text
        }
    ]
    output = LLM.create_chat_completion(messages)
    print(output)
    # Process the input and get the chatbot's response
    response = output["choices"][0]["message"]["content"]
    chat_history.append(("user: ", input_text))
    # Add the chatbot's response to the chat history
    chat_history.append(("you: ", response))
    # Display the chatbot's response in the chat history
    chat_history_text.config(state=tk.NORMAL)
    chat_history_text.insert(tk.END, "Chatbot: " + response + "\n")
    chat_history_text.config(state=tk.DISABLED)
    # Speak the chatbot's response
    # engine.say(response)
    # engine.runAndWait()

    


def listen_microphone():
    global current_input

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                # Listen for the user's input
                audio = recognizer.listen(source)
                print("gonna rec")
                # Recognize the speech
                text = recognizer.recognize_google(audio)
                print("error?")
                # Set the current input to the recognized text
                current_input = text

                # Process the input
                process_input(current_input)

            except sr.UnknownValueError:
                pass


def start_listening():
    # Start a new thread for listening to the microphone
    Thread(target=listen_microphone).start()

def on_window_close():
    # Stop the speech recognition and text-to-speech engines
    recognizer.__exit__()
    engine.stop()
    root.destroy()
    print("window closed")
    # Stop the AI model
    LLM.__exit__()
    exit(LLM)
    # Close the application window
    print("LLM closed")
    exit()

def on_closing():
    print("closing")
    on_window_close()
# Create the GUI
root = tk.Tk()
root.title("Chatbot with Voice")
root.geometry("1280x720")

# Create a frame for the chat history
chat_history_frame = ttk.Frame(root)
chat_history_frame.pack(pady=10)

# Create a scrollable text widget for the chat history
chat_history_text = tk.Text(chat_history_frame, wrap=tk.WORD, state=tk.DISABLED)
chat_history_text.pack(side=tk.LEFT, fill=tk.BOTH)

# Create a scrollbar for the chat history
chat_history_scrollbar = ttk.Scrollbar(chat_history_frame, command=chat_history_text.yview)
chat_history_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_history_text.config(yscrollcommand=chat_history_scrollbar.set)

# Create a frame for the input field and button
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

# Create an entry field for the user's input
input_entry = ttk.Entry(input_frame)
input_entry.pack(side=tk.LEFT)

# Create a button to submit the user's input
submit_button = ttk.Button(input_frame, text="Submit", command=lambda: Thread(process_input(input_entry.get())).start())
submit_button.pack(side=tk.LEFT, padx=10)

# Create a button to start listening to the microphone
listen_button = ttk.Button(root, text="Listen", command=start_listening)
listen_button.pack(pady=10)
# Start the GUI event loop
root.mainloop()

