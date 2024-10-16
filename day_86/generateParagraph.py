import random
import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

# Download the required NLTK data
nltk.download('gutenberg')
nltk.download('punkt_tab')  # This is the sentence tokenizer


def generate_typing_paragraphs(num_paragraphs=20, min_sentences=10, max_sentences=12):
    # Load raw text from a public domain English text (e.g., Jane Austen's "Emma")
    raw_text = gutenberg.raw('austen-emma.txt')

    # Tokenize the text into sentences
    sentences = sent_tokenize(raw_text, language='english')

    paragraphs = []

    # for each paragraph
    for _ in range(num_paragraphs):
        # Randomly pick a number of sentences for each paragraph
        num_sentences = random.randint(min_sentences, max_sentences)

        # Join random sentences to form a paragraph
        paragraph_sentences = random.sample(sentences, num_sentences)
        paragraph_to_merge = ' '.join(paragraph_sentences)

        paragraphs.append(paragraph_to_merge)

    return paragraphs