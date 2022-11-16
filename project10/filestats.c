/*
Author: Marshall Jones

This program prints statistics on a text file and prints a numbered
listing to an output file or to the display.
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

void processFile(FILE *infile, FILE *outfile);
int wordCountInLine(char * line);

int main(int length, char *argVec[]){
    if (length == 1){ 
        printf("Usage: ./filestats <input file> [<output file>]\n");
	return 0; 
    }   
    FILE *infile = fopen(argVec[1], "r");
    if (infile == NULL){
	printf("The input file does not exist in this directory\n");
	return 0;
    }
    FILE *outfile = NULL;
    if (length == 3){
        outfile = fopen(argVec[2], "w");    // Using an output file
    }
    else{
	    outfile = stdout;                   // Using the terminal
    }
    processFile(infile, outfile);
    fclose(infile);
    if (outfile != stdout){
        fclose(outfile);
    }
}

/*
 * Prints a numbered listing of the input file to
 * the output file
 */
void processFile(FILE *infile, FILE *outfile){
    int max = 80;
    int fieldWidth = 4;
    char line[max];
    int lineNumber = 1;
    int lineCount = 0;
    int charCount = 0;
    int wordCount = 0;
    while (fgets(line, max, infile)){
        fprintf(outfile, "%*d%s", fieldWidth, lineNumber, "> ");  
        fputs(line, outfile);
        charCount += strlen(line);
        wordCount += wordCountInLine(line);
        lineCount++;
        lineNumber++;
    }
    fprintf(outfile, "\nLines: %d   Words: %d   Characters: %d\n", 
           lineCount, wordCount, charCount);
}


int wordCountInLine(char * line){
    int count = 0;

    // this variable will track whether or not we're inside a word
    bool inword = false;

    // loop over each character in the line:
    for (char * p=line; *p; ++p) {
        // if the character is blank (space, tab, or newline):
        if(*p == ' ' || *p == '\t' || *p == '\n'){
            inword = false; // set inword = false
        }
        // otherwise:
        else{
            // if !inword:
            if(!inword){
                // count++
                count++;
            }
            // set inword = true
            inword = true;
        }
    }
    
    return count;
}