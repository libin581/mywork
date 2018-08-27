#include <stdio.h>

//定义回调函数 
typedef void (*FunPtr)(void); 
class A    
{ 
  public: 
    //回调函数，必须声明为 static 
    static void callBackFun(void)     
    { 
      printf("This is callback func\n");
    } 
}; 
//设置触发条件，调用回调函数 
void Funtype(FunPtr p) 
{ 
  p( ); 
} 
int main(void) 
{ 
    Funtype(A::callBackFun); 
    return 0;
} 