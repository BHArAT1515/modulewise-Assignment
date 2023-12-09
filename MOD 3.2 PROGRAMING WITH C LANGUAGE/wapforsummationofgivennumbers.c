#include <stdio.h>

// Function to find the summation of digits in a number
int digitSummation(int num) {
    if (num == 0)
        return 0;
    else
        return (num % 10) + digitSummation(num / 10);
}

int main() {
    int number;

    printf("Enter a number: ");
    scanf("%d", &number);

    int sum = digitSummation(number);

    printf("Summation of the digits in %d is: %d\n", number, sum);

    return 0;
}

