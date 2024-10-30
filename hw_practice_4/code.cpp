#include <iostream>

int main() {
    int number = 1234;
    int sum = 0;

    while (number !=0){
        sum += number % 10;
        number /= 10;
    }
    std::cout << "Sum of digits" << sum << std::endl;
    return 0;
}