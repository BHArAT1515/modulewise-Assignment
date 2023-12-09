#include<stdio.h>
/*
addition = c=a+b
subtraction = num=x+y
multiplication = p=q*r
division = l=m/n
modulo = i=j%k
*/ 
main(){
	int c,a,b,num,x,y,q,r,l,m,n;
	float  i,j,k;
	printf("\n This is addition");
	//addition
	printf("\nenter value of a and b: ");
	scanf("%d %d", &a,&b);
	c=a+b;
	printf("answer is :%d",c);
	
	printf("\n This is subtraction");
	//subtraction
	printf("\n");
	printf("\n enter value of x and y: ");
	scanf("%d %d", &x,&y);
	num=x-y;
	printf("answer is :%d", num);
	printf("\n This is multiplication");
	//multiplication
	printf("\n");
	printf("\n enter value of q and r: ");
	scanf("%d %d", &q,&r);
	num=q*r;
	printf("answer is :%d",num);
	printf("\n This is division ");
	//division
	printf("\n");
	printf("\n enter value of m and n: ");
	scanf("%d %d", &m,&n);
	num=m/n;
	printf("answer is :%d",num);
	printf("\n This is modulo");
	
}
