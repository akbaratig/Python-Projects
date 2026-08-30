from abc import ABC, abstractmethod
import random
import string
import nltk


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class Pingenerator(PasswordGenerator):
    def __init__(self, length):
        self.length = length
        
    def generate(self) -> str:
        return ''.join([random.choice(string.digits) for _  in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length = 10, include_numbers = False, include_symbols = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation
            
    def generate(self) -> str:
        return ''.join(random.choice(self.characters) for _ in range(self.length))
    

class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
        self,
        number_of_words : int = 4,
        seperator : str = '-', 
        capitalization : bool = False,
        vocabulary : list = None
    ):
        if (vocabulary is None) or (len(vocabulary) == 0):
            self.vocabulary = words
        else:
            self.vocabulary = vocabulary
            
        self.numb_of_words = number_of_words
        self.seperator = seperator
        self.capitalization = capitalization
    
    def generate(self):
        password_words = [random.choice(self.vocabulary) for _ in range(self.numb_of_words)]
        if self.capitalization:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]
        
        return self.seperator.join(password_words)
    
    
if __name__ == "__main__":
    words = nltk.corpus.words.words()
    
    while True:
        print("=" * 50)
        print("Select password generator:")
        print("1. Random Password Generator")
        print("2. Memorable Password Generator")
        print("3. Pin Generator")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            length = int(input("Enter the length of the password: "))
            include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
            generator = RandomPasswordGenerator(length, include_numbers, include_symbols)
            print(f"Generated Password: {generator.generate()}")
        
        elif choice == '2':
            number_of_words = int(input("Enter the number of words: "))
            seperator = input("Enter the separator (default is '-'): ") or '-'
            capitalization = input("Randomly capitalize words? (y/n): ").lower() == 'y'
            generator = MemorablePasswordGenerator(number_of_words, seperator, capitalization, words)
            print(f"Generated Password: {generator.generate()}")
        
        elif choice == '3':
            length = int(input("Enter the length of the PIN: "))
            generator = Pingenerator(length)
            print(f"Generated PIN: {generator.generate()}")
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Please try again.")