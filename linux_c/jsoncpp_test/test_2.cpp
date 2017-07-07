#include<json/json.h>  
#include<iostream>  
using namespace std;  
  
int main(int argc, char** argv)  
{      
    Json::Value root;  
    Json::FastWriter fast;  
    Json::Value json_temp;// 临时对象，供如下代码使用  
    json_temp["name"] = Json::Value("helloworld");  
    json_temp["age"] = Json::Value(26);  
					  
    root["a"]= Json::Value("1");//字符型.新建一个 Key（名为：a），赋予字符串值："value_string"。  
    root["b"]= Json::Value(2);//数字  
    root["c"]= Json::Value(false);//新建一个 Key（名为：c），赋予bool值：false。  
    root["d"]= Json::Value(3.14);//新建一个 Key（名为：d），赋予 double 值：3.14  
    root["key_object"]= json_temp;//新建一个 Key（名为：key_object），赋予 json::Value 对象值  
    root["key_array"].append("array_string");// 新建一个 Key（名为：key_array），类型为数组，对第一个元素赋值为字符串："array_string"。  
    root["key_array"].append(1234);  
												    
    cout<<fast.write(root)<<endl;  
    Json::StyledWriter styled_writer;//另一种格式化的方式,输出结果的格式不一样  
    cout << styled_writer.write(root) <<endl;  
    //  
    cout<<"读取root中各个成员的信息:"<<endl;  
    string a = root["a"].asString();  
    cout<<"a的值:"<<a<<endl;  
    string name=root["key_object"]["name"].asString();  
    cout<<"读取子节点信息:"<<name<<endl;  
    //Json::Reader 是用于读取的，说的确切点，是用于将字符串转换为 Json::Value 对象的  
    cout<<"以下展现读操作:"<<endl;  
    Json::Reader reader;  
    Json::Value json_object;  
    Json::Value json_object1;  
    const char* json_document = "{\"age\": 26,\"name\" :\"helloworld\"}";  
    const char *json_my = "{\"candidates\":[{\"accesskey\":\"BC75CA64\",\"adjust\":0,\"duration\":278000,\"id\":\"16080455\",\"score\":60,\"singer\":\"席琳迪翁\",\"song\":\"my heart will good go on\",\"uid\":\"1000000010\"}],\"info\":\"OK\",\"keyword\":\"Céline Dion - My Heart Will Go On\",\"proposal\":\"16080455\",\"status\":200}";  
    if (!reader.parse(json_document, json_object))  
        return 0;  
    cout << json_object["name"];//自带换行?  
    cout << json_object["age"] << endl;  
																							  
    if (!reader.parse(json_my, json_object1))  
        return 0;  
    Json::StyledWriter styled_writer1;//另一种格式化的方式,输出结果的格式不一样  
    cout << json_object1["keyword"];//自带换行?  
    cout << styled_writer1.write(json_object1) <<endl;  
    return 0;  
						    
}  
