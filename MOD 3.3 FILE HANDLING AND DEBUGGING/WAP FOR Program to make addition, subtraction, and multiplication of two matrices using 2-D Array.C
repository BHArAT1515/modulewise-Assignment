#include <stdio.h>

#define ROWS 3
#define COLS 3

// Function to add two matrices
void addMatrix(int mat1[ROWS][COLS], int mat2[ROWS][COLS], int result[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            result[i][j] = mat1[i][j] + mat2[i][j];
        }
    }
}

// Function to subtract two matrices
void subtractMatrix(int mat1[ROWS][COLS], int mat2[ROWS][COLS], int result[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            result[i][j] = mat1[i][j] - mat2[i][j];
        }
    }
}

// Function to multiply two matrices
void multiplyMatrix(int mat1[ROWS][COLS], int mat2[ROWS][COLS], int result[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            result[i][j] = 0;
            for (int k = 0; k < COLS; k++) {
                result[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }
}

// Function to display a matrix
void displayMatrix(int mat[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            printf("%d\t", mat[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int mat1[ROWS][COLS], mat2[ROWS][COLS], result[ROWS][COLS];
    
    printf("Enter elements of first matrix (%dx%d):\n", ROWS, COLS);
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            scanf("%d", &mat1[i][j]);
        }
    }
    
    printf("Enter elements of second matrix (%dx%d):\n", ROWS, COLS);
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            scanf("%d", &mat2[i][j]);
        }
    }
    
    // Addition
    addMatrix(mat1, mat2, result);
    printf("Addition of matrices:\n");
    displayMatrix(result);

    // Subtraction
    subtractMatrix(mat1, mat2, result);
    printf("Subtraction of matrices:\n");
    displayMatrix(result);

    // Multiplication
    multiplyMatrix(mat1, mat2, result);
    printf("Multiplication of matrices:\n");
    displayMatrix(result);

    return 0;
}

