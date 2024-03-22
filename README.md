# <img src="https://help.apple.com/assets/5FDCE7A064869015B86C4E71/5FDCE7A164869015B86C4E78/en_US/c34b1b0e87e731a83161d9bb21345afc.png" alt="Image of Apple Notes logo" width="25" height="25"> Notes Reverse
*by Jacob Field*

## Description
Reverses the order of a text file line by line

Takes a .txt file as input and returns a new .txt file with the ordering of the rows reversed

## Inspiration
In 2018, I started keeping a diary in my iPhone's notes app by writing down a few words for each day. 

As the note sheet grew, I had to scroll down further and further to add a new entry because of how I ordered the note sheet. 

After many years, I finally re-ordered my note sheet and fixed my problem with this simple program!

## How to Use
1. Create a `.txt` file in the same location as `main.py` that contains your desired text

2. In `main.py`, change the variable `FILE_PATH` to your text file's name:
```python
FILE_PATH = 'your text file.txt'
```

## Example Input and Output
Example input `notes.txt`
```
3/1/2024 - walked the dog
3/2/2024 - it was sunny outside today
3/3/2024 - studied all day for my calc exam
3/4/2024 - listening to new music
3/5/2024 - packing for my next vacation!
```
Example output `reversed_notes.txt`
```
3/5/2024 - packing for my next vacation!
3/4/2024 - listening to new music
3/3/2024 - studied all day for my calc exam
3/2/2024 - it was sunny outside today
3/1/2024 - walked the dog
```
