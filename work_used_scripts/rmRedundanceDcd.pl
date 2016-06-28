#! /usr/bin/perl


@deldcdlist=&getdeldcdlist();


while (my $deldcd = shift @deldcdlist) {
    chomp($deldcd);
    my $isfound = FALSE;
    foreach (glob '*'){
        my $filename=$_;
        if ($deldcd=~m#.*$filename.*#){
            system("rm $filename");
            print "$filename removed \n";
            $isfound = TRUE;
            last;
        }
    }
    
    if ($isfound eq FALSE){
        print "$deldcd is not found \n";
    }

}


sub getdeldcdlist(){
return  @deldcdlist = qw(
siemens_gsm_v9.dcd
k_gsm.dcd
idcm_gsm.dcd
id_gsm.dcd
inboss_sd_gsm.dcd
inboss_uploader_d_gsm.dcd
inboss_siemens_gsm_v9.dcd
ic_gsm.dcd
ericsson_gsm_ng_block.dcd
inboss_d_gsm.dcd
inboss_q_gsm.dcd
inboss_huawei_gsm_252.dcd
inboss_ericsson_gsm.dcd
ericsson_gsm_ng.dcd
dm_gsm.dcd
pd_pp_gsm.dcd
po_pp_gsm.dcd
pi_pp_gsm.dcd
pps_pp_gsm.dcd
iuser_ipr.dcd
iuser_rnt.dcd
iuser_rec.dcd
iuser_gif.dcd
);

}
