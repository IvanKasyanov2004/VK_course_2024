#include <iostream>
#include <string>
using namespace std;

bool isPalindrome(const std::string& s){
    int l = 0;
    int r = s.length() - 1;
    
    while(l <= r){
        if(s[l] != s[r]){
            return false;
        }
        l++;
        r--;
    }
    
    return true;
}

int main() {
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