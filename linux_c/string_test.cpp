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
#include <string.h>

using namespace std;


//注意：当字符串为空时，也会返回一个空字符串
void split(string& s, string& delim,vector< string >* ret)
{
    size_t last = 0;
    size_t index=s.find_first_of(delim,last);
    while (index!=string::npos)
    {
        ret->push_back(s.substr(last,index-last));
        last=index+1;
        index=s.find_first_of(delim,last);
    }
    if (index-last>0)
    {
        ret->push_back(s.substr(last,index-last));
    }
}

string&   replace_all(string&   str,const   string&   old_value,const   string&   new_value)
{
    while (true)   {
        string::size_type   pos(0);
        if (   (pos=str.find(old_value))!=string::npos   )
            str.replace(pos,old_value.length(),new_value);
        else   break;
    }
    return   str;
}

int str2str_PreRemoveZero(        const char* pIn, 
                                char* pOut)
{
	if ( NULL == pOut )
	{
		return -1;;
	}

    const char * pTmp = pIn;
    while(*pTmp == '0')
    {
        pTmp++;
    }

    strcpy(pOut, pTmp);
}

int main()
{
    char str[10];
    sprintf(str,"%d",123);
    cout<<strlen(str)<<endl;
    string str2=str;

    printf("%s,%d,%d\n",str2.c_str(),sizeof(str2.c_str()), str2.length());

    string::iterator iter=str2.begin();
    while (iter!=str2.end())
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

    if ('8' == str2[str2.size()-1]) {
        cout<<"last of str2 is '8'"<<endl;
    }

    string str6;
    str6.resize(str2.size()+1);
    strcpy((char *)str6.c_str(),str2.c_str());
    str6+="+++";
    str6.append("_");
    str6 = str6+",";
    cout<<str6<<endl;


    //char ServiceUsage[] = "2000000002|1357|6144|6144|0";
    char ServiceUsage[] = "2000000001|3|99|925|0;2000000009|3|465|1583|0;1030000020|3|546|478|0";
    char *pServiceUsage = ServiceUsage;
    while(*pServiceUsage != '\0'){
        if (*pServiceUsage == ';'){
            *pServiceUsage = '|';
        }
        pServiceUsage++;
    }   

    string strServiceUsage = ServiceUsage;
    string strdelim = "|";
    vector<string> strParts;
    split(strServiceUsage, strdelim, &strParts);
	cout<<"tet"<<strParts[3]<<" "<<strParts[6]<<endl;
    cout<<endl;
    int partIdx=0;
    string strNewServiceUsage;
    for (vector<string>::iterator it=strParts.begin(); it !=strParts.end(); it++) {
        if (partIdx%5 == 0) {
            *it = "N" + *it;
        }

        strNewServiceUsage += *it + ",";
        partIdx++;
    }
    strNewServiceUsage=strNewServiceUsage.substr( 0 , strNewServiceUsage.size()-1);
	cout<<ServiceUsage<<endl;
    cout<<strNewServiceUsage;
    cout<<endl;

    cout<<"--------------------------"<<endl;

    string strtest;
	if (strtest.empty()){
	cout<<"strtest is empty"<<endl;
	}

   char s[] = "a,b*c,d";
   const char *sep = ",*"; //可按多个字符来分割
   char *p;
   p = strtok(s, sep);
   while(p){
       printf("%s ", p);
       p = strtok(NULL, sep);
   }
   printf("\n");

   char aa[] = "ab";
   printf("atoi(%s) = %d\n", aa, atoi(aa));
 
   char bb[] = "00123";
   long long lltmp;
   sscanf(bb, "%lld",&lltmp); 
   printf("atoll(%s) = %lld\n", bb, lltmp);

   cout<<"=================="<<endl;
   
   char cc[10]="00012345";
   char dd[10];
   str2str_PreRemoveZero(cc, dd);
   printf("%s-->%s\n\n", cc, dd);
   
   char ee[10]="1234";
   char ff[10];
   str2str_PreRemoveZero(ee, ff);
   printf("%s-->%s\n\n", ee, ff);
   
    return 0;
}


