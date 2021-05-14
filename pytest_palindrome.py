import pytest 
import palindrome

def test_space():
    #Passed Test
    assert palindrome.determinePalindrome("racecar") == "String is a palindrome", "passed test" 
    #Failed Test
    #assert palindrome.determinePalindrome("race car") == "not a valid input", "failed test" 

def test_randomAsciiSymbols():
    #Passed Test
    assert palindrome.determinePalindrome("$#@#$") == "String is a palindrome", "passed test"
    #Failed Test
    #assert palindrome.determinePalindrome("$#@##$") == "Not a palindrome", "failed test"