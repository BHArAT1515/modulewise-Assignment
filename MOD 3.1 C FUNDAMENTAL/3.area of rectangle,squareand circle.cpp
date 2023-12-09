#include<stdio.h>
main(){
	int a,b,rectangle,radius;
	float triangle,circle;
	printf("enter the length: ");
	scanf("%d",&a);
	printf("enter the width: ");
	scanf("%d",&b);
	rectangle=a*b;
	triangle=(a*b)*1/2;
	printf("\n area of rectangle is: %d", rectangle);
	printf("\n area of triangleis: %f", triangle);
	printf("\n enter the radius: ");
	scanf("%d", &radius);
	circle=3.14*radius*radius;
	printf("\n area of circle is:%f", circle);
}
