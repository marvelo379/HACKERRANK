def minion_game(string):
    vow=['A','E','I','O','U']
    s,k=0,0
    
    
    for i in range(len(string)):
        
        if string[i] in vow:
            
            k=k+len(string)-i
        else:
            s=s+len(string)-i
    if s>k:
        print("Stuart"+" "+"%d"%s)
    elif k>s:
        print("Kevin"+" "+'%d' %k)
    else:
        print("Draw")
        
    
    # your code goes here
******************************
#ants problem


#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'solve' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY V as parameter.
 */

int solve(vector<int> V) {
    int n=V.size(),c=0;
    int x=2*n/2*(n-n/2)*100000;
    sort(V.begin(),V.end());
    for(int i=0;i<n-1;i++){
        if(V[i+1]-V[i]==1){
            c++;
            i++;
            
        }
    }
    if(V[n-1]-V[0]==1){
        c++;
    }
    x=x+c;
    return x*2;
}
    



int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string V_count_temp;
    getline(cin, V_count_temp);

    int V_count = stoi(ltrim(rtrim(V_count_temp)));

    string V_temp_temp;
    getline(cin, V_temp_temp);

    vector<string> V_temp = split(rtrim(V_temp_temp));

    vector<int> V(V_count);

    for (int i = 0; i < V_count; i++) {
        int V_item = stoi(V_temp[i]);

        V[i] = V_item;
    }

    int result = solve(V);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
******************
ABBREVATION PROBLEM............................

#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    m,n=len(a),len(b)
    dp=[[False]*(m+1) for _ in range(n+1)]
    dp[0][0]=True
    for i in range(n+1):
        for j in range(m+1):
            if i==0 and j!=0:
                dp[i][j]=a[j-1].islower() and dp[i][j-1]
            elif i!=0 and j!=0:
                if(a[j-1]==b[i-1]):
                    dp[i][j]=dp[i-1][j-1]
                elif a[j-1].upper()==b[i-1]:
                    dp[i][j]=dp[i-1][j-1] or dp[i][j-1]
                elif not(a[j-1].isupper() and b[i-1].isupper()):
                    dp[i][j]=dp[i][j-1]
    return "YES" if dp[n][m] else "NO"                
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input().strip())

    for q_itr in xrange(q):
        a = raw_input()

        b = raw_input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
