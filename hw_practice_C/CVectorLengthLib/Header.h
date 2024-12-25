#pragma once

#ifdef MYLIBRARY_EXPORTS
#define MYLIBRARY_API __declspec(dllexport)  // ƒл€ компил€ции библиотеки
#else
#define MYLIBRARY_API __declspec(dllimport) // ƒл€ использовани€ библиотеки
#endif
extern "C" {
	MYLIBRARY_API float vector_length(const int* numbers, int size);

}