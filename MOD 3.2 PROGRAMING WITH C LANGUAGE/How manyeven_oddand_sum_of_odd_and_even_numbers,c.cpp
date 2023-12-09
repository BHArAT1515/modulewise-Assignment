#include <stdio.h>
int main() {
    int start, end;
    int evenCount = 0, oddCount = 0;
    int evenSum = 0, oddSum = 0;

    printf("Enter the start number: ");
    scanf("%d", &start);

    printf("Enter the end number: ");
    scanf("%d", &end);
    if (start % 2 != 0)
        start++;
    for (int i = start; i <= end; i += 2) {
        evenCount++;
        evenSum += i;
    }
    for (int i = start + 1; i <= end; i += 2) {
        oddCount++;
        oddSum += i;
    }

    printf("Number of even numbers: %d\n", evenCount);
    printf("Number of odd numbers: %d\n", oddCount);
    printf("Sum of even numbers: %d\n", evenSum);
    printf("Sum of odd numbers: %d\n", oddSum);

    return 0;
}

