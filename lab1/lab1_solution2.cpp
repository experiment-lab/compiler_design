// string contain 'the' in it anywhere in string 
// dfa accept all string containg 'the'
// Ex -->   'these' -> valid string
//          'those' -> invalid string


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
        if(s[i]=='t' && s[i+1]=='h' && s[i+2]=='e'){
            ans = 1;
            break;
        }
    }
    
    output = (ans)?"String is valid" : "String is invalid";
    cout<<output<<endl;
    return 0;
}
