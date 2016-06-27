#! /usr/bin/perl

my $file=shift @ARGV;
if (&isFileExit($file) == -1){
	exit 0;
}

if (&isFolder($file) == 0){
    &fileTypeList("$file");
}
else{
    system("file $file");
}

sub isFileExit{
    $file=shift @_;
    $fileExist = `test -e $file && echo "EXIST" || echo "NOT EXIST" `;
    if ( $fileExist =~ m#NOT# ) {
        print "$file is not exist!!!\n";
        return -1;
    }
    else{   
        return 0;
    }
}

sub isFolder{
    $file=shift @_;
    $isFolder = `test -d $file && echo "TRUE" || echo "FALSE"`;
	if ( $isFolder =~ m#TRUE# ) {
	    return 0;
	}
	else{
		return -1;
	}
}


sub fileTypeList{
	my $dir=shift @_;
	chdir "$dir" and print "cd folder: $dir\n" or die "cannot chdir to $dir:$!";
	foreach (glob '*'){
		if (-d $_){
            &fileTypeList("$_");
		}
		elsif(-f $_){
            my $fileName=$_;
            # my $firstLine;
            #open(FILE,"<","$fileName") or die"cannot open the file: $!!!\n";
            # while (<FILE>){
            #     $firstLine=$_;last;
            # }
            # close FILE;
            # chomp($firstLine);
                    
            my $fileType=`file $fileName`;
            if ($fileType=~m#.*shell.*#){
                print "$fileName: shell script\n";
            }
            elsif ($fileType=~m#.*perl.*#){
                print "$fileName: perl script\n";
            }
            elsif ($fileType=~m#.*python.*#){
                print "$fileName: python script\n";
            }
            else{
                print "$fileName: $fileType\n";
            }
        }
		else{
	      	print "file $_ is not folder or file\n";
        }
	}
    chdir "..";
    return;
}

