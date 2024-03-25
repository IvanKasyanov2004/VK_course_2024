#include <iostream>
using namespace std;

#ifndef N
#define N 9
#endif

void showArray(int (&a)[N]){
    for (int i = 0; i < N; i++){
        std::cout << a[i] << " ";
    }
}

void zeroLast(int (&arr)[N]){ //аналогично задаче 5, но индексы движутся влево
    int j = N - 1;
    for(int i = N - 1; i >= 0; --i){
        if(arr[i] == 0 and arr[j] == 0){ //если j указывает на ноль, то нет смысла делать swap
            j -= 1;
        }
        else if(arr[i] == 0 and arr[j] != 0){  //меняем местами только если j указывает не на ноль
            swap(arr[i], arr[j]);
            j -= 1;
        }
        
    }
}

int main(){
    int a1[N] = {0, 2, 0, 0, 5, 6, 7, 8, 9};
    showArray(a1);
    cout << "-> ";
    zeroLast(a1);
    showArray(a1);
    cout << endl;

    int a2[N] = {0, 2, 0, 4, 0, 3, 0, 0, 0};
    showArray(a2);
    cout << "-> ";
    zeroLast(a2);
    showArray(a2);
    cout << endl;
}