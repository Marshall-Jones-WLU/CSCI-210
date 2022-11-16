/*  File: numbers.c
    Author: Marshall Jones

    Implementation file for numbers functions
*/

#include "numbers.h"

// Input function for the numbers
int getNumbers(int numbers, int max) {
    int count = 0;
    int num;
    printf("Enter a number or 0 to stop: ");
    scanf("%d", &num);
    while (num){
        numbers[count] = num;
        count++;
        printf("\nEnter a number or 0 to stop: ");
        scanf("%d", &num);
    }
    
}

// Output function for the numbers
int printNumbers(int numbers, int count) {
    int i;
    for (i = 0; i < count; i++) {
        printf("%d\n", numbers[i]);
    }
}

// Function that finds the sum of the input numbers
int sum(int numbers, int count) {
    int i;
    int result = 0;
    for (i = 0; i < count; i++) {
        result += numbers[i];
    }
    return result;
}

// Function that finds the average of the input numbers
int average(int numbers, int count) {
    int avg = sum(numbers, count) / count;
    return avg;
}