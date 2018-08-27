--闭包返回的是一个函数

i=3

function aaa()
    i = i + 1
    return i
end

function newCounter() 
  local i = 0 
  --return function ()
  --  i = i + 1
  --  return i
  --  end
  return aaa
end 

 
cc = newCounter()  --注意这里有括号，cc是newCounter的返回函数
                   -- 没有括号相当于newCounter赋给cc
print(cc())  --> 1 
print(cc())  --> 2
print(_G['i'])

-------------------
function Fun1()
    local iVal = 10          -- upvalue
    function InnerFunc1()     -- 内嵌函数
        print(iVal)          --
    end
						  
    function InnerFunc2()     -- 内嵌函数
        iVal = iVal + 10
    end
											   
    return InnerFunc1, InnerFunc2
end


-- 将函数赋值给变量，此时变量a绑定了函数InnerFunc1, b绑定了函数InnerFunc2
local a, b = Fun1()
 
-- 调用a
a()          -->10
  
-- 调用b
b()          -->在b函数中修改了upvalue iVal
   
-- 调用a打印修改后的upvalue
a()          -->20

