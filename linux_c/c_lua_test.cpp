#include <time.h> 
 
extern "C"  
{  
#include "lua.h"  
#include "lualib.h"  
#include "lauxlib.h"  
}/* Lua解释器指针 */  
 
const char LUA_SCRIPT[] =  
    "function loop_add(a, b)            "  
    "   local sum = 0                   "  
    "   for i = 1, 10000000 do          "  
    "       sumsum = sum + a + b           "  
    "   end                             "  
    "   return sum                      "  
    "end                                "  
    "                                   "  
    "function add(a, b)                 "  
    "   return a + b                    "  
    "end                                "  
    ;  
 
// lua 脚本里面的函数由C调用  
int use_lua_add(lua_State *L, const char *func_name, int x, int y)  
{  
    int sum;                        /* 通过名字得到Lua函数 */  
    lua_getglobal(L, func_name);    /* 第一个参数 */  
    lua_pushnumber(L, x);           /* 第二个参数 */  
    lua_pushnumber(L, y);           /* 调用函数，告知有两个参数，一个返回值 */  
    lua_call(L, 2, 1);              /* 得到结果 */  
    sum = (int)lua_tointeger(L, -1);  
    lua_pop(L, 1);  
    return sum;  
}  
 
int main()  
{  
    int i, sum = 0;  
    clock_t tStart, tStop;  
 
    lua_State *L = lua_open();  /* opens Lua */  
    luaL_openlibs(L);  
    if (luaL_dostring(L, LUA_SCRIPT))  // Run lua script  
    {  
        printf("run script failed/n");  
        lua_close(L);  
        return -1;  
    }  
 
    sum = 0;  
    tStart = clock();  
    for (i = 0; i < 10000000; i++)  
    {  
        sum += 1 + 1;  
    }  
    tStop = clock();  
    printf("C++: %dms./nThe sum is %u./n",  
           (tStop - tStart) * 1000 / CLOCKS_PER_SEC, sum);  
 
    sum = 0;  
    tStart = clock();  
    sum = use_lua_add(L, "loop_add", 1, 1);  
    tStop = clock();  
    printf("Lua loop_add: %dms./nThe sum is %u./n",  
           (tStop - tStart) * 1000 / CLOCKS_PER_SEC, sum);  
             
    sum = 0;  
    tStart = clock();  
    for (i = 0; i < 10000000; i++)  
    {  
        sum += use_lua_add(L, "add", 1, 1);  
    }  
    tStop = clock();  
    printf("Loop lua add: %dms./nThe sum is %u./n",  
           (tStop - tStart) * 1000 / CLOCKS_PER_SEC, sum);  
    lua_close(L);  
    return 0;  
} 