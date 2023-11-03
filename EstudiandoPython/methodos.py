"""
Este script demuestra el uso de varios métodos avanzados de la clase String en Python.
"""

def demonstrate_string_methods():
    # lower() y upper()
    example_string = "This is a String"
    lower_case_string = example_string.lower()
    upper_case_string = example_string.upper()

    # strip(), lstrip(), y rstrip()
    white_spaced_string = "   This is a String   "
    stripped_string = white_spaced_string.strip()

    # count()
    example_sentence = "This is an example sentence."
    count_of_is = example_sentence.count("is")

    # endswith()
    file_name = "document.txt"
    is_text_file = file_name.endswith(".txt")

    # isnumeric()
    numeric_string = "12345"
    is_numeric = numeric_string.isnumeric()

    # join() y split()
    words = ["This", "is", "a", "sentence"]
    joined_string = " ".join(words)

    sentence = "This is a sentence"
    word_list = sentence.split()

    # Impresión de resultados
    print(f"Original String: {example_string}")
    print(f"Lowercase String: {lower_case_string}")
    print(f"Uppercase String: {upper_case_string}")
    print(f"Stripped String: {stripped_string}")
    print(f"Count of 'is': {count_of_is}")
    print(f"Is Text File: {is_text_file}")
    print(f"Is Numeric: {is_numeric}")
    print(f"Joined String: {joined_string}")
    print(f"Word List: {word_list}")

if __name__ == "__main__":
    demonstrate_string_methods()
