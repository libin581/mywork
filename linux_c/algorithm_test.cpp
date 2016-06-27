#include <algorithm>
#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

bool isShorter(const string &s1, const string &s2)
{
	return s1.size() < s2.size();
}

bool GT6(const string &s)
{
	return s.size() >= 6;
}

int main()
{
	vector<string> sVec;
	sVec.push_back("libin");
	sVec.push_back("huwei");
	sVec.push_back("VIP");
	sVec.push_back("wangpeng");
	sVec.push_back("skdfj");

    vector<string>::const_iterator result=
		find(sVec.begin(),sVec.end(),"VIP");
	cout<<"The value "<<"VIP "
	    << (result==sVec.end()?
		   " is not present" : " is present")
        <<endl;

	string strSum=accumulate(sVec.begin(), sVec.end(), string(""));
	cout<<"sum of sVec: "<<strSum<<endl;

    fill(sVec.begin()+4,sVec.end(),"abab");
	fill_n(back_inserter(sVec),2,"cdcd");
	vector<string>::iterator it=sVec.begin();
	for (;it!=sVec.end();it++)
		cout<<*it<<" ";
	cout<<endl;

    sVec.clear();
    sVec.resize(10);
    string strGrp[]={"the","quick","red","fox",
	     "jump","over","the","slow","red","turtle"};
	int ii=0;
	for(it=sVec.begin();ii<10;it++,ii++)
    {
	    *it=strGrp[ii];
		cout<<strGrp[ii]<<" ";
	}
	cout<<endl;

    sort(sVec.begin(),sVec.end());
    for(it=sVec.begin();it!=sVec.end();it++)
		cout<<*it<<" ";
	cout<<endl;

	vector<string>::iterator end_unique=
		unique(sVec.begin(), sVec.end());
	sVec.erase(end_unique, sVec.end());
    for(it=sVec.begin();it!=sVec.end();it++)
		cout<<*it<<" ";
	cout<<endl;

    stable_sort(sVec.begin(), sVec.end(), isShorter);
    for(it=sVec.begin();it!=sVec.end();it++)
		cout<<*it<<" ";
	cout<<endl;

	vector<string>::size_type wc=count_if(sVec.begin(),
	                 sVec.end(), GT6);
    cout<<wc<<endl;
}

