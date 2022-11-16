/*
Author: Ken Lambert

Tests a random number generator, using the system clock
to seed the generator.

*/


#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){

   int i, n;
   
   n = 10;
   
   /* Intializes random number generator */
   srand((unsigned)time(NULL));

   /* Print n random numbers from 1 to 100 */
   for( i = 0 ; i < n ; i++ ){
      printf("%d\n", rand() % 100 + 1);
   }
   
   return(0);
}