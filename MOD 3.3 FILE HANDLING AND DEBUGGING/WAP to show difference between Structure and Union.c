#include <stdio.h>
#include <string.h>

// Define a structure
struct Student {
    int rollNumber;
    char name[50];
    float marks;
};

// Define a union
union Employee {
    int employeeId;
    float salary;
    char department[30];
};

int main() {
    // Using structure
    struct Student student1;
    student1.rollNumber = 101;
    strcpy(student1.name, "John Doe");
    student1.marks = 85.5;

    printf("Student Details:\n");
    printf("Roll Number: %d\n", student1.rollNumber);
    printf("Name: %s\n", student1.name);
    printf("Marks: %.2f\n\n", student1.marks);

    // Using union
    union Employee employee1;
    employee1.employeeId = 1001;
    printf("Employee Details:\n");
    printf("Employee ID: %d\n", employee1.employeeId);

    employee1.salary = 50000.0;
    printf("Salary: %.2f\n", employee1.salary);

    strcpy(employee1.department, "IT");
    printf("Department: %s\n", employee1.department);

    return 0;
}

