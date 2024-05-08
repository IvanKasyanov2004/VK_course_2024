#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

void print(vector<int> arr){
    for(int i : arr){
        cout << i << " ";
    }
    cout << endl;
}

vector<int> twoSum(vector<int> arr, int target) {
    unordered_map<int, int> Map;
    for(int i = 0; i < arr.size(); ++i){
        Map[arr[i]] = i;  //заполняем мапу ключ - значение элмеента массива, значение - индекс числа
    }
    for(int i = 0; i < arr.size(); ++i){  //проходимся по всем элементам 
        int diff = target - arr[i]; 
        if(Map.find(diff) != Map.end() and Map[diff] != i){  //если есть элемент, который в сумме с i-тым дает target, то возвращаем эти два
            return vector<int> {i, Map[diff]};  //возвращаем индексы элементов
        }
    }
    return vector<int> {};
}

int main() {
    vector<int> arr {0, -3, 4, 5, 4, -6, 2};
    print(twoSum(arr, 9));
    print(twoSum(arr, 0));
    print(twoSum(arr, 4));
}