#! /usr/bin/perl

my $file=shift @ARGV;
if (-d $file){
        &chgForFolder("$file");
}
elsif(-f $file){
        system("dos2unix $file");
}else{
        printf "not valid file input!!!\n";
}

sub chgForFolder{
	my $dir=shift @_;
	print "cd folder: $dir\n";
	chdir "$dir" or die "cannot chdir to $dir:$!";
	foreach (glob '*'){
		if (-d $_){
                      &chgForFolder("$_");
		}
		elsif(-f $_){
                     if ((m#.*\.c.*#) || (m#.*\.h.*#) || (m#.*\.p.*#) || (m#.*\.sh.*#))
		     {
                       system("dos2unix $_");
		     }
                     else
		     {
			print "file $_ is not changed\n";
		     }
         	}
		else{
	        	print "file $_ is not folder or file\n";
                }
	}
        chdir "..";
        return;
}



