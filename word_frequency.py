import string
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def format_printer(dict, num):
    print(f'The top {num} words in you file are:')
    for x in dict[:num]:
        print(f'{x[0]} || {x[1]}')


def frequency_sorter(dict):
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)


def word_counter(text):
    word_frequency = {

    }
    for word in text:
        if word in word_frequency:
            word_frequency[word] = word_frequency[word]+1
        else:
            word_frequency[word] = 1
    return word_frequency


def remove_stop_words(text):
    text_list = text.split()
    # print(text_list)
    for word in text_list:
        for stop_word in STOP_WORDS:
            if word == stop_word:
                #   print('Deleting', word)
                text_list.remove(word)
    return text_list


def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))


def remove_uppercase(text):
    return text.lower()


def filter_file(text):
    remove_punctuation(text)
    remove_stop_words(text)
    remove_uppercase(text)


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    print(f'Your file is: {file}')
    with open(file) as open_file:
        read_file = open_file.read()
    halfway = remove_punctuation(remove_uppercase(read_file))
    closer = remove_stop_words(halfway)
    format_printer(frequency_sorter(word_counter(closer)), 10)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
