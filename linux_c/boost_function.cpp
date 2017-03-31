//Boost::function是一个函数包装器，也即一个函数模板，
//可以用来代替拥有相同返回类型，相同参数类型，以及相同参数个数的各个不同的函数
//这样在不同的地方用不同的函数来替代 f 可以得到类似于C++中多态的效果

#include <iostream>
#include <string>
#include "boost/function.hpp"

int fsum(int i, int j)
{
    return i + j;
}

class Person
{
public:
    void operator() (std::string name, int age)
    {
        std::cout << name << ": " << age << std::endl;
    }
};

class Car
{
public:
    Car(){}
    virtual ~Car(){}
    void info(int i)
    {
        std::cout << "info = " << i << std::endl;
    }
};

int main()
{
    // 1. 普通函数
    boost::function<int(int, int)> func1;
    func1 = fsum;
    std::cout << "4 + 5 = " << func1(4, 5) << std::endl;

    // 2. 函数对象
    boost::function<void(std::string, int)> func2;
    Person person;
    func2 = person;
    func2("myname", 30);

    // 3. 成员函数
    boost::function<void(Car*, int)> func3;
    func3 = &Car::info;
    Car car;
    func3(&car, 25);

    // 4. 空函数
    boost::function<int(int, int)> func4;
    assert(func4.empty());
    assert(!func1.empty());
    func1.clear();
    assert(func1.empty());
    try
    {
        func1(4, 5);
    }
    catch (std::exception& e)
    {
        std::cout << e.what() << std::endl;
    }
}