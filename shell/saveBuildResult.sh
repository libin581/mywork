function saveBuildResult()
{
	echo "Save build result"
	fileName=$(time +%Y%m%d_%H%m%s)
	tar -zcv -f  $fileName.tar.bz2  BIN/
}

