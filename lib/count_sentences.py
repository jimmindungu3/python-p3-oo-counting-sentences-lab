class MyString:
    def __init__(self, value=""):
        # Verify that the value is a string before assigning it
        if not isinstance(value, str):
            raise ValueError("MyString value must be a string")
        self.value = value

    def is_sentence(self):
        # Check if the value ends with a period
        return self.value.endswith('.')

    def is_question(self):
        # Check if the value ends with a question mark
        return self.value.endswith('?')

    def is_exclamation(self):
        # Check if the value ends with an exclamation mark
        return self.value.endswith('!')

    def count_sentences(self):
        # Count the number of sentences by splitting on periods, questions marks, and exclamation marks
        sentences = re.split(r'[.!?]', self.value)
        # Remove empty strings from the list (e.g., consecutive punctuation marks)
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return len(sentences)


