#pragma once

#ifdef MYLIBRARY_EXPORTS
#define MYLIBRARY_API __declspec(dllexport)  // ��� ���������� ����������
#else
#define MYLIBRARY_API __declspec(dllimport) // ��� ������������� ����������
#endif
extern "C" {
	MYLIBRARY_API float vector_length(const int* numbers, int size);

}