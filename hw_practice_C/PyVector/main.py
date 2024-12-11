from ctypes import *

import math
import time
import random

# Загружаем библиотеку
lib = CDLL('./CVectorLengthLib.dll')

def time_cpp(data):
    lib.vector_length.argtypes = (POINTER(c_int), c_int)
    lib.vector_length.restype = c_float

    data = [2, 3, 5 ]
    array_type = c_int * len(data)
    c_array = array_type(*data)

    a = lib.vector_length(c_array, len(data))
    return a

def time_python(data):
    start_time = time.time()

    sum = 0
    for i in data:
        sum += i**2
    result = math.sqrt(sum)

    end_time = time.time()
    return end_time - start_time


test_case = [
    10_000, 50_000, 100_000, 200_000, 500_000
]
data = [random.randint(0, 100) for i in range(1000)]

for iterations in test_case:
    cpp_duration = 0
    for i in range(iterations):
        cpp_duration += time_cpp(data)

    python_duration = 0
    for i in range(iterations):
        python_duration += time_python(data)


    print(f"iterations: {iterations}, python_duration: {python_duration}, cpp_duration: {cpp_duration}")
