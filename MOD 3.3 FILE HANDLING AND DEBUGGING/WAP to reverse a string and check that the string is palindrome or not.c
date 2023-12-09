#include <stdio.h>
#include <string.h>

// Function to reverse the given string
void reverseString(char str[]) {
    int length = strlen(str);
    int i, j;
    char temp;

    for (i = 0, j = length - 1; i < j; i++, j--) {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
    }
}

// Function to check if the string is a palindrome
int isPalindrome(char str[]) {
    int length = strlen(str);
    int i, j;

    for (i = 0, j = length - 1; i < j; i++, j--) {
        if (str[i] != str[j]) {
            return 0; // Not a palindrome
        }
    }

    return 1; // Palindrome
}

int main() {
    char str[100];

    printf("Enter a string: ");
    scanf("%s", str);

    // Reverse the string
    reverseString(str);

    printf("Reversed string: %s\n", str);

    // Check if the reversed string is a palindrome
    if (isPalindrome(str)) {
        printf("The original string is a palindrome.\n");
    } else {
        printf("The original string is not a palindrome.\n");
    }

    return 0;
}

