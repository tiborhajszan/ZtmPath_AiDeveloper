import re

# Function to clean subtitle file content
def clean_subtitle(content):
    # Remove timestamps and sequence numbers
    cleaned_content = re.sub(r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', content)
    # Remove any remaining sequence numbers
    cleaned_content = re.sub(r'\n\d+\n', '', cleaned_content)
    # Remove excessive new lines
    cleaned_content = re.sub(r'\n+', '\n', cleaned_content).strip()
    return cleaned_content

# Read the subtitle file
with open('./Notes_PromptEngineering/Névtelen videó.srt', 'r') as file:
    content = file.read()

# Extract the cleaned text
extracted_text = clean_subtitle(content)

# Optionally, save to a new text file
with open('./Notes_PromptEngineering/extracted_text.txt', 'w') as output_file:
    output_file.write(extracted_text)

# Print the extracted text
print(extracted_text)
