//http://blog.163.com/bical@126/blog/static/479354942011026105222733/

#include <iostream>
#include <cassert>
#include <string>
#include "boost/regex.hpp"

int main() {
  // 3 digits, a word, any character, 2 digits or "N/A", 
  // a space, then the first word again
  boost::regex reg("\\d{3}([a-zA-Z]+).(\\d{2}|N/A)\\s\\1");
  
  std::string correct="123Hello N/A Hello";
  std::string incorrect="123Hello 12 hello";
  
  assert(boost::regex_match(correct,reg)==true);
  assert(boost::regex_match(incorrect,reg)==false);
  
  //--------------------------------------------------------
  // "new" and "delete" 出现的次数是否一样？
  boost::regex reg2("(new)|(delete)");
  boost::smatch m;
  std::string s=
    "Calls to new must be followed by delete. \
     Calling simply new results in a leak!";
  int new_counter=0;
  int delete_counter=0;
  std::string::const_iterator it=s.begin();
  std::string::const_iterator end=s.end();

  while (boost::regex_search(it,end,m,reg2)) {
    // 是 new 还是 delete?
    m[1].matched ? ++new_counter : ++delete_counter;
    it=m[0].second;
  }

  if (new_counter!=delete_counter)
    std::cout << "Leak detected!\n";
  else
    std::cout << "Seems ok...\n";
  
  //---------------------------------------------------------
   boost::regex reg3("(Colo)(u)(r)",
    boost::regex::icase|boost::regex::perl);
  
  std::string s2="Colour, colours, color, colourize";

  s=boost::regex_replace(s2,reg3,"$1$3");
  std::cout << s2 << "\n";
  
}