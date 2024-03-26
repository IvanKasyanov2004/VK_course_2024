#include <iostream>
#include <string>
#include <stack>
using namespace std;

//аналогично задаче со скобками
string removeDuplicates(const string& s) {
    stack<char> charStack; //создаем стек
    
    for(char c : s){ //проходимся по всем элементам
        if(!charStack.empty() and c == charStack.top()){  //если стек не пустой и в нем уже есть эта буква то удаляем
            charStack.pop();
        }else{   //если буква другая или стек пустой (первый элемент), добавляем стек
            charStack.push(c);
        }
    }
    
    string result;  //создаем строку из элементов стека
    while(!charStack.empty()){
        result = charStack.top() + result;
        charStack.pop();
    }
    
    return result;
}

int main() {
    string str1 = "cdffd";
    string str2 = "uioouiouuo";
    string str3 = "fqffqzzsd";
    
    cout << str1 << " -> " << removeDuplicates(str1) << endl;
    cout << str2 << " -> " << removeDuplicates(str2) << endl;
    cout << str3 << " -> " << removeDuplicates(str3) << endl;
    
    return 0;
}