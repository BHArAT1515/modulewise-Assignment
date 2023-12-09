#include <stdio.h>

int findMax(int arr[], int size) {
    int max = arr[0];
    int i; // Declare 'i' outside the loop
    for (i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}
int main() {
    int size;
    printf("Enter the size of the array: ");
    scanf("%d", &size);
    
    int arr[size];
    printf("Enter %d elements: ", size);
    
    int i; // Declare 'i' outside the loop
    for (i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }
    
    int max = findMax(arr, size);
    printf("The maximum number is: %d\n", max);
    
    return 0;
    
}

