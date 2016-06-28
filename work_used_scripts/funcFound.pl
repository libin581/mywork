#! /usr/bin/perl

@dcdlist=&getdcdlist();

while (my $dcd = shift @dcdlist) {
    chomp($dcd);
    my $isfound = FALSE;
    foreach (glob '*'){
        my $filename=$_;
        if ($dcd=~m#.*$filename.*#){
            print "$filename is found \n";
            $isfound = TRUE;
            last;
        }
    }
  
    if ($isfound eq FALSE){
    print "$dcd is not found \n";
    }
}



sub getdcdlist(){
return my @dcdlist=qw(
ericsson_gsm.dcd
huawei_gsm_252.dcd
ericsson_gsm.dcd
huawei_gsm_252.dcd
huawei_gsm_252_gw.dcd
d_gsm.dcd
q_gsm.dcd
i_gsm.dcd
r_gsm.dcd
rd_gsm.dcd
multi_voice.dcd
huawei_cs.dcd
ims_as.dcd
gsm_400.dcd
ericsson_gsm.dcd
ed_gsm.dcd
eq_gsm.dcd
sd_gsm.dcd
ip_card.dcd
ippay_pip.dcd
ippay_gip.dcd
ippay_bip.dcd
vcard_vc_pps.dcd
vc_sett.dcd
vcard_scp.dcd


);

}


