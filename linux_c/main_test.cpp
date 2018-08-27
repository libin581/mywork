/* C++里面是不是所有的动作都是 main( )函数引起的  
不是。对于C++程序而言，静态变量、全局变量、全局对象的分配早在 main( )函数之前就已
经完成了。所以，并不是所有的动作都是由 main( )引起的，main( )只不过是一个约定的函数
入口，在main( )函数中的代码执行之前，会调用一个由编译器生成的_main( )函数，而_main( )
函数会进行所有全局对象的构造及初始化工作。 */

#include<iostream> 
using namespace std; 

class A 
{ 
     public: 
         A() {cout<<"construct"<<endl;} 
         ~A() {cout<<"destruct"<<endl;} 
}; 
 
A a; 
int main( ) 
{ 
     cout<<"main"<<endl; 
     return 0; 
}

