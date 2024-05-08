#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <vector>
using namespace std;


vector<vector<string>> groupAnagrams(vector<string> strs) {
    unordered_map<string, vector<int>> Map; // ключ - отсортированная строка, значение - вектор индексов анаграмм
    for(int i = 0; i < strs.size(); ++i){
        string sorted = strs[i];
        sort(sorted.begin(), sorted.end()); // отсортировали строку
        if(Map.find(sorted) == Map.end()){ // если ключа нет, добавляем его в мапу
            Map[sorted] = vector<int>();
        }
        Map[sorted].push_back(i); // добавляем индекс в вектор анаграмм для данного ключа
    }

    vector<vector<string>> answer;  //заполняем ответ
    for(const auto& pair : Map){   //проходимся по парам ключ-значение
        vector<string> anagrams;  
        for(int i : pair.second){  //заполняем вектор анаграмм
            anagrams.push_back(strs[i]);
        }
        answer.push_back(anagrams); // добавляем вектор анаграмм в ответ
    }

    return answer;
}

void printAnswer(vector<vector<string>> answer) {
    for(const auto& group : answer){
        cout << "[";
        for(int i = 0; i < group.size(); ++i){
            cout << group[i];
            if (i < group.size() - 1) {
                cout << ", ";
            }
        }
        cout << "]" << endl;
    }
}

int main() {
    vector<string> strs1 {"eat","tea","tan","ate","nat","bat"};
    printAnswer(groupAnagrams(strs1));

    vector<string> strs2 {"won","now","aaa","ooo","ooo"};
    printAnswer(groupAnagrams(strs2));
}