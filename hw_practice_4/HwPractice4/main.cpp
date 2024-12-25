#include <iostream>
#include <cmath>
using namespace std;

float sec(float x){
    return 1/cos(x);
}

int main() {
    float e = 2.71828;
    float x, y;
    cin >> x >> y;
    float R = sec(y*y/x);
    float S = pow(e, 1/x)*log(y);

    cout << R << " " << S << endl;
    
    float C;
    C = max(R , S);

    cout << C << endl;
}