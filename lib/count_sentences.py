#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value = ''):
        if  isinstance(value, str) and value != '':
            self.value = value
        
        else:
            print('The value must be a string.')

    def is_sentence(self):
        if(self.value.endswith('.') == True):
            return True
        
        else:
            return False
        
    def is_question(self):
        if(self.value.endswith('?') == True):
            return True
        
        else:
            return False
        
    def is_exclamation(self):
        if(self.value.endswith('!') == True):
            return True
        
        else:
            return False
        
    def count_sentences(self):
        if hasattr(self, "value"):
            cleaned_value = self.value.replace(',', '')

            sentences = re.split(r'[.!?]', cleaned_value)
    
            sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

            length = len(sentences)
            return length
        else:
            return 0
            
        
            
