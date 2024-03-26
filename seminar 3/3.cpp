#include <iostream>
using namespace std;

int binarySearchSqrt(int target) {
    int l = 0;
    int r = target;

    while(l <= r){
        int middle = (l + r) / 2;

        if(middle * middle > target){
            r = middle - 1;
            continue; //continue - возвращение к началу while
        }

        if(middle * middle < target){
            l = middle + 1;
            continue;
        }

        return middle; //middle * middle == target (оставшийся случай)
    }

    return r;
}

int main(){
    int target = 9022;
    int result = binarySearchSqrt(target);
    cout << target << " -> " << result << endl;

    target = 100;
    result = binarySearchSqrt(target);
    cout << target << " -> " << result << endl;

    target = 0;
    result = binarySearchSqrt(target);
    cout << target << " -> " << result << endl;
}