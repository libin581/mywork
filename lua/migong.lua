local room1, room2, room3, room4
function room1 () 
    print("enter room1")
    local move = io.read() 
    if move == "south" then 
        return room3() 
    elseif move == "east" then 
        return room2() 
    else 
        print("invalid move") 
        return room1()   -- stay in the same room 
    end 
end 
 
function room2 () 
    print("enter room2")
    local move = io.read() 
    if move == "south" then 
        return room4() 
    elseif move == "west" then 
        return room1() 
    else 
        print("invalid move") 
        return room2() 
    end 
end 

function room3 () 
    print("enter room3")
    local move = io.read() 
    if move == "north" then 
        return room1() 
    elseif move == "east" then 
        return room4() 
    else 
        print("invalid move") 
        return room3() 
    end 
end

function room4 () 
    print("enter room4")
    print("congratilations!") 
end

room1()