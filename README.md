# Wordle - The viral word game in python!

## Screenshots

![image](https://user-images.githubusercontent.com/20843172/163562300-4ee00609-2637-4c45-b63b-044bc3ea3ee4.png)
![image](https://user-images.githubusercontent.com/20843172/163562800-7ce1bd6f-537c-4bde-9ce5-0b6df32581b6.png)

## Information

The popular word game [Wordle](https://www.nytimes.com/games/wordle) took the internet by storm in 2022, as it became one of the most viral online games on the planet, as users shared their scores in social media and competed with friends and strangers alike, trying to guess the mystery 5-letter word in as few tries as possible.

Being both a Python and Wordle enthusiast I participated in the viral trend by creating a clone of the game in python, to be played locally from your computer's terminal!

## Lessons learnt from this project
- Further understood and implemented OOP principles in python, through the structure of the different components that power the game.
- Expanded my knowledge on extracting data from "back-end" procedures (eg. an array's items that the program uses to check the state of the game) and feeding them to the "front-end" of the program, translating them and displaying them in a way that is understandable to the the end-user (player) through methods of a visualizer object.
- Learn how to visualize data in an aesthetically pleasing way through the terminal

## Rules

The rules are simple, the player must guess a random 5 letter word in the fewest tries possible, with a maximum of 6 tries.

For each guess, the player receives hints about the letters of the mystery word. 

For each letter in the player's guess, a symbol is shown that ties that letter to the mystery word:
  - A tick means that the letter exists in that exact position in the mystery word.
  - An asterisk means that the letter is in the mystery word, but at another position.
  - An X means that the letter is not in the mystery word.

As an example: if the mystery word is PARTY, then guessing RAINY will return the hints: \[✱ ✔ ✖ ✖ ✔]

## Instructions

0. Download any 3.x version of python
1. Clone this repository to your preferred directory
2. On your terminal, change into the directory that pydle.py is located
  cd C:\...\pydle
  py pydle.py
