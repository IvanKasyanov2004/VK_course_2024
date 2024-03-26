#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool isPalindrome(const string& s) {
    stack<char> stack;
    
    for(char ch : s){ //заполняем стек LIFO
        stack.push(ch);
    }
    
    for(char ch : s){
        if(ch != stack.top()){  //извлекаем из стека и сравниваем со строкой
            return false;
        }
        stack.pop();
    }
    
    return true;
}

int main(){
    string str = "aboba";
    cout << str << " -> ";
    if(isPalindrome(str)){
        cout << "True" << endl;
    }else{
        cout << "False" << endl;
    }
    
    str = "aboda";
    cout << str << " -> ";
    if(isPalindrome(str)){
        cout << "True" << endl;
    }else{
        cout << "False" << endl;
    }
}