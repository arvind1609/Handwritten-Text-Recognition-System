from spellchecker import SpellChecker

spell = SpellChecker()

def correct_spelling(word):
    original_word = word
    
    # If word is all caps like an acronym
    if not word.isupper():
         original_word = word.lower()
    corrected_word = spell.correction(original_word)
    
    # If correction string size less than original, keep original
    if len(original_word) == len(corrected_word):
        final_word = corrected_word
    else:
        final_word = original_word

    if word[0].isupper() and not word.isupper():
        final_word = final_word.capitalize()
    
    return final_word    
