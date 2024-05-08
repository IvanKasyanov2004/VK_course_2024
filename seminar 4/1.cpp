#include <iostream>
#include <vector>
using namespace std;

void print(vector<int> arr){
    for(int i : arr){
        cout << i << " ";
    }
    cout << endl;
}

//сортировка Шелла - проходимся нескольок раз с разным gap
void ShellSort(vector<int> &arr){
    int n = arr.size();
    int gap = n / 2;
    while(gap > 0){
        for(int cur_pos = 0; cur_pos < n; cur_pos++){  //с одним гэпом двигаемся на 1 шаг вправо, пока не дойдем до конца
            int m_gap = cur_pos;
            while(m_gap >= gap and arr[m_gap] < arr[m_gap - gap]){  //последовательно сравниваем все элементы на расстоянии gap, меняем местами, если еще есть элемент слева и если левый юольше правого
                swap(arr[m_gap], arr[m_gap - gap]);
            }
        }
        gap = gap / 2;
    }
}


int main(){
    vector<int> arr {3, 8, 10, -11, 0, 30, 7};
    ShellSort(arr);
    print(arr);
}