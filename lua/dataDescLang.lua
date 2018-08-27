entry{ 
title = "Tecgraf", 
org = "Computer Graphics Technology Group, PUC-Rio", 
url = "http://www.tecgraf.puc-rio.br/", 
contact = "Waldemar Celes", 
description = [[ 
TeCGraf is the result of a partnership between PUC-Rio, 
the Pontifical Catholic University of Rio de Janeiro, 
and <A HREF="http://www.petrobras.com.br/">PETROBRAS</A>, 
the Brazilian Oil Company. 
TeCGraf is Lua's birthplace, 
and the language has been used there since 1993. 
Currently, more than thirty programmers in TeCGraf use 
Lua regularly; they have written more than two hundred 
thousand lines of code, distributed among dozens of 
final products.]] 
}

function fwrite (fmt, ...) 
  return io.write(string.format(fmt, unpack(arg))) 
end 

function BEGIN() 
io.write([[ 
<HTML> 
<HEAD><TITLE>Projects using Lua</TITLE></HEAD> 
<BODY BGCOLOR="#FFFFFF"> 
Here are brief descriptions of some projects around the 
world that use <A HREF="home.html">Lua</A>. 
]]) 
end 

function entry0 (o) 
 N=N + 1 
  local title = o.title or '(no title)' 
 fwrite('<LI><A HREF="#%d">%s</A>\n', N, title) 
end 

function entry1 (o) 
 N=N + 1 
  local title = o.title or o.org or 'org' 
 fwrite('<HR>\n<H3>\n') 
  local href = '' 
 
 if o.url then 
  href = string.format(' HREF="%s"', o.url) 
 end 
 fwrite('<A NAME="%d"%s>%s</A>\n', N, href, title) 
 
 if o.title and o.org then 
  fwrite('\n<SMALL><EM>%s</EM></SMALL>', o.org) 
 end 
 fwrite('\n</H3>\n') 
 
 if o.description then 
  fwrite('%s', string.gsub(o.description, 
         '\n\n\n*', '<P>\n')) 
  fwrite('<P>\n') 
 end 
 
 if o.email then 
  fwrite('Contact: <A HREF="mailto:%s">%s</A>\n', 
    o.email, o.contact or o.email) 
 elseif o.contact then 
  fwrite('Contact: %s\n', o.contact) 
 end 
end 

function END() 
fwrite('</BODY></HTML>\n') 
end 

BEGIN() 
 
N = 0 
entry = entry0 
fwrite('<UL>\n') 
dofile('db.lua') 
fwrite('</UL>\n') 
 
N = 0 
entry = entry1 
dofile('db.lua') 
 
END() 