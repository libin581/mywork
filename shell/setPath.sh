#expr index "myScriptPath" "$PATH"
#if [ index >= "1" ]; then
#exit 0
#fi
function setPath()
{
	# if the myScrpty is exit, how to do ?
	myScriptPath=':/home/b2li/myScript'
	PATH="$PATH$myScriptPath"
	echo "$PATH"
}

function main()
{
	setPath
}

main