/*
Author: Marshall Jones
Project 8
File: guess.c

This program plays a guessing game with the user.  The program
displays a greeting and thinks of a number between 1 and 100.
The user inputs guesses until a guess equals the number. If user's
guess is too large or too small, the computer replies with a hint
to that effect.  When the user guesses the number in less than 7
attempts, the program displays the total number of guesses. However,
if the user exceeds 7 attempts, they lose the game and the program ends.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    int n, guess, count;
    srand((unsigned)time(NULL)); // initialize random number generator
    n = rand() % 100 + 1; // set random number to n
    guess = 0; // initialize guess variable to 0
    count = 0; // initialize count variable to 0

    printf("\nWelcome to the guessing game!\
    \nI have chosen a number between 1 and 100.\
    \nGuess in 7 tries to win.\n\n");
    while(1){
        count += 1;
        if(count > 7){
            printf("\nSheesh, you need to rethink your strategy. You lost!\n");
            printf("The number was %i", n);
            printf("\n\n");
            break;
        }
        printf("Enter your guess: ");
        scanf("%d", &guess);

        if(guess < n){
            printf("\nToo small!\n");
        } else if(guess > n){
            printf("\nToo big!\n");
        } else {
            printf("%s %d %s", "\nCongratulations! You've guessed it in", count, "tries!\n\n");
            break;
        }
    }
    }
