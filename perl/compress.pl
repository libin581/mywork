#! /usr/bin/perl

#-j: 透过 bzip2 支持压缩/解压缩：此时档名最好为 *.tar.bz2 
#-z: 透过 gzip  支持压缩/解压缩：此时档名最好为 *.tar.gz

if (@ARGV < 1){
    &usage();
    exit 0;
}

$file = shift @ARGV;
#$file =~ s/\s*\///;
$file =~ s/\s*//;
if ($file eq "-h" or $file eq "--help"){
    &usage();
    exit 0;
}
elsif ($file eq "-c"){
    $file=pop @ARGV;
    @filepath=split /\//, $file;
    $filename=pop @filepath;
    $filename=pop @filepath unless defined $filename;

    while(my $path=shift @filepath)
    {
        chdir "$path";
    }

    #printf("$filename\n");
    $compr_format=shift @ARGV;
    #print "$compr_format\n";
    if ($compr_format eq "bz2")
    {
        system("tar -jc -f $filename.tar.bz2 $filename");
        system("ls -l $filename.tar.bz2");
    }
    elsif ($compr_format eq "gz")
    {
        system("tar -zc -f $filename.tar.gz $filename");
        system("ls -l $filename.tar.gz");
    }
    elsif ($compr_format eq "tar")
    {
        system("tar -rP -f $filename.tar $filename");
        system("ls -l $filename.tar");
    }
    else
    {
        system("tar -zc -f $filename.tar.gz $filename");
        system("ls -l $filename.tar.gz");
    }
}
elsif ($file eq "-t"){
    $filename=shift @ARGV;
    $filename =~ s/\s*//;
    
    unless(-e $filename){
        print "$filename is not exit!!!\n"
    }
    
    print "-----------file list of tar file--------------\n";
    
    if ($filename =~ m/.*tar\.bz2/)
    {
        system("tar -jtv -f $filename");
    }
    elsif($filename =~ m/.*tar\.gz/)
    {
        system("tar -ztv -f $filename");
    } 
    elsif($filename =~ m/.*tar$/)
    {
        system("tar -tP -f $filename");
    } 
    else
    {
        printf("other compress format, not .gz or .bz2");
    }
}
elsif ($file eq "-x"){
    $filename=shift @ARGV;

    if ($filename =~ m/.*tar\.bz2/)
    {
        system("tar -jxv -f $filename");
    }
    elsif($filename =~ m/.*tar\.gz/)
    {
        system("tar -zxv -f $filename");
    }
    elsif($filename =~ m/.*tar$/)
    {
        system("tar -xv -f $filename");
    }
    else
    {
        printf("other compress format, not .gz or .bz2");
    }
}
else{
    printf("not recognize parameter: $file");
    &usage();
}

sub usage(){
    print "
    compress.pl: help
    compress.pl -h: help
    compress.pl --help: help
    compress.pl -t filename: show files in compress packet
    compress.pl -c filename: compress files to compress packet
    compress.pl -x filename: decompress files from compress packet
    ";
    print "\n";
}

