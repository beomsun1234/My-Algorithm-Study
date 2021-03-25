#include <bits/stdc++.h>

using namespace std;

stack<int> s;
queue<int> q;

void stackfunction(){
    s.push(5);
    s.push(2);
    s.push(3);
    s.push(7);
    s.pop();
    s.push(1);
    s.push(2);
    s.pop();

    while (!s.empty())
    {
        cout<<s.top()<<' ';
        s.pop();
    }
}
void queuefuntion()
{
    q.push(5);
    q.push(2);
    q.push(3);
    q.push(7);
    q.pop();
    q.push(1);
    q.push(4);
    q.pop();
    while (!q.empty()){
        cout << q.front() << ' ';
        q.pop();
    }

}

int main(void){
    stackfunction();
    queuefuntion();


}