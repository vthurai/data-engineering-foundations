import unittest, re

'''
QUESTION 1.
A 'tokenizer' is a program that breaks down a string into individual parts called tokens.
For example, Python's interpreter needs to first tokenize the keywords and names in the code that
you write before it can compile them into machine code. This is done using regex.
Write a function that tokenizes a sentence, returning a list.
For this question we consider a token as:
- Any (alphabetical) word, which may contain apostrophes or hyphens.
- Any punctuation mark (not including apostrophes or hyphens).
- Any phrase inside quotes or parentheses (but not including them).
Assume the input string will only contain the characters mentioned above.
'''
def tokenize(text):
    tokens = []

    p1 = r'((?<=")(.+)(?="))' #text in quotation, excluding quotes
    p2 = r'((?<=\()(.+)(?=\)))' #text in parentheses, excluding parentheses
    p3 = r'(\w+\-\w*)' #hyphenated words
    p4 = r'(?<=\s)(\w+)' #word with space behind
    p5 = r'(\w+\'\w*)' #word with apostrophe
    p6 = r'([^\w\s\-"\(\)])' #other punctuation

    pattern = p1+'|'+p2+'|'+p3+'|'+p4+'|'+p5+'|'+p6

    while len(text) > 0:
        if re.search(pattern, text):
            span = re.search(pattern, text).span()
            index1 = span[0]
            index2 = span[1]
            if index1:
                tokens.append(text[:index1].strip())
            tokens.append(text[index1:index2].strip())
            text = text[index2:].strip()
        else:   #if text entered is just one word or last word left
            tokens.append(text.strip())
            text = ''

    print(tokens)


'''
QUESTION 2.
Write a function that parses a string and returns True if it can be a valid Python dictionary.
For this question:
- Keys can be a single string or a positive integer. Strings need to be surrounded by "double-quotes".
- Values can be a single string, positive integer, or another dictionary.
Assume the input string will contain only dictionary characters (braces, colons, commas, spaces),
double-quotes, and alphanumeric characters.
You do not need to check if the keys are unique, only that the syntax is valid.
Do not use eval or any parsing modules. Try to work out the solution on your own.
'''
def is_valid_dict(text):



# Unit tests below.
class TestQ1(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(tokenize(''), [])

    def test_short(self):
        self.assertEqual(tokenize('Token'), ['Token'])

    def test_long(self):
        self.assertEqual(tokenize('There are many ways to catch a fish'),
        ['There', 'are', 'many', 'ways', 'to', 'catch', 'a', 'fish'])

    def test_apos(self):
        self.assertEqual(tokenize('Can\'t you see where I\'m going'),
        ['Can\'t', 'you', 'see', 'where', 'I\'m', 'going'])

    def test_hyphen(self):
        self.assertEqual(tokenize('orange-red twenty-two non-sequitur'),
        ['orange-red', 'twenty-two', 'non-sequitur'])

    def test_punc(self):
        self.assertEqual(tokenize('Why? Well, to be honest: I forgot.'),
        ['Why', '?', 'Well', ',', 'to', 'be', 'honest', ':', 'I', 'forgot', '.'])

    def test_quote(self):
        self.assertEqual(tokenize('Mark Twain "Samuel Langhorne Clemens" wrote "The Adventures of Tom Sawyer"'),
        ['Mark', 'Twain', '"', 'Samuel Langhorne Clemens', '"', 'wrote', '"', 'The Adventures of Tom Sawyer', '"'])

    def test_paren(self):
        self.assertEqual(tokenize('The man (and his wife) left the (office) building'),
        ['The', 'man', '(', 'and his wife', ')', 'left', 'the', '(', 'office', ')', 'building'])

    def test_comb(self):
        self.assertEqual(tokenize('George Lucas\' Film, STAR WARS: EPISODE IV "A NEW HOPE" (now playing) Monday-Friday.'),
        ['George', 'Lucas\'', 'Film', ',', 'STAR', 'WARS', ':', 'EPISODE', 'IV', '"', 'A NEW HOPE', '"', '(', 'now playing', ')', 'Monday-Friday', '.'])


class TestQ2(unittest.TestCase):

    def test_valid(self):
        valid = [r'{"a" : 1}',
                 r'{0 : "a", 1 : "b", "key0" : "c", "key1" : "d"}',
                 r'{0:{0:1}}',
                 r'{"":""}',
                 r'{0:1}',
                 r'{"":456}',
                 r'{0:""}',
                 r'{"":{"":{"":""            ,"":""},"":""}}',
                 r'{   "firstkey"  :   "firstvalue",   "secondkey":    "secondvalue"}',
                 r'{"this is a key" : "this is a value"}',
                 r'{"{this is a valid key}" : "this } is a valid { value"}',
                 r'{ "key"  : { "nest0" : { "nest1" : 1 }  }  }',
                 r'{ "key"  : { "nest0" : { "nest1" : { "nest20" : 999, "": 1, "}{}{}{":2 }, 765:1 }  }  }',
                 r'{0:1, 1:2,}', # Trailing commas are allowed.
                 ]

        for test_string in valid:
            with self.subTest(test_string=test_string):
                msg = "The following string is valid but the function returned False: " + test_string
                self.assertEqual(is_valid_dict(test_string), True, msg)

    def test_invalid(self):
        invalid = [r'',
                   r',',
                   r',,,,',
                   r'1',
                   r'1:1',
                   r'abc',
                   r'{}', # Sets are not dictionaries.
                   r'{{}',
                   r'{{}}',
                   r'}',
                   r'{',
                   r'{""}',
                   r'{,,,,,,}',
                   r'{"invalid"}',
                   r'{"invalid": }',
                   r'{1:1 22:33}',
                   r'{1: {}, 2: {}}',
                   r'{a}',
                   r'{0}',
                   r'{,}',
                   r'{1:1, , 2:2,}',
                   r'{0: "a", "invalid":{0} }',
                   r'{1: 2, "3":{{} }',
                   r'{"key1" "key2"}',
                   r'{"key1": 1 "key2": 2}',
                   r'{ {1:2} : "dictionary is key" }',
                   r'{ "00" : "00" }{ "01" : "01" }',
                   r'{ "00" : "00" },{ "01" : "01" }',
                   ]

        for test_string in invalid:
            with self.subTest(test_string=test_string):
                msg = "The following string is invalid but the function returned True: " + test_string
                self.assertEqual(is_valid_dict(test_string), False, msg)

if __name__ == "__main__":
    unittest.main()
