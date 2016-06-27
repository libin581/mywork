/*
used for studying and testing
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main()
{
    char str[10];
	sprintf(str,"%d",123);
	cout<<strlen(str)<<endl;
	string str2=str;

	printf("%s,%d\n",str2.c_str(),sizeof(str2.c_str()));

    string::iterator iter=str2.begin();
	while(iter!=str2.end())
	    cout<<*iter++<<" ";
    cout<<endl;
  
    str2.insert(3,4,'c');
	cout<<str2<<endl;

	str2.erase(6,2);
	cout<<str2<<endl;

	string str3("45678");
	str2.assign(str3);
	cout<<str2<<endl;

    cout<<str3.substr(3,3)<<endl;

    str2.append(str3);
	cout<<str2<<endl;

	str2.replace(3,2,"abc");
	cout<<str2<<endl;

    cout<<str2.find("abc")<<endl;

    cout<<str2.find_first_of("678")<<endl;
	cout<<str2.find_first_of("bc")<<endl;

    cout<<str2.size()<<endl;

    char str4[100];
	memcpy(str4, str2.c_str(), str2.size());
	str4[str2.size()]='\0';
	cout<<str4<<endl;

    vector<char> str5(str4,str4+8);
//  stack<char> stk(str5);
//	while(stk.top() != "")
//	    cout<<stk.pop()<<" ";
    cout<<endl;

    if('8' == str2[str2.size()-1]){
		cout<<"last of str2 is '8'"<<endl;
    }

	string str6;
	str6.resize(str2.size()+1);
	strcpy((char *)str6.c_str(),str2.c_str());
	str6+="+++";
	str6.append("_");
	cout<<str6<<endl;


    cout<<"--------------------------"<<endl;

    return 0;
}


