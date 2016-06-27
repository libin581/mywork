#include <stdio.h>

/* ENVIRON 变量包含了整个环境。*/
extern char** environ;

int main ()
{
      char** var;
      for (var = environ; *var != NULL; ++var) {
          printf("%s\n", *var);
      }
      return 0;
}
