#include <stdio.h>

// Define the structure for employee
struct Employee {
    int empno;
    char empname[50];
    char address[100];
    int age;
};

int main() {
    // Create an array of structures to store information about five employees
    struct Employee employees[5];

    // Get information about employees from the user
    int i;
    for (i = 0; i < 5; i++) {
        printf("Enter Employee %d Details:\n", i + 1);
        printf("Employee Number: ");
        scanf("%d", &employees[i].empno);
        printf("Employee Name: ");
        scanf(" %[^\n]", employees[i].empname);
        printf("Address: ");
        scanf(" %[^\n]", employees[i].address);
        printf("Age: ");
        scanf("%d", &employees[i].age);
        printf("\n");
    }

    // Display information about employees
    printf("Employee Details:\n");
    for (i = 0; i < 5; i++) {
        printf("Employee %d:\n", i + 1);
        printf("Employee Number: %d\n", employees[i].empno);
        printf("Employee Name: %s\n", employees[i].empname);
        printf("Address: %s\n", employees[i].address);
        printf("Age: %d\n", employees[i].age);
        printf("\n");
    }

    return 0;
}

