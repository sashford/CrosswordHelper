This repo is meant to provide a simple tool to help identify possible words that could fit in word games such as crosswords.  While you 
will need the couple of other files, you will only need to run main.py for the program itself.

You will need to import your own word lists that you want to use.  Simply copy any .txt files into the WordLists directory and they will 
be parsed automatically.

To use the program itself, you will be prompted to input a pattern.  This pattern will simply consist of any letters that you know, and 
any gaps are filled with a "_" character.  For example, if the correct answer I was trying to find was "ability" but I only knew the 
first and last letters, I would type in "a_____y" and the program will output a list of available words that fit that pattern.  From 
there you can use the hints from the crossword itself to help you narrow down the list of words to the correct answer.
