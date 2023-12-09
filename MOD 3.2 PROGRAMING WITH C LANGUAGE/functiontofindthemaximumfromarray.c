#include <stdio.h>

// Function to find the maximum number in the array
int findMax(int arr[], int size) {
    int max = arr[0]; // Assume the first element as the maximum
    
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i]; // Update max if a larger element is found
        }
    }
    
    return max; // Return the maximum number
}

int main() {
    int size;
    
    printf("Enter the size of the array: ");
    scanf("%d", &size);
    
    int arr[size];
    
    printf("Enter %d elements: ", size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }
    
    int max = findMax(arr, size); // Call the function to find the maximum
    
    printf("The maximum number is: %d\n", max);
    
    return 0;
}

