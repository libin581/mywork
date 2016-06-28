#! /usr/bin/perl
$province="xizang";
$ngfolder=$province."_ng";
$workpath="/home/libin3/CMCC_ZJ/billing/billing40/app30/filter/template/";
chdir $workpath;
mkdir $ngfolder;
$workpath=$workpath."$province";
chdir $province;

@dcdlist=&getdcdlist();

foreach $dcdfile(@dcdlist){
       my $fileName=$dcdfile;
       #unless (-f $fileName){
       #    print "$fileName is not exist!!!\n";
       #    next;
       #}

      my $isfound = FALSE;
      foreach ( glob "*"){
          #if ($fileName=~m#.*$_.*#){
          if ($fileName eq $_){
              print "\n$fileName: no match funcs \n";
             $isfound=TRUE;
             last;
          }
      }

      if ($isfound eq FALSE){
             print "$fileName is not found  \n";
             next;
      }

       #get the encode type
       my $ENCODE_TYPE = &get_ENCODE_TYPE("$fileName");

       #replace strings
       open(SRCFILE,"<","$fileName") || die "cannot open file $fileName: $!\n";
       open(DSTFILE,">","../$ngfolder/$fileName") || die "cannot open file $fileName: $!\n";
       while(my $eachline=<SRCFILE>){
           $eachline = replaceString($eachline);
           print DSTFILE "$eachline";
           
           #add PROPERTY_FILE_ENCODE_TYPE in the PROPERTY
           if (defined($ENCODE_TYPE)){
               if ($eachline=~m#.*PROPERTY_FILTER_CHECK.*#){
                   $eachline=~s/PROPERTY_FILTER_CHECK/PROPERTY_FILE_ENCODE_TYPE/;
                   $eachline=~s/YES/$ENCODE_TYPE/;
                   $eachline=~s/NO/$ENCODE_TYPE/;
                   print DSTFILE "$eachline";
                   #print DSTFILE "PROPERTY_FILE_ENCODE_TYPE = $ENCODE_TYPE\n";
               }
           }
       }
       close SRCFILE;
       close DSTFILE;
}

