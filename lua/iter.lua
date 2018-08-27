function list_iter (t) 
  local i = 0 
  local n = table.getn(t) 
  return function () 
  i = i + 1 
   if i <= n then return t[i] end 
  end 
end 

t = {10, 20, 30} 
iter = list_iter(t)   -- creates the iterator , 这里参数t 要带上
while true do 
  local element = iter()  -- calls the iterator 
  if element == nil then break end 
 print(element) 
 end 
 
for element in list_iter(t) do 
 print(element) 
end 