#include <stdio.h>

// Function to reverse a string using recursion
void reverseString(char str[]) {
    if (str[0] == '\0') {
        return;
    }

    reverseString(str + 1);
    putchar(str[0]);
}

int main() {
    char str[100];

    printf("Enter a string: ");
    scanf("%s", str);

    printf("Reverse of the string: ");
    reverseString(str);

    printf("\n");

    return 0;
}

