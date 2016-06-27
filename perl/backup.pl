#! /usr/bin/perl

$bakPath = "/home/ut/share/";
$bakfile = "back.tar";
$bakfile = "$bakPath" . "$bakfile";



if (@ARGV < 1){
    &help();
    &showTarfile($bakfile);
    exit 0;
}

$file = shift @ARGV;
#$file =~ s/\s*\///;
$file =~ s/\s*//;
if ($file eq "-h" or $file eq "--help"){
    &help();
    exit 0;
}
elsif ($file eq "-r"){
    $file = shift @ARGV;
    defined $file or die "filename is empty!!!\n";
    if (&isFileInTarFile($file) == -1){
        print "$file is not in $bakfile!!!\n";
    }
    else{
        system("tar --delete $file -f $bakfile");
        print "delete $file from the tar file\n";
    }
    &showTarfile($bakfile);
}
elsif ($file eq "-d"){
    &default();
    &showTarfile($bakfile);
}
elsif ($file eq "-x"){
    $file= shift @ARGV;
    defined $file or die "filename is empty!!!\n";
    if (&isFileInTarFile($file) == -1){
        print "$file is not in $bakfile!!!\n";
    }
    else{
        system("tar -xf $bakfile $file");
        print "get $file from the tar file\n";
        system("ls -l $file");
    }
}
elsif ( defined $file ) {
    #$fileExist = `test -e $file && echo "EXIST" || echo "NOT EXIST" `;
    #unless ( $fileExist =~ m#NOT# ) {
    if ( -e $file){
        @filepath=split /\//, $file;
        $file=pop @filepath;
        $file=pop @filepath unless defined $file;

        while(my $path=shift @filepath)
        {
            chdir "$path";
        }

        #$curpath=$ENV{'PWD'};
		#print "---$curpath---\n";

        if (-d $file){
            system("tar -zcf $file.tar.gz $file");
            if (&isFileInTarFile($file) == 0){
               system("tar --delete $file.tar.gz -f $bakfile");
            }
            system("tar -rPf $bakfile $file.tar.gz");
            system("rm $file.tar.gz");
        }
        else {
            if (&isFileInTarFile($file) == -1){
                system("tar -rPf $bakfile $file");
            }
            else{
                system("tar -uPf $bakfile $file");
            }
        }
        &showTarfile($bakfile);
    }
    else {
        print "$file is not exist!!!\n";
        exit 0;
    }
}

sub help{
    print "
    backup.pl: help
    backup.pl -h: help
    backup.pl --help: help
    backup.pl -d: backup default files
    backup.pl file: backup a file or folder
    backup.pl -r file: delete file from back.tar
  ";
    print "\n";
}


sub default{
     #$curpath=$ENV{'PWD'};
     chdir $ENV{'HOME'} or die "can't change dir to $ENV{'HOME'}";
     system("tar -uPf $bakfile .profile");
     system("tar -uPf $bakfile share.sh");
     system("tar -uPf $bakfile .bashrc");
     system("tar -uPf $bakfile .vimrc");
     #chdir $curpath or die "can't change dir to $curpath";
     print ".profile share.sh .bashrc .vimrc is updated to back file\n";
};

sub showTarfile{
    print "-----------file list of tar file--------------\n";
    $tarfile=shift @_;
    #if (&isFileExit($tarfile) == 0){
    if ( -e $tarfile ){
        system("tar -tPf $tarfile");
        print "\n";
    }
    else{
        exit 0;
    }
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


sub isFileInTarFile{
    $file=shift @_;
    $baklist = `tar -tPf "$bakfile" `;
    if ( $baklist =~ m#$file# ){
        return 0;
    }
    else{
        return -1;
    }
}
