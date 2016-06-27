#include <iostream>
using namespace std;

class animal
{
public:
	void sleep()
	{
		cout<<"animal sleep"<<endl;
	}

	void breathe()
	{
		cout<<"animal breathe"<<endl;
	}

};

class fish:public animal
{
public:
	void breathe()
	{
		cout<<"fish bubble"<<endl;
	}

	void swim()
	{
		cout<<"fish swim"<<endl;
	}
};


int main()
{
	fish fh;
	animal *pAn=&fh;
	pAn->sleep();
	pAn->breathe();
	fh.sleep();
	fh.breathe();
	fh.swim();
}
	
