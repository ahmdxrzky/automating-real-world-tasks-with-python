# Scenario
# For this project, you'll create a "word cloud" from a text by writing a script. This script needs to process the text, remove punctuation,
# ignore case and words that do not contain all alphabets, count the frequencies, and ignore uninteresting or irrelevant words.
# A dictionary is the output of the calculate_frequencies function. The wordcloud module will then generate the image from your dictionary.

# Import some external libraries
!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# Upload text file through uploader widget
def _upload():
    _upload_widget = fileupload.FileUploadWidget()
    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # Remove all punctuations --> return a list contains all words from the text
    letter_buffer = ""
    word_buffer = []
    for letter in file_contents:
        if letter not in punctuations:
            if letter != " ":
                letter_buffer += letter.lower()
            else:
                word_buffer.append(letter_buffer)
                letter_buffer = ""
    
    # Choose words with alphabets only
    word_alpha_only = []
    for word in word_buffer:
        if word.isalpha():
            if word not in uninteresting_words:
                word_alpha_only.append(word)
    
    # Count how many times each word appears and put it in a dictionary
    # with the word as the key and the count as the value
    word_dictionary_from_text = {}
    for word in word_alpha_only:
        if word not in word_dictionary_from_text.keys():
            word_dictionary_from_text[word] = 1
        else:
            word_dictionary_from_text[word] += 1
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_dictionary_from_text)
    return cloud.to_array()

  
# Display your wordcloud image
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
