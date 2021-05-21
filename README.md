# Cows-and-Bulls

Bulls and Cows is a mind game that involves 2 or more players.

The player(s) have to guess a 4 digit number (/string) with no repeated characters. They are given a fixed set of tries to attempt to find the expected 4 digit sequence(Note: It doesn't _have_ to be just 4 digits. It could be any no. of digits, but 4 is the most predominantly used one).

Everytime the player correctly guesses a character in the exact position as it is expected, the clue hints at it by saying "bull". On the otherhand, if the correctly guessed character is at some other position, then it is at hinted by saying "cow".

For example:
Let the code = 4321

```javascript
Player:
Guess = 4123
_Bulls: 1 and Cows: 3_

Guess = 1234
_Bulls: 0 and Cows: 4_

Guess = 5678
_Bulls: 0 and Cows: 0_

etc.,
```
