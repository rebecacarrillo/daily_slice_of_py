# This is the OOP solution to the word cleaner problem that I discussed on February 12, 2025. You can find me on threads a @rebecacarrillojj or on github. 



class WordsCleaner:
    """
    A class for cleaning non-alphanumeric characters from words.
    Think of it as a spa treatment for your strings - cleaning up the rough edges!
    """
    
    def __init__(self, words=None):
        """
        Initialize the WordsCleaner with an optional list of words.
        
        Args:
            words (list, optional): Initial list of words to clean
        """
        self.words = words if words is not None else []
        self.cleaned_words = []
    
    def add_words(self, new_words):
        """
        Add more words to the cleaner's list.
        Like adding more laundry to the washing machine!
        
        Args:
            new_words (list): Additional words to clean
        """
        if isinstance(new_words, list):
            self.words.extend(new_words)
        else:
            raise TypeError("new_words must be a list")
    
    def add_word(self, word):
        """
        Add a single word to the cleaner's list.
        
        Args:
            word (str): Single word to add
        """
        if isinstance(word, str):
            self.words.append(word)
        else:
            raise TypeError("word must be a string")
    
    def _strip_word_head_and_tail(self, word):
        """
        Private method to strip non-alphanumeric characters from word edges.
        The real workhorse - like a barber for strings!
        
        Args:
            word (str): The word to clean
        Returns:
            str: The cleaned word
        """
        if not word:
            return word
        
        # Find the start of alphanumeric characters
        for start, char in enumerate(word):
            if char.isalnum():
                break
        else:  # No alphanumeric characters found
            return ""
        
        # Find the end of alphanumeric characters
        for end, char in enumerate(word[::-1]):
            if char.isalnum():
                break
        
        return word[start:len(word) - end]
    
    def clean(self):
        """
        Clean all words in the list.
        Returns the cleaned words and stores them internally.
        Like running the washing machine after loading it up!
        
        Returns:
            list: List of cleaned words
        """
        self.cleaned_words = [self._strip_word_head_and_tail(word) for word in self.words]
        return self.cleaned_words
    
    def get_cleaned_words(self):
        """
        Retrieve the last set of cleaned words.
        
        Returns:
            list: The most recently cleaned words
        """
        return self.cleaned_words
    
    def clear(self):
        """
        Reset the cleaner, clearing all words.
        Like emptying the washing machine for the next load!
        """
        self.words = []
        self.cleaned_words = []


def run_tests():
    """
    Test cases for the WordsCleaner class.
    Test your code. Bring honor to your family. You know you want to :) Do it. 
    """
    # Create a cleaner instance
    cleaner = WordsCleaner()
    
    # Test single word addition
    cleaner.add_word("!!!hello!!!")
    assert cleaner.clean() == ["hello"], "Yikes. Single word test failed"
    
    # Test multiple words
    cleaner.clear()
    test_words = ["!!!hello!!!", "#@$world#@$", "...python..."]
    cleaner.add_words(test_words)
    assert cleaner.clean() == ["hello", "world", "python"], "Multiple words test failed"
    
    # Test edge cases
    cleaner.clear()
    edge_cases = ["", "#@$%", "hello", "123", "!@#hello!@#world!@#"]
    cleaner.add_words(edge_cases)
    expected = ["", "", "hello", "123", "hello!@#world"]
    assert cleaner.clean() == expected, "Edge cases test failed"
    
    # Test initialization with words
    init_cleaner = WordsCleaner(["!!!hello!!!", "#@$world#@$"])
    assert init_cleaner.clean() == ["hello", "world"], "Initialize with words test failed"
    
    print("All tests passed! Enjoy your fleeting moments of computing bliss")


if __name__ == "__main__":
    run_tests()