sub replaceString(){
    my $line=shift @_;
    unless ($line=~m#\s+RECORD_.*#){
         return $line;
    }
    
    #if (($line=~m#.*RECORD_XDR_OUTPUT.*#) || ($line=~m#.*RECORD_NAME.*#) || ($line=~m#.*RECORD_NEXT.*#)){
    #     return $line;
    #}

    #if ($line=~m#.*RECORD_TYPE.*#){
    #if (($line=~m#.*CONTROL.*#) || ($line=~m#.*HEAD.*#) || ($line=~m#.*TAIL.*#) ){
    #     return $line;
    #}
    #}

    %old_new=(
        "BILL_RECORD" => "BILL //BILL_RECORD",
        "HEAD_RECORD" => "HEAD //HEAD_RECORD",
        "TAIL_RECORD" => "TAIL //TAIL_RECORD",
        "CONTROL_RECORD" => "CONTROL //CONTROL_RECORD",

        "RECORD_ENCODE_TYPE" => "//RECORD_ENCODE_TYPE",
        "RECORD_FIELD_STABLE" => "//RECORD_FIELD_STABLE",
        "RECORD_FIELD_NOORDER" => "//RECORD_FIELD_NOORDER",

        ########## get from note of guangxi ng
	"zj_convert_format_user_number"                    => "convert_format_user_number //zj_convert_format_user_number" ,
	"zj_convert_switch_wlan_roam_filename"             => "sh_convert_switch_wlan_roam_filename //zj_convert_switch_wlan_roam_filename" ,
	"psd_convert_conbineDateTime"                      => "convert_conbineDateTime //psd_convert_conbineDateTime" ,
	"zj_convert_filter_wireless_service"               => "convert_filter_wireless_service //zj_convert_filter_wireless_service" ,
	"zj_convert_format_opp_number"                     => "convert_format_opp_number //zj_convert_format_opp_number" ,
	"zj_convert_format_opp_user_number"                => "convert_format_opp_number //zj_convert_format_opp_user_number" ,
	"zj_convert_gsm_cfcalltype_adjust"                 => "convert_gsm_cfcalltype_adjust //zj_convert_gsm_cfcalltype_adjust" ,
	"public_convert_judge_0_duration"                  => "convert_gsm_duration //public_convert_judge_0_duration" ,
	"zj_convert_gsm_format_anumbe"                     => "convert_gsm_format_anumber //zj_convert_gsm_format_anumbe" ,
	"zj_convert_gsm_format_anumber"                    => "convert_gsm_format_anumber //zj_convert_gsm_format_anumber" ,
	"zj_convert_gsm_format_anumber"                    => "convert_gsm_format_anumber //zj_convert_gsm_format_anumber" ,
	"zj_convert_huawei_call_type"                      => "convert_huawei_call_type //zj_convert_huawei_call_type" ,
	"zj_convert_gsm_cfcalltype_according_servicecode"  => "convert_huawei_msoftx_gsm_cfcalltype_by_servicecode //zj_convert_gsm_cfcalltype_according_servicecode" ,
	"zj_convert_huawei_user_number_exchange"           => "convert_huawei_user_number_exchange //zj_convert_huawei_user_number_exchange" ,
	"zj_convert_judge_shortest_duartion"               => "convert_judge_0_duration //zj_convert_judge_shortest_duartion" ,
	"zj_convert_judge_imsi_empty"                      => "convert_judge_imsi_empty //zj_convert_judge_imsi_empty" ,
	"zj_convert_judge_longest_duration"                => "convert_judge_longest_duration //zj_convert_judge_longest_duration" ,
	"public_convert_set_ori_basic_charge_1008X"        => "convert_set_ori_basic_charge_1008X //public_convert_set_ori_basic_charge_1008X" ,
	"public_convert_gsm_inboss_cdr_60_old"             => "public_convert_gsm_inboss_cdr_60 //public_convert_gsm_inboss_cdr_60_old" ,
	"zj_convert_filter_gsm_someservice_from_msc"       => "convert_filter_gsm_someservice_from_msc //zj_convert_filter_gsm_someservice_from_msc" ,
	"hlr_convert_split_record_local_by_user_number"    => "convert_split_record_local_by_user_number_gx //hlr_convert_split_record_local_by_user_number" ,
	"convert_gsm_split_lmerge_by_sequenceno"           => "guangxi_convert_gsm_split_merge_by_sequenceno //convert_gsm_split_lmerge_by_sequenceno" ,
	"convert_gprs_partial_type_ericsson_new"           => "convert_gprs_partial_type_ericsson //convert_gprs_partial_type_ericsson_new" ,
  "neimeng_gsm_convert_format_opp_number"            => "convert_format_opp_number// neimeng_gsm_convert_format_opp_number" ,
    );

    my $replaceFunc=FALSE;
    while ((my $strOrig, my $strReplace)=each %old_new){
        #print "$strOrig => $strReplace \n";
        next if ($line=~m#.*$strReplace.*#);
        my $strOrig_ = "$strOrig"."_";
        if ($line=~m#.*RECORD_CONVERT_FUNC.*$strOrig.*#){
             unless ($line=~m#.*RECORD_CONVERT_FUNC.*$strOrig_.*#){
                     $replaceFunc =TRUE;
                     $line=~s/$strOrig/$strReplace/;
                     last;
             }
        }elsif($line=~m#.*$strOrig.*#){
                 $line=~s/$strOrig/$strReplace/;
                 last;
        }
    } 

    if (($line=~m#^\s*RECORD_CONVERT_FUNC#) && ($replaceFunc eq FALSE)){
        my $where=index($line, "=");
        $where = $where + 1;
        my $noReplacefunc=substr($line, $where);
        $noReplacefun=~s/[\n\r]//g;
        $noReplacefun=~s/^\s+//;
        $noReplacefun=~s/\s+$//;
        print "$noReplacefunc";
    }

    return $line;
}

sub get_ENCODE_TYPE(){
    my $file=shift @_;

    open(FILE,"<","$file") || die"cannot open file $file: $!\n";
    my $ENCODE_TYPE = undef;
    while (my $line=<FILE>){
         return $ENCODE_TYPE if ($line=~m#.*OPERTY_FILE_ENCODE_TYPE.*#);
         if ($line=~m#.*RECORD_ENCODE_TYPE.*#){
             if ($line=~m#.*ASCII.*#){
                 $ENCODE_TYPE = ASCII;
             }elsif($line=~m#.*ASNONE.*#){
                 $ENCODE_TYPE = ASNONE;
             }elsif($line=~m#.*BCD.*#){
                 $ENCODE_TYPE = BCD;
             }
             last;
         }
    }
    close FILE;

    return $ENCODE_TYPE;
}

sub skip_blank_nots_line(){
    my $line = shift @_;
    my $SKIP = FALSE;
}

sub getdcdlist(){
    my @dcdlist=qw( 
d_gsm.dcd
q_gsm.dcd
i_gsm.dcd
k_gsm.dcd
r_gsm.dcd
idcm_gsm.dcd
id_gsm.dcd
inboss_uploader_d_gsm.dcd
inboss_siemens_gsm_v11.dcd
ic_gsm.dcd
huawei_cs.dcd
gsm_400.dcd
ed_gsm.dcd
dm_gsm.dcd
eq_gsm.dcd
inboss_alcatel_gsm_spatial.dcd
vsat_center.dcd
siemens_gsm_v8_gw.dcd
siemens_gsm_v8.dcd
siemens_gsm_v11.dcd
ims_hw_mmtel.dcd
ims_hw_as.dcd
gsm_meeting.dcd
alcatel_gsm_v8.dcd
alcatel_gsm_spatial.dcd
uploader_d_gsm.dcd
inboss_siemens_gsm_v8.dcd
huawei_msoftx3000_gsm.dcd
inboss_alcatel_gsm_v8.dcd
pd_pp_gsm.dcd     
po_pp_gsm.dcd
pps_pp_gsm.dcd
pa_pp_gsm.dcd
ip_card.dcd
vc_sett.dcd
vcard_scp.dcd
scp_pp_17951IP.dcd
v_agent.dcd
);
#    foreach (glob "*"){
#          if ($_=~m#.*gsm.*#){
#              push(@dcdlist,$_);
#          }
#      }

return @dcdlist;
}


