#include <set>
#include <string>
#include <iostream>

using namespace std;

int main()
{
    set<string> set1;
	set1.insert("the");
    set1.insert("and");
    set1.insert("the");

	cout<<"size="<<set1.size()<<endl;
	set<string>::iterator ret=set1.begin();
	for(;ret!=set1.end();ret++)
		cout<<*ret<<" ";
 
    cout<<endl;

    set<string>::iterator set_it=set1.find("the");
    if(set_it != set1.end())
		cout<<"the"<<" is found"<<endl;
	
    if(set1.count("the"))
		cout<<"the"<<" is found"<<endl;

    if(set1.erase("the"))
		cout<<"clear \"the\", "<<"size = "<<set1.size()<<endl;

}
