#! /usr/bin/perl

@lines=`grep ".*convert.*//.*convert.*" *.dcd | cut -d "=" -f 2 | sort`;

my $i=0;
while($i<$#lines){
    chomp($lines[$i]);
    $lines[$i]=~s/\s*\/\// \/\//;
    $i++;
}


open(FILE,">","convertFunc") || die "cannot open file:$!\n";
$i=0;
my %old_new={};
while($i<$#lines){
    my $line=$lines[$i];
    $i = $i + 1;
    chomp($line);
    my $where=index($line, "//");
    $where = $where + 2;
    $oldstr = substr($line, $where);
    next if (exists $old_new{$oldstr});
    $old_new{$oldstr}=$line;
    print FILE "\"$oldstr\" => \"$line\",\n";
}

close FILE;

