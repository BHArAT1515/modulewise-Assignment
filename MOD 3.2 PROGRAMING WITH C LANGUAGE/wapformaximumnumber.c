#include <stdio.h>
int max(int a, int b) {
    return (a > b) ? a : b;
}
int findMax(int a, int b, int c) {
    return max(a, max(b, c));
}
int main() {
    int num1, num2, num3;

    printf("Enter three numbers: ");
    scanf("%d %d %d", &num1, &num2, &num3);

    int maximum = findMax(num1, num2, num3);

    printf("The maximum number is: %d\n", maximum);

    return 0;
}

