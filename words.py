word_list = ["hello", "goodbye", "good", "bad", "hey", "everyone", "Edible", "roy", "underwear"]

def make_uppercase(words):
   """Takes a list of words and capitilizes the first letter of every word then prints the word"""
   for word in words:
      print(word.upper())

def e_words(words):
   """ Only prints words that start with the letter "e" """
   for word in words:
      if word[0] == "e" or word[0] == "E":
         print(word.upper())



def print_upper_words3(words, must_start_with):
   for word in words:
      for letter in must_start_with:
         if word.startswith(letter):
            print(word.upper())
            break








