def capitalize_words(sentence):
    return ' '.join([word.capitalize() for word in sentence.split()])

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels="aeiouAEIOU"
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return count

def is_palindrome(s):
    s=s.replace(" ","").lower()
    return s==s[::-1]