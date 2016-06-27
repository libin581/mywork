#include <time.h> 
 
extern "C"  
{  
#include "lua.h"  
#include "lualib.h"  
#include "lauxlib.h"  
}/* Lua������ָ�� */  
 
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
 
// lua �ű�����ĺ�����C����  
int use_lua_add(lua_State *L, const char *func_name, int x, int y)  
{  
    int sum;                        /* ͨ�����ֵõ�Lua���� */  
    lua_getglobal(L, func_name);    /* ��һ������ */  
    lua_pushnumber(L, x);           /* �ڶ������� */  
    lua_pushnumber(L, y);           /* ���ú�������֪������������һ������ֵ */  
    lua_call(L, 2, 1);              /* �õ���� */  
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