#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;


string extraLetter(string a, string b) {
    unordered_map<char, int> MapB;
    for(char c : b){  //заполняем мапу B  (ключ - буква, значение - сколько раз встречается)
        MapB[c] += 1;
    }

    for(char c : a){  //проходимся по строке A
        if(MapB.find(c) != MapB.end()){  //если элемента с нет, то find вернет end
            MapB[c] -= 1;
        }
    }


    for(const auto& pair : MapB){  //проходимся по парам ключ-значение (буква - индекс)
        if(pair.second > 0){
            return string(1, pair.first);  //конструируем строку с одним значением 
        }
    }

    return "";
}

int main() {
    string a = "abc";
    string b = "abcc";
    cout << extraLetter(a, b) << endl; 
}