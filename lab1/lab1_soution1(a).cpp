// contain 3 consecutive zeros
// dfa containing 3 consecutive zeros ( anywhere in string )


#include <iostream>
#include<bits/stdc++.h>
#include<algorithm>
using namespace std;

int main(){
    string  s , output;
    int cnt=0,ans = 0;
    cin>> s;
    for(char i : s){
        if(i == '0'){
            cnt++;
            ans = std::max(cnt,ans);
        }
        else{
            cnt = 0;
        }
    }
    
    output = (ans>=3)?"String is valid" : "String is invalid";
    cout<<output<<endl;
    return 0;
}
