function dec2hex_ip(decIp)
	local hexIp="";
	
    local nFindStartIndex = 1 
    local splitTable = {}
    local nSplitIndex = 1
    while true do  
        local nFindLastIndex = string.find(decIp, "%.", nFindStartIndex)  
        if not nFindLastIndex then  
			splitTable[nSplitIndex] = string.sub(decIp, nFindStartIndex)  
            break  
        end  
        splitTable[nSplitIndex] = string.sub(decIp, nFindStartIndex, nFindLastIndex - 1)  
        nFindStartIndex = nFindLastIndex + 1
        nSplitIndex = nSplitIndex + 1  
    end  
    
	if nSplitIndex >= 4 then
		for i = 1, 4 do
			hexIp = hexIp .. string.format("%02X",splitTable[i]);
		end
	end
    return hexIp;
end	
	
local testip="10.1.130.54"
local hexip=dec2hex_ip(testip)
print(hexip)

testip="10.1.43"
hexip=dec2hex_ip(testip)
if string.len(hexip) == 0 then
print("empty string")
end