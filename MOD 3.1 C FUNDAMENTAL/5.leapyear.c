#include<stdio.h>
int main(){
	int y;
	
	printf("enter year: ");
	scanf("%d", &y);
	
	if(y % 4 == 0 && y % 100!=0 || y % 400 == 0)
	{
		printf("this is leap year : ");
	}
	else
	{6+-
	    printf("this is not leap year : ");
    }
	return 0;	
}

