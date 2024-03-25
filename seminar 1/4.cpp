#include <iostream>
using namespace std;

#ifndef N
#define N 3
#endif
#ifndef M
#define M 7
#endif

void showArrayM(int (&a)[M]){
    for (int i = 0; i < M; i++){
        std::cout << a[i] << " ";
    }
}
void showArrayN(int (&a)[N]){
    for (int i = 0; i < N; i++){
        std::cout << a[i] << " ";
    }
}

//слияние без выделения памяти
void mergeArrays(int (&arr1)[M], int (&arr2)[N]){  //идем справа налево и заполяем массив  (третий указатель в самый конец, и на место его ставим новые элементы)
    int p1 = M - N - 1;
    int p2 = N - 1;
    int p3 = M - 1;
    while(p2 >= 0){
        if (p1 >= 0 and arr1[p1] > arr2[p2]){
            arr1[p3] = arr1[p1];
            p1 -= 1;
        }
        else {
            arr1[p3] = arr2[p2];
            p2 -= 1;
        }
        p3 -= 1;
    }
}

int main(){
    int a1[N] = {1, 7, 8};
    int b1[M] = {3, 8, 10, 11, 0, 0, 0};
    showArrayN(a1);
    cout << ", ";
    showArrayM(b1); 
    cout << "-> ";
    mergeArrays(b1, a1);
    showArrayM(b1);
    cout << endl;

    int a2[N] = {1, 10, 28};
    int b2[M] = {3, 8, 10, 11, 0, 0, 0};
    showArrayN(a2);
    cout << ", ";
    showArrayM(b2); 
    cout << "-> ";
    mergeArrays(b2, a2);
    showArrayM(b2);
}