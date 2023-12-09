#include <stdio.h>
void printFibonacci(int limit) {
    int num1 = 0, num2 = 1, nextTerm; 
    printf("Fibonacci series up to %d:\n", limit);
    printf("%d, %d", num1, num2);
    nextTerm = num1 + num2;
    while (nextTerm <= limit) {
        printf(", %d", nextTerm);
        num1 = num2;
        num2 = nextTerm;
        nextTerm = num1 + num2;
    }
    printf("\n");
}
int main() {
    int limit;
    printf("Enter the limit for the Fibonacci series: ");
    scanf("%d", &limit);
    printFibonacci(limit);
    return 0;
}

