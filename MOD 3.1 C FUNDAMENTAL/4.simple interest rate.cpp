#include<stdio.h>

float calculate_simple_interest(float principal, float rate, float time) {
	float interest = (principal * rate * time) / 100;
	return interest;
}

int main(){
	float principal, rate, time;
	
	printf("enter the principal amount: ");
	scanf("%f", &principal);
	
	printf("enter the interest rate: ");
	scanf("%f", &rate);
	
	printf("enter the time period(in years): ");
	scanf("%f", &time);
	
	float interest = calculate_simple_interest(principal, rate, time);
	float amount = principal + interest;
	
	
	printf("principal amount: %0.2f\n", principal);
	printf("interest rate: %0.2f\n", rate);
	printf("time period: %0.2f\n", time);
	printf("simple interest: %0.2f\n", interest);
	printf("total amount: %0.2f\n", amount);
	
	return 0;
}
