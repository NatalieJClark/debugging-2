# CHALLENGE: Debug the following program ...

# class LetterCounter:
#     def __init__(self, text):
#         self.text = text

#     def calculate_most_common(self):
#         counter = {}
#         most_common = None
#         most_common_count = 1
#         for char in self.text:
#             if not char.isalpha():
#                 continue
#             counter[char] = counter.get(char, 1) + 1
#             if counter[char] > most_common_count:
#                 most_common = char
#                 most_common_count += counter[char]
#         return [most_common_count, most_common]

# counter = LetterCounter("Digital Punk")
# print(counter.calculate_most_common())
# Intended output:
# [2, "i"]


#  SOLUTION:
class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 0
        for char in self.text:
            if not char.isalpha():
                continue
            # Original code:
            # keyscounter[char] = counter.get(char, 1) + 1        
            # Debugged by adding if/else statement
            #   For counter dictionary keys that don't yet exist, their value is set to 1
            #   For counter dictionary keys that already exist, their value is increased by 1
            if counter.get(char) == None:
                counter[char] = 1
            else:
                counter[char] = counter.get(char) + 1

            if counter[char] > most_common_count:
                most_common = char
                # Original code:
                # most_common_count += counter[char]  
                # Debugged by changing to =
                most_common_count = counter[char]
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]