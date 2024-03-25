#include <iostream>
using namespace std;

#ifndef N
#define N 7
#endif

void showArray(int (&a)[N]){
    for (int i = 0; i < N; i++){
        std::cout << a[i] << " ";
    }
}

void reverseArray(int (&arr)[N], int left_idx, int right_idx){
    int left = left_idx;
    int right = right_idx;
    while (left < right){
        swap(arr[left], arr[right]);
        left++;
        right--;
    }
}

void reversePartOfArray(int (&arr)[N], int k){
    //развернули весь массив, развернули первую половину, развернули вторую половину
    //еслиk k > n, то k = k mod n
    if (k > N) { k = k % N; }
    reverseArray(arr, 0, N - 1);
    reverseArray(arr, 0, k - 1);
    reverseArray(arr, k, N - 1);
}



int main(){
    int arr1[N] = {1, 2, 3, 4, 5, 6, 7};
    showArray(arr1);
    cout << "(k = 3) -> ";
    reversePartOfArray(arr1, 3);
    showArray(arr1);
    cout << endl;

    int arr2[N] = {1, 2, 3, 4, 5, 6, 7};
    showArray(arr2);
    cout << "(k = 10) -> ";
    reversePartOfArray(arr2, 10);
    showArray(arr2); 
}