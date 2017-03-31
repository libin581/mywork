#include <iostream>
#include <string>
#include <boost/shared_ptr.hpp>

using namespace std;

class Book
{
private:
    string name_;

public:
    Book(string name) : name_(name)
    {
        cout << "Creating book " << name_ << " ..." << endl;
    }

    ~Book()
    {
        cout << "Destroying book " << name_ << " ..." << endl;
    }
};

int main()
{   
    cout << "=====Main Begin=====" << endl;
    {
        boost::shared_ptr<Book> myBook(new Book("<<1984>>"));
        cout << "[From myBook] The ref count of book is " << myBook.use_count() << ".\n" << endl;

        boost::shared_ptr<Book> myBook1(myBook);
        cout << "[From myBook] The ref count of book is " << myBook.use_count() << "." << endl;
        cout << "[From myBook1] The ref count of book is " << myBook1.use_count() << ".\n" << endl;

        cout << "Reset for 1th time. Begin..." << endl;
        myBook.reset();
        cout << "[From myBook] The ref count of book is " << myBook.use_count() << "." << endl;
        cout << "[From myBook1] The ref count of book is " << myBook1.use_count() << "." << endl;
        cout << "Reset for 1th time. End ...\n" << endl;

        cout << "Reset for 2th time. Begin ..." << endl;
        myBook1.reset();
        cout << "Reset for 2th time. End ..." << endl;
    }
    cout << "===== Main End =====" << endl;

    return 0;
}