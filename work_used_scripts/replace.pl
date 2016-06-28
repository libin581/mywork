#! /usr/bin/perl
$srcfile=shift @ARGV;
$dstfile=shift @ARGV;

 #get the encode type
 my $ENCODE_TYPE = &get_ENCODE_TYPE($srcfile);

 #replace strings
 open(SRCFILE,"<",$srcfile) || die "cannot open file $srcfile: $!\n";
 open(DSTFILE,">",$dstfile) || die "cannot open file $dstfile: $!\n";
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
        "ASASNONENE"  => "BER   //ASASNONENE",

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
	"convert_gsm_split_lmerge_by_sequenceno"           => "convert_gsm_split_merge_by_sequenceno //convert_gsm_split_lmerge_by_sequenceno" ,
	"convert_gprs_partial_type_ericsson_new"           => "convert_gprs_partial_type_ericsson //convert_gprs_partial_type_ericsson_new" ,


    ###########get from gsm prefix
    "neimeng_convert_format_opp_number"                => "convert_format_opp_number // neimeng_convert_format_opp_number" ,
    "zj_convert_set_mscid_according_filename"          => "zj_convert_set_mscid_according_filename_validTime  // zj_convert_set_mscid_according_filename",
    "gansu_convert_gsm_sequenceno_ericsson"            => "convert_gsm_sequenceno_ericsson",
	"convert_gsm_sequenceno_ericsson"                  => "guangxi_convert_gsm_sequenceno_ericsson // convert_gsm_sequenceno_ericsson",
    "convert_g_gprs_tariff_list"                       => "convert_ig_gprs_tariff_list  //  convert_g_gprs_tariff_list",
    "convert_split_wlan_by_oper_id"                    => "convert_split_wlan_by_oper_id_24  //convert_split_wlan_by_oper_id",
    "convert_wlan_PARTIAL_TYPE_INDICATOR"              => "convert_wlan_partial_type_indicator  //convert_wlan_PARTIAL_TYPE_INDICATOR",

    ###others
    "convert_supplement_imsi_15"                       => "zj_convert_supplement_imsi_15 //convert_supplement_imsi_15",
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

#    if (($line=~m#^\s*RECORD_CONVERT_FUNC#) && ($replaceFunc eq FALSE)){
#        my $where=index($line, "=");
#        $where = $where + 1;
#        my $noReplacefunc=substr($line, $where);
#        $noReplacefun=~s/[\n\r]//g;
#        $noReplacefun=~s/^\s+//;
#        $noReplacefun=~s/\s+$//;
#        print "$noReplacefunc";
#    }

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



