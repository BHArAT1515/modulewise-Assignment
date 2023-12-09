#include <stdio.h>

// Function to reverse a string using recursion
void reverseString(char str[]) {
    if (str[0] == '\0') {
        return; // Base case: If the string is empty, return
    }

    reverseString(str + 1); // Recursive call with the next character in the string

    putchar(str[0]); // Print the current character
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

