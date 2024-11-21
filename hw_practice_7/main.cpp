#include <iostream>
#include <vector>
#include <set>
#include <sstream>


std::vector<int> func1(const std::vector<int>& arr, int t) {
        int n = 0;
        for (int i : arr) {
            if (i > t) {
                n++;
            }
        }

        std::vector<int> res(n);
        n = 0;
        for (int i : arr) {
            if (i > t) {
                res[n++] = i;
            }
        }
        return res;
    }

     std::set<int> func2(const std::set<int>& set1, const std::set<int>& set2) {
        std::set<int> res;
        for (int i : set1) {
            if ( ( (i >= 10 && i < 20) || (i >= 100 && i < 200) || (i >= 1000 && i < 2000)) && set2.find(i) != set2.end()) {
                res.insert(i);
            }
        }
        return res;
    }

int main() {
    std::vector<int> arr1 = func1({ 0, 0, 0, 10, 10, 10 }, 1);
    std::cout << "func1 result" << std::endl;
    for (int i : arr1) {
        std::cout << i << std::endl;
    }

    std::set<int> set1 = { 11, 12, 13, 14, 15, 16 };
    std::set<int> set2 = { 14, 15, 16, 17, 18, 19 };
    std::set<int> res = func2(set1, set2);

    std::cout << "func2 result" << std::endl;
    for (int i : res) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    return 0;
}
