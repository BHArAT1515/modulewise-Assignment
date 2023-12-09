#include<stdio.h>
main(){
	int number;
	
	printf("enter a number: ");
	scanf("%d", &number);
	
	(number%2==0)? printf("number is even.\n") : printf("number is odd.\n");
}
