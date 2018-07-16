#include <map>
#include <string>
#include <iostream>

using namespace std;

int main()
{
    map<string, int> word_count;
    word_count["sdf"]=3;
	word_count["sdfjk"]=5;
	map<string, int>::iterator map_it=word_count.begin();
	for (;map_it!=word_count.end();map_it++)
	    cout<<map_it->first<<"   "<<map_it->second<<endl;

    cout<<"-----------------"<<endl;
	map<string,string> aa_test;
	string strT = aa_test["sdla"];
	if (strT.empty())
    	cout<<"strT is empty"<<endl;
	if (aa_test.count("a") == 0)
    	cout<<"aa_test has no key \"a\" "<<endl;
    cout<<"-----------------"<<endl;

    pair<map<string, int>::iterator,bool> ret=
	        word_count.insert(make_pair("sdf",6));
	
	if (!ret.second)
	   ret.first->second += 6;
    
	cout<<"sdf"<<"    "<<word_count["sdf"]<<endl;
	cout<<"sdft"<<"    "<<word_count["sdft"]<<endl;

    word_count.insert(make_pair("sdf",10));
   
	for (map_it=word_count.begin();map_it!=word_count.end();map_it++)
	    cout<<map_it->first<<"   "<<map_it->second<<endl;
    
	int occurs=0;
	if (occurs=word_count.count("sdf"))
		cout<<occurs<<endl;
 
    map<string,int>::iterator it=word_count.find("sdf");
	if (it != word_count.end())
		cout<<"find"<<endl;

    if (word_count.erase("sdf"))
		cout<<"OK: "<<"sdf"<<" removed\n";
	else cout<<"not OK: "<<"sdf"<<" not found!\n";

    cout<<"======================================="<<endl;

    multimap<string, int> name_phone;
    name_phone.insert(make_pair("libin", 189239));
    name_phone.insert(make_pair("libin", 1239));
    name_phone.insert(make_pair("liwei", 1349));
    name_phone.insert(make_pair("liwei", 139949));
    name_phone.insert(make_pair("liwei", 13098298449));

	multimap<string, int>::iterator multimap_it=name_phone.begin();
	for (;multimap_it!=name_phone.end();multimap_it++)
	    cout<<multimap_it->first<<"   "<<multimap_it->second<<endl;
    
	occurs=0;
	if (occurs=name_phone.count("liwei"))
		cout<<"liwei occurs times: "<<occurs<<endl;
    
	cout<<"phones for liwei:"<<endl;
	multimap<string,int>::iterator mul_it=name_phone.find("liwei");
    for (int ii=0;ii<occurs;ii++,mul_it++)
        cout<<mul_it->second<<" "<<endl;

    cout<<endl;

    if (name_phone.erase("libin3"))
		cout<<"libin3 is erased"<<endl;
    else 
	    cout<<"libin3 is not exist"<<endl;

	cout<<"phones for liwei:"<<endl;
	multimap<string,int>::iterator beg=name_phone.lower_bound("liwei");
	multimap<string,int>::iterator end=name_phone.upper_bound("liwei");
    while(beg!=end){
		cout<<beg->second<<endl;
        beg++;
	}

}

