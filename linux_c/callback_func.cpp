#include <stdio.h>

//����ص����� 
typedef void (*FunPtr)(void); 
class A    
{ 
  public: 
    //�ص���������������Ϊ static 
    static void callBackFun(void)     
    { 
      printf("This is callback func\n");
    } 
}; 
//���ô������������ûص����� 
void Funtype(FunPtr p) 
{ 
  p( ); 
} 
int main(void) 
{ 
    Funtype(A::callBackFun); 
    return 0;
} 