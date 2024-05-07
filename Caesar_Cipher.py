#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:56:05 2024

@author: annamarakasova
"""

def encrypt(input_text, num_of_shifts):
    """This function takes a text and a number as an input,
and encrypts the text by shifting the letters by the given number of shifts to the right in the alphabet.
To decrypt, use the same number of shifts but negative"""
    
    upd_text  = input_text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = []
    
    
    def get_shift_amount(i):
        """This function gets the correct index of a letter if its index is out of the range of the dictionary"""
        return i % 26
    
    for char in upd_text:
        
        if char in alphabet:
            char_index = get_shift_amount(alphabet.find(char) + num_of_shifts)

            encrypted_text.append(alphabet[char_index])
 
        else:
            encrypted_text.append(char)
#     Checking for capital letters in the text
    for i in range(len(input_text)):
        if input_text[i].isupper():
            encrypted_text[i] = encrypted_text[i].upper()
            
    return "".join(encrypted_text)
