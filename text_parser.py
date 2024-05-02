import re
import random
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
import os
import yaml

def load_gestures():
    df = pd.read_csv('gestures_dataset/gestures.csv', usecols=['Category', 'Gesture', 'Weight'])

    global mappings
    mappings = {}

    # Group by the 'Category' and aggregate lists of 'Gesture' and 'Weight'
    for category, group in df.groupby('Category'):
        gestures = group['Gesture'].tolist()
        weights = group['Weight'].tolist()
        mappings[category] = (gestures, weights)   
    return mappings

def tokenize_sentences(text):
    # Download the Punkt tokenizer models (only needs to be done once)
    # nltk.download('punkt')

    # Use NLTK's sent_tokenize to split text into sentences
    sentences = sent_tokenize(text)
    return sentences

def get_random_choice(gesture):
    global speech_controls, default_contextual
    pause = 1000
    speed = 80  # between 70-80 for an effective communication
    volume = 100 # maximum volume; range 10-100
    
    # We need Nao to hesitate one second after starting each gesture for an effective communication
    pause_marker =  f"\\pau={pause}\\"
    
    if speech_controls:   
        # Slow down Nao's speed and boost its volume for an effective communication 
        speech_controls_markers = f"\\rspd={speed}\\ \\vol={volume}\\"

    if not default_contextual:
        mode_marker = "^mode(disabled)"
    else:
        mode_marker = ""
    if gesture in mappings:
        choices, weights = mappings[gesture]
        selected_choice = random.choices(choices, weights)[0]
        return f"{speech_controls_markers} ^start(animations/Stand/Gestures/{selected_choice}) {pause_marker} {mode_marker}"
    
def replace_bracket_contents(text):
    pattern = r'\{([^}]+)\}'
    
    def replacement(match):
        gesture = match.group(1)  # Extract the gesture within the braces
        return get_random_choice(gesture)

    # Replace all occurrences in the text using the replacement function
    replaced_text = re.sub(pattern, replacement, text)
    return replaced_text

def save_parsed_text(text, directory='parsed_texts'):
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    # List all files in the directory that match the naming pattern
    files = [f for f in os.listdir(directory) if f.startswith('parsed_text') and f.endswith('.txt')]
    
    # Sort files to find the highest numbered file
    files.sort()
    last_file = files[-1] if files else 'parsed_text0.txt'
    
    # Extract the number from the last file and increment it for the new file
    last_number = int(last_file.replace('parsed_text', '').replace('.txt', ''))
    new_file = f'parsed_text{last_number + 1}.txt'
    
    full_path = os.path.join(directory, new_file)
    
    with open(full_path, 'w') as file:
        file.write(text)

    print(f'File saved as {new_file}')

class CustomLoader(yaml.SafeLoader):
    def construct_scalar(self, node):
        value = super(CustomLoader, self).construct_scalar(node)
        return value.replace('\\\\', '\\')

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.load(file, Loader=CustomLoader)

if __name__ == "__main__":
    
    load_gestures()

    speech_controls = True
    # default_contextual = False
    default_contextual = True

    # Sample input text with gestures in braces
    input_text = """{Thinking} Staying fit, now that's an important question. 
    {Explain} It involves both eating healthy and exercising regularly. 
    {ShowSky} Start with simple activities like walking or stretching. 
    {ShowFloor} Gradually, you can try more intensive exercises. 
    {Yes} Remember, consistency is key to staying fit. 
    {CalmDown} Don't rush the process; take it step by step. 
    {Enthusiastic} And find activities that you truly enjoy! """

    sentences = tokenize_sentences(input_text)

    llm_response = load_yaml('llm_response.yaml') 
    sentences = tokenize_sentences(llm_response['response6'])

    parsed_text = ""
    for sentence in sentences:
        parsed_sentence = replace_bracket_contents(sentence)
        print(parsed_sentence)
        parsed_text += parsed_sentence + "\n"
    
    save_parsed_text(parsed_text)

    