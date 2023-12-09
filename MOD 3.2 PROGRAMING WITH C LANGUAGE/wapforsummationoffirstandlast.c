#include <stdio.h>

// Function to find the summation of first and last digits in a number
int firstAndLastDigitSum(int num) {
    int lastDigit = num % 10;

    while (num >= 10) {
        num /= 10;
    }

    int firstDigit = num;

    return firstDigit + lastDigit;
}

int main() {
    int number;

    printf("Enter a number: ");
    scanf("%d", &number);

    int sum = firstAndLastDigitSum(number);

    printf("Summation of the first and last digits in %d is: %d\n", number, sum);

    return 0;
}

