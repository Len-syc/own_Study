#include <iostream>
using namespace std;
class MylenQin{
public:

};
int main(){
    int x = 10;
    int y = 10;
    typedef int LenQin;
    enum Account{
        a = 100,
        b = 101,
        c = 1012,
    } test;
    test = a;
    cout <<test<<endl;
    test = b;
    cout <<test;
    float f = static_cast<float>(test);
    cout<<f;
    Base* base = new Derived;
    Derived* derived = dynamic_cast<Derived*>(base);
    if (derived) {
        // 如果检查发现它确实是有按钮的积木（derived不为空）
        derived->sayHello(); // 你可以按按钮让它发声
    } else {
        // 如果检查发现它只是普通的方块（derived为空）
        cout << "这个积木没有特别的功能" << endl;
    }
}