from window import SpeedTyper
from generateParagraph import generate_typing_paragraphs


if __name__ == '__main__':
    # Generate a long list of random English paragraphs
    paragraph_list = generate_typing_paragraphs(num_paragraphs=10)
    clean_paragraphs = [paragraph.replace('\n', ' ') for paragraph in paragraph_list]

    # debug
    print(clean_paragraphs)
    print(clean_paragraphs[0])
    app = SpeedTyper(clean_paragraphs)
