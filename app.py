def is_sentence(sentence):
    string = ''
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    
    return string[::-1].casefold() == string.casefold()
    
sentence  = input("Please enter a sentence: ")
if is_sentence(sentence):
    print("'{}' is a palindrome sentence".format(sentence))
else:
    print("'{}' is not a palindrome sentence".format(sentence))