// dfa accepting all strings containing
// no. of 0`s divisible by 2 and no. of 1`s divisible by 3

#include <iostream>
#include<bits/stdc++.h>
#include<algorithm>
#include<string>
using namespace std;

int main(){
    string  s , output;
    int cnt0 = 0 , cnt1 = 0;
    cin>> s;
    for(char i=0;i<(s.length());i++){
        if(s[i]=='1'){
            cnt1++;
        }
        else{
            cnt0++;
        }
    }
    
    if(cnt0%2==0 && cnt1%3==0){
        cout<<"String is valid"<<endl;
    }
    else{
        cout<<"String is invalid"<<endl;
    }
  
    return 0;
}
