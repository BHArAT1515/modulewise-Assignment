#include <stdio.h>

// Function to find factorial using recursion
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1; // Base case: Factorial of 0 and 1 is 1
    } else {
        return n * factorial(n - 1); // Recursive call with n-1
    }
}

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (num < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        int result = factorial(num);
        printf("Factorial of %d is %d.\n", num, result);
    }

    return 0;
}

