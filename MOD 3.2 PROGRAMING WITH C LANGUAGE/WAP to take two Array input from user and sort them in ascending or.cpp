#include <stdio.h>
#include <string.h>

// Recursive function to reverse a string
void reverseString(char str[], int start, int end) {
    if (start >= end)
        return;

    // Swap the characters at start and end positions
    char temp = str[start];
    str[start] = str[end];
    str[end] = temp;

    // Recursive call with the updated positions
    reverseString(str, start + 1, end - 1);
}

int main() {
    char str[100];

    printf("Enter a string: ");
    scanf("%s", str);

    int len = strlen(str);
    reverseString(str, 0, len - 1);

    printf("Reversed string: %s\n", str);

    return 0;
}

