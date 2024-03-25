#include <iostream>
using namespace std;

#ifndef N
#define N 7
#endif
#ifndef M
#define M 5
#endif

void showArrayMN(int (&a)[M + N]){
    for (int i = 0; i < M + N; i++){
        std::cout << a[i] << " ";
    }
}
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

//слияние двух массивов с дополнительной аллокацией памяти
void mergeArrays(int (&a)[N], int (&b)[M], int (&c)[M + N]){
    for(int i = 0; i < M + N; i++){
        c[i] = 0;
    }
    int i = 0;
    int j = 0;
    while(i < N and j < M){
        if(a[i] <= b[j]){
            c[i + j] = a[i];
            i += 1;
        }
        else{
            c[i + j] = b[j];
            j += 1;
        }
    }
    while(i < N){
        c[i + j] = a[i];
        i += 1;
    }
    while(j < M){
        c[i + j] = b[j];
        j += 1;
    }
}

int main(){
    int a1[N] = {1, 2, 3, 4, 5, 7, 10};
    int b1[M] = {0, 2, 5, 20, 30};
    int c1[M + N];
    showArrayN(a1);
    cout << ", ";
    showArrayM(b1); 
    cout << "-> ";
    mergeArrays(a1, b1, c1);
    showArrayMN(c1);
    cout << endl;

    int a2[N] = {1, 2, 3, 4, 5, 7, 10};
    int b2[M] = {0, 0, 0, 0, 0};
    int c2[M + N];
    showArrayN(a2);
    cout << ", ";
    showArrayM(b2); 
    cout << "-> ";
    mergeArrays(a2, b2, c2);
    showArrayMN(c2);
}