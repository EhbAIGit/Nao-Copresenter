import re

def process_text(input_text):
    # Dictionary mapping the bracketed text to specific values
    mapping = {
        '[happy]': '\\mrk=4001\\',
        '[sad]': '\\mrk=4002\\',
        '[humor]': '\\mrk=4003\\',
        '[info]': '\\mrk=4004\\',
        '[searching]': '\\mrk=4005\\',
        '[privacy]': '\\mrk=4006\\',
        '[learn]': '\\mrk=4007\\'
    }

    # Find all instances of text within brackets
    matches = re.findall(r'\[.*?\]', input_text)

    # Process each match
    for match in matches:
        if match in mapping:
            # Replace the bracketed text with its corresponding value
            input_text = input_text.replace(match, mapping[match])
        else:
            # Handle cases where the bracketed text is not recognized
            print(f"Warning: '{match}' does not match any predefined category.")

    return input_text

# Example usage:
example_text = "This is an example text with [happy] and [sad] emotions."
processed_text = process_text(example_text)
print(processed_text)
