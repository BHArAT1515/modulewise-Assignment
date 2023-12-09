#include<stdio.h>

int convert_years_to_days(int years) {
	int days = years*365;
	return days;
}

int convert_days_to_years(int days) {
	int years = days/365;
	return years;
}

int main() {
	int years, days;
	
	
	//convert years to days
	printf("enter the number of years: ");
	scanf("%d",&years);
	int converted_days = convert_years_to_days(years);
	printf("%d years is equal to %d.\n", years, converted_days);
	
	//convert days to years
	printf("enter the number of days: ");
	scanf("%d", &days);
	int converted_years = convert_days_to_years(days);
	printf("%d days is equal to %d years.\n", days, converted_years);
	
	return 0;
}
