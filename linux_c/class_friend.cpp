#include <string>
#include <iostream>
using namespace std;

//----------------------friend function----------------
class example; // 这里必须对类 example 做前向声明，否则下面的函数声明将报错
void reset(example &e);

class example
{
public:
    friend void reset(class example &e);
private:
    int n;
};

// 该函数定义必须放在类 example 的后面，否则无法解析变量n
void reset(example &e)
{
    e.n = 0;
}
//-----------end friend funciton--------------

//---------------friend class----------------
class woman; // 前向声明

class man
{
public:
    void disp(woman &w);
    void reset(woman &w);
};

class child
{
public:
    void disp(woman &w);
};


class woman
{
public:
    friend class man; // 将man设为woman的友元类，这样man对象的任何成员函数都可以访问woman的私有成员
    friend void child::disp(woman &w);
	void setName(string &str);
private:
    string name;
};

void woman::setName(string &str)
{
	name=str;
}

void man::disp(woman &w)
{
    cout << "man say: "<<w.name << endl;
}

void man::reset(woman &w)
{
    w.name.clear();
}

void child::disp(woman &w)
{
    cout <<"child say: "<< w.name << endl;
}

//---------------end of friend class-------------

int main()
{
	woman A;
	string name("Lily");
	A.setName(name);
	man B;
	child C;
	B.disp(A);
	C.disp(A);
	B.reset(A);
	C.disp(A);
}
