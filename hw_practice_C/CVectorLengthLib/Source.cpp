#include "pch.h"
#include "Header.h"
#include <cmath>
#include <cstdlib>
#include <ctime>

float vector_length(const int* vector, int size) {
    clock_t start_time = clock(); // ������ ������ �������

    float sum = 0;
    for (int i = 0; i < size; ++i) {
        sum += vector[i] * vector[i];
    }
    float result = sqrt(sum);

    clock_t end_time = clock(); // ����� ������ �������
    float elapsed_time = float(end_time - start_time) / CLOCKS_PER_SEC; // ����� � ��������

    return elapsed_time; // ���������� ����� ����������
}
