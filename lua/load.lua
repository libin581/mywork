local  addscript="function dadd(a,b) return a+b  end"
assert(loadstring(addscript))()
print(tostring(dadd(2,3)))

local  script="local ee={[0]={id=0,lv=5,text='yy'},[1]={id=1,lv=3,text='zz'}}  return ee"
local tb=assert(loadstring(script))()
print(tb[0].text)


f = loadstring("i = i + 1") 
i = 0 
f(); print(i)   --> 1 
f(); print(i)   --> 
