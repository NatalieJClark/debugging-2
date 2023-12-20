# EXERCISE: Debug the following program so that all the tests pass ...
# class VowelRemover:
#     def __init__(self, text):
#         self.text = text
#         self.vowels = ["a", "e", "i", "o", "u"]

#     def remove_vowels(self):
#         i = 0
#         while i < len(self.text):
#             if self.text[i].lower() in self.vowels:
#                 self.text = self.text[:i] + self.text[i+1:]
#             i += 1
#         return self.text
    

#  SOLUTION:
class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            # Debugged by adding else statement
            # Only move to the next index if a non-vowel is found 
            else:
                i += 1
        return self.text
