//http://blog.csdn.net/doon/article/details/9113851
#include <iostream>
#include <boost/signal.hpp>  
#include <boost/bind.hpp>

void helloworld() {
    std::cout << "Hello, World!(func)" << std::endl;
}

struct HelloWorld {
    void operator() () const
    {
        std::cout << "Hello, World!" << std::endl;
    }
};

void printMore(const std::string& user)
{
    std::cout << user << " say: Hello World!\n";
}


boost::signal<void ()>sig;

int main()
{
    boost::signals::connection c = sig.connect(&helloworld);
    
    HelloWorld hello;
    sig.connect(hello);
        
    sig.connect(boost::bind(printMore, "Tom"));  
    sig.connect(boost::bind(printMore, "Jerry"));
    
    c.block();
    sig();
    
    c.unblock();
    sig();
    
    c.disconnect();
}

