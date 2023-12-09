#include<stdio.h>
main(){
	int x, y;
	printf("\n enter the number x: ");
	scanf("%d", &x);
	printf("\n enter the number y: ");
	scanf("%d", &y);
	x = x+y;
	y=x-y;
	printf("\n this is value of y=%d", y);
	x=x-y;
	printf("\n this is vale of x=%d", x);
}
