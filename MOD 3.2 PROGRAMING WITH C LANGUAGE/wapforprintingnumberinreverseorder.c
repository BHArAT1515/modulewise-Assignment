#include <stdio.h>
void printReverse(int number) {
    int reversedNumber = 0;
    while (number != 0) {
        int lastDigit = number % 10;
        reversedNumber = reversedNumber * 10 + lastDigit;
        number /= 10;
    }
    printf("Reversed number: %d\n", reversedNumber);
}
int main() {
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);
    printReverse(number);
    return 0;
}

