import random
import string



class Characters:
    def __init__(self, symbols,numbers):
        self.symbols = symbols
        self.numbers = numbers
    def capital_alphabets(self):
        capital_letters = list(string.ascii_uppercase)
        return capital_letters

    def small_alphabets(self):
        small_letters = list(string.ascii_lowercase)
        return small_letters

    def num(self):
        numbers = self.numbers.split(" ")
        return numbers

    def symb(self):
        symbols = self.symbols
        return symbols.split(" ")

class Password:
    def generating_password(self):
          nums = "0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5"
          signs = "! @ # $ % ^ & * ( ) _ + { } [ ] < > ? / ~ = . @ ` ,"
          ch = Characters(signs,nums)
          capital_letters = ch.capital_alphabets()
          small_letters = ch.small_alphabets()
          numbers = ch.num()
          symbols = ch.symb()
          characters = [capital_letters,small_letters,numbers,symbols]
          password = ""
          length1 = range(int(input("how long should the password be?")))
          for length in length1:
              range1 = int(random.uniform(0,4))
              range2 = int(random.uniform(0,26))
              character = characters[range1][range2]
              password += str(character)
          return password

def main():
    pwd = Password()
    password = pwd.generating_password()
    return password

