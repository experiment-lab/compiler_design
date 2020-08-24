// substring of 101
// dfa accepting all strings containing 101( anywhere in string ) 

#include <iostream>
#include<bits/stdc++.h>
#include<algorithm>
#include<string>
using namespace std;

int main(){
    string  s , output;
    int ans = 0;
    cin>> s;
    for(char i=0;i<(s.length()-3);i++){
        if(s[i]=='1' && s[i+1]=='0' && s[i+2]=='1'){
            ans = 1;
            break;
        }
    }
    
    output = (ans)?"String is valid" : "String is invalid";
    cout<<output<<endl;
    return 0;
}
