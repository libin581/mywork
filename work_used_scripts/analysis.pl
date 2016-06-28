#! /usr/bin/perl

$file=shift @ARGV;

open(SRCFILE,"<","$file") || die"cannot open file $file: $!\n";
while(my $line=<SRCFILE>){
	if ($line=~m#\$.*</#){
		chomp($line);
	    my $where=index($line, "\$");
	    my $pathname = substr($line, $where-1);
	    $pathname =~s/<\/.*>//;
	    print "$pathname \n";

	    #$line=~s/^\s*//;
	    #print "$line \n"
	}

#$DATA01/rating/rat_gsm_roamout</normal_xdr_path>

}
close SRCFILE;
