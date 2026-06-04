#include<iostream>
#include<stdio.h>
#include<unordered_map>
#include<string>
using namespace std;

int main(){
    int n_t_c;
    unordered_map<string,int> d;
    string k = "OK";
    cin >> n_t_c;
    for (int i = 0; i<n_t_c; i++){
        string s;
        cin >> s;
        if (d.count(s)){
            cout << s + to_string(d[s])<< endl;
            d[s]++;
        }
        else {
            d[s] = 1;
            cout << k << endl;
        }
    }
}
//# check if present in dict, if not set freq = 1 and PRINT OK, if alr present in dict, PRINT NAME+{FREQ}