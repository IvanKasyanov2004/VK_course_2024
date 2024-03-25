#include <iostream>
using namespace std;

#ifndef N
#define N 5
#endif

void showArray(int (&a)[N]){
    for (int i = 0; i < N; i++){
        std::cout << a[i] << " ";
    }
}

void reverseArray(int (&arr)[N]){
    int left = 0;
    int right = N - 1;
    while (left < right){
        swap(arr[left], arr[right]);
        left++;
        right--;
    }
}

int main(){
    int a[N] = {1, 2, 3, 4, 5};
    showArray(a);
    reverseArray(a);
    cout << "-> ";
    showArray(a);
}