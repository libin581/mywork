#! /usr/bin/perl
# 该脚本在并行处理上有些问题，需要改进


if (@ARGV < 2){
    &help();
    exit 0;
}

$oldString=shift @ARGV;
$newString=shift @ARGV;
$path="./";

#$fileList = `grep $oldString -rl $path`;
$fileList = `find $path -type f`;

@fileArray=split(/\n+/, $fileList);
#print "@fileArray\n";
$processNum=50;
$fileNumAll=@fileArray;
print "fileNumAll: $fileNumAll\n";
$fileNumSplit=$fileNumAll/$processNum;
$fileNumSplit = (int($fileNumSplit) == $fileNumSplit ? $fileNumSplit : int($fileNumSplit) + 1);
print "fileNumSplit: $fileNumSplit \n";

for (my $idx=0; $idx<$processNum; $idx++) {
    #print "$idx, $fileNumSplit\n";
    @splitFileListArray=@fileArray[$idx*$fileNumSplit..($idx+1)*$fileNumSplit-1];
    #print "@splitFileListArray\n";
    $splitFileList = join(" ", @splitFileListArray);
    #print "$splitFileList\n";
    print "start process: $idx\n";
    system("sed -i \"s\/$oldString\/$newString\/g\" $splitFileList &");
}

sub help{
    print "
    =======usage:replace oldstring with newstring =======
    use: $0 oldstring newstring
    default to replace all files in current path.
  ";
    print "\n";
}
