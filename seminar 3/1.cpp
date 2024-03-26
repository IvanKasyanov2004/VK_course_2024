#include <iostream>
using namespace std;

//скопировать n листов за наименьшее время, x, y - сколько минут на 1 лист
int copyTime(int n, int x, int y){ 
    int left = 0;
    int right = (n - 1) * max(x, y); //определили левую и правую границы вpeмени

    int middle;
    while(left + 1 < right){
        middle = (left + right) / 2;
        if(middle / x + middle / y < n - 1){
            left = middle; //если успевает за это время напечатать n - 1, то сдвигаем
        }
        else{
            right = middle;
        }
    }

    return right + min(x, y); //так как нужно скопировать один лист, чтобы загрузить 2 принтера
}

int main(){
    int n = 10;
    int x = 2;
    int y = 1;
    cout << "n = " << n << ", x = " << x << ", y = " << y << " -> " << copyTime(n, x, y) << endl;

    x = 1; y = 1;
    cout << "n = " << n << ", x = " << x << ", y = " << y << " -> " << copyTime(n, x, y) << endl;

    n = 1, x = 10; y = 1;
    cout << "n = " << n << ", x = " << x << ", y = " << y << " -> " << copyTime(n, x, y) << endl;
}