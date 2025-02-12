def clean_words(word_list):
    """
    Takes a list of words and removes non-alphanumeric characters from the start and end of each word.
    Returns a new list with the cleaned words.
    
    Args:
        word_list (list): List of strings to clean
    Returns:
        list: New list containing cleaned strings
    """
    return [strip_word_head_and_tail(word) for word in word_list]

def strip_word_head_and_tail(word):
    """
    Strips non-alphanumeric characters from the start and end of a word.
    Like giving your string a haircut, but we only trim the split ends!
    
    Args:
        word (str): The word to clean
    Returns:
        str: The cleaned word
    """
    # this is our ending condition
    if not word:
        return word
    
    # Find where the actual word begins
    for start, char in enumerate(word):
        if char.isalnum():
            break
    else:  # No alphanumeric characters found
        return ""
    
    # Now find where the word ends
    for end, char in enumerate(word[::-1]):
        if char.isalnum():
            break
    
    # Return the juicy middle part
    # Everything between start and (length - end)
    return word[start:len(word) - end]


# Test cases. Test your code. Bring honor to your family. You know you want to :) Do it. 
def run_tests():
    """
    Runs test cases for our string cleaning functions.
    If these fail, fix them before starting a new feature please.
    """
    
    test_cases = [
        # [input, expected_output]
        ["hello", "hello"],
        ["!!!hello!!!", "hello"],
        ["#@$%", ""],
        ["", ""],
        ["hi there", "hi there"],
        ["123", "123"],
        ["!@#hello!@#world!@#", "hello!@#world"],
        ["...py...thon...", "py...thon"],
    ]
    
    for test_input, expected in test_cases:
        result = strip_word_head_and_tail(test_input)
        assert result == expected, f"Test failed! Input: {test_input}, Expected: {expected}, Got: {result}"
    
    # Test the main function with a list of words
    word_list = ["!!!hello!!!", "#@$world#@$", "...python..."]
    expected_list = ["hello", "world", "python"]
    result_list = clean_words(word_list)
    assert result_list == expected_list, f"List test failed! Expected: {expected_list}, Got: {result_list}"
    
    print("All tests passed! Enjoy your fleeting moments of computing bliss")


if __name__ == "__main__":
    run_tests()
