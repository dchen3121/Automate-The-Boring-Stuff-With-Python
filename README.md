# Automate The Boring Stuff With Python

A list of notes and projects I did while going through the book "Automate the Boring Stuff with Python". 
There will be notes stored inside a folder for each chapter, inside a raw .py file. The list of projects can be found below. 

## Project Summaries: 

### password_locker.py: 
- **Usage**:   
  password_locker \<keyword\>
- **Purpose**:   
  The key to keyword (stored inside a dictionary in original python file) will be copied to the clipboard.
- Learned how to take values from python files using command line programs.
- Insecure - involves changing the source code.


### bullet_point_adder.py:
- **Usage**:   
  bullet_point_adder
- **Purpose**:   
  The value copied to clipboard previously will have a bullet point added in front of every one of its newlines.
- Learned how to manipulate clipboard input and return another value efficiently, for repetitive tasks.


### find_phone_email.py:
- **Usage**:   
  find_phone_email \<input\>
- **Purpose**:  
  Finds all values inside input and returns all the phone numbers and emails inside input copied to the clipboard.
- Learned how to use regexes to search through strings / inputs.


### refine_word_document.py:
- **Usage**:  
  refine_word_document
- **Purpose**:  
  Removes all duplicate spaces and duplicate punctuation of whatever's copied to the clipboard.
- Practiced more interaction with regexes.


### random_quiz_generator.py:
- **Usage**:  
  random_quiz_generator \<input\>
- **Purpose**:  
  Generates input number of quizzes based on the data inside source python file.
- Learned how to open, read, and write in .txt documents and change directories on a windows computer.
- Familiarized with os and shutil modules
- This can be used as a future template for creating multiple choice / fill in the blank quizzes.


### mcb.py:
- **Usage**:   
  mcb \<keyword\>: copies value stored of keyword to clipboard  
  mcb save \<keyword\>: saves value on clipboard to keyword  
  mcb list: lists all the stored keywords (but not the keys)  
  mcb delete \<keyword\>: deletes the keyword-value pair  
  mcb deleteall: deletes all the keywords 
- Learned how to store data inside shelves externally, not just within the python source file.


### mapit.py:
- **Usage**:  
  mapit / mapit \<input\>
- **Purpose**:  
  Opens the default web browser to the google maps page where the location of the value of input / clipboard is opened.
- Learned how to interact with web browsers and open web pages at ease.
