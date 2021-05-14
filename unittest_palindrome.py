import unittest
import palindrome

class testPalindrome(unittest.TestCase):
    def test_space(self):
        #Passing case
        self.assertEqual(palindrome.determinePalindrome("racecar"), "String is a palindrome")
        #Failing Case
        #self.assertEqual(palindrome.determinePalindrome("race car", "not a valid input"))
    def test_randomAsciiSymbols(self):
        #Passing Case
        self.assertEqual(palindrome.determinePalindrome("$#@#$"), "String is a palindrome")
        #Failing Case
        #self.assertEqual(palindrome.determinePalindrome("$#@##$"), "Not a palindrome")
        

if __name__ == '__main__':
    unittest.main()