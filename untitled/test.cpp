#include <iostream>
using namespace std;
int Max(int a,int b){
    int result;
    if (a>b)
        return a;
    else
        return b;
}
int main() {
    int c = 10;
    int c1 = 100;
    int c2;
    c2 = Max(c,c1);
//  cout<<Max(c,c1);
    cout<<c2;
}
