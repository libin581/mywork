//函数模板包含各种返回类型，函数参数个数，参数类型不同的各种函数
//typedef boost::function<void()> Func;
//or
//typedef boost::function<void(void)> Func;
//注意Func没有返回值，不能获取实例函数的返回值
//也不能传入参数


#include<boost/function.hpp>
#include<boost/bind.hpp>
#include<iostream>

typedef boost::function<void(void)> Func;

int test(int num)
{
   std::cout<<"In test:"<<num<<std::endl;    
}

int cpp(int *ptr)
{
    std::cout<<"In CPP"<<std::endl;    
    return 10;
}

int main()
{
  Func f;
  f=boost::bind(test,6);
  f(); //f(6)
  
  f.clear();
  
  int *ptr = NULL;
  f=boost::bind(cpp,ptr);
  f();
}