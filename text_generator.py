# Example text
original_text = ("\\pau=2000\\ ^mode(disabled) \\mrk=1001\\ ^start(animations/Stand/Gestures/Hey_1) One, Two.  ^wait(animations/Stand/Gestures/Hey_1) Three. \\mrk=1002\\ ^mode(disabled) Three, Four. Now Check if I have a latch.")

gestures_list = [
    'BodyTalk_1', 'BodyTalk_2', 'BodyTalk_3', 'BodyTalk_4', 'BodyTalk_5',
    'BodyTalk_6', 'BodyTalk_7', 'BodyTalk_8', 'BodyTalk_9', 'BodyTalk_10', 
    'BodyTalk_11', 'BodyTalk_12', 'BodyTalk_13', 'BodyTalk_14', 'BodyTalk_15', 'BodyTalk_16', 
    'YouKnowWhat_1', 'YouKnowWhat_2', 'YouKnowWhat_3',
    'YouKnowWhat_5', 'YouKnowWhat_6', 
    'Bored_1', 
    'BowShort_1', 
    'But_1', 
    'CalmDown_1', 'CalmDown_2', 'CalmDown_3', 'CalmDown_4', 'CalmDown_5', 'CalmDown_6', 
    'Choice_1', 
    'Desperate_1', 'Desperate_2', 'Desperate_3', 'Desperate_4', 'Desperate_5', 
    'Embarrassed_1', 
    'Enthusiastic_1', 'Enthusiastic_2', 'Enthusiastic_3', 'Enthusiastic_4', 'Enthusiastic_5', 
    'Everything_1', 'Everything_2', 'Everything_3', 'Everything_4', 
    'Excited_1', 
    'Explain_1', 'Explain_2', 'Explain_3', 'Explain_4', 'Explain_5', 'Explain_6',
    'Explain_7', 'Explain_8', 'Explain_9', 'Explain_10', 'Explain_11',
    'Far_1', 'Far_2', 'Far_3', 
    'Give_1', 'Give_2', 'Give_3', 'Give_4', 'Give_5', 'Give_6', 
    'Happy_1', 'Happy_2', 'Happy_3', 'Happy_4', 
    'Hey_1', 'Hey_2', 'Hey_3', 'Hey_4', 'Hey_5', 'Hey_6', 
    'Hysterical_1', 
    'IDontKnow_1', 'IDontKnow_2', 'IDontKnow_3', 'IDontKnow_4', 
    'Me_1', 'Me_2', 'Me_3', 'Me_4', 'Me_5', 'Me_6', 'Me_7', 
    'No_1', 'No_2', 'No_3', 'No_4', 'No_5', 'No_6', 'No_7', 'No_8', 'No_9', 
    'Nothing_1', 'Nothing_2', 
    'Peaceful_1', 
    'Please_1', 'Please_2', 'Please_3', 
    'ShowFloor_1', 'ShowFloor_2', 'ShowFloor_3', 'ShowFloor_4', 
    'ShowSky_1', 'ShowSky_2', 'ShowSky_4', 'ShowSky_5', 'ShowSky_6', 'ShowSky_7', 'ShowSky_8', 
    'ShowSky_9', 'ShowSky_10', 'ShowSky_11',
    'ShowTablet_2', 'ShowTablet_3', 
    'Think_1', 'Think_2', 'Think_3', 
    'Thinking_1', 'Thinking_2', 'Thinking_3', 'Thinking_4', 'Thinking_5', 'Thinking_6', 'Thinking_7', 'Thinking_8', 
    'Yes_1', 'Yes_2', 'Yes_3', 
    'You_1', 'You_2', 'You_3', 'You_4', 'You_5', 'You_6'
]

# Generating the new text
new_texts = []
for item in gestures_list:
    # Replace all instances of "Hey_1" with the current item in the loop
    replaced_text = original_text.replace("Hey_1", item)
    new_texts.append(replaced_text)

# Combine all the modified texts into a single string separated by new lines
final_text = "\n".join(new_texts)

# Specify the filename
filename = 'output_text.txt'

# Writing the final_text to a file
with open(filename, 'w') as file:
    file.write(final_text)

print(f"Data saved to {filename}")
