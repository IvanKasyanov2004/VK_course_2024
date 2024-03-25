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
//передвинуть четные числа вперед
void evenFirst(int (&arr)[N]){ //индексы первого и последнего в разворачиваемом
    int i = 0;
    int j = 0;
    for(int i = 0; i < N; ++i){
        if(arr[i] % 2 == 0){
            swap(arr[i], arr[j]);
            j += 1;
        }
    }
}


int main(){
    int a1[N] = {1, 2, 3, 4, 5, 6, 7};
    showArray(a1);
    cout << "-> ";
    evenFirst(a1);
    showArray(a1);
    cout << endl;

    int a2[N] = {0, 9, 0, 4, 2, 6, 11};
    showArray(a2);
    cout << "-> ";
    evenFirst(a2);
    showArray(a2);
    cout << endl;
}