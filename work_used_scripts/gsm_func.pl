#! /usr/bin/perl

%old_new=(
convert_bxf_dfile                                  =>  gsm_convert_bxf_dfile                                 ,   
convert_cell_lac                                   =>  gsm_convert_cell_lac                                  ,
convert_change_ericssion_oppnumber                 =>  gsm_convert_change_ericssion_oppnumber                ,
convert_conbineDateTime                            =>  gsm_convert_conbineDateTime                           ,
convert_ericsson_cfcalltype                        =>  gsm_convert_ericsson_cfcalltype                       ,
convert_ericsson_vpmn_judge                        =>  gsm_convert_ericsson_vpmn_judge                       ,
convert_ericsson_vpmn_judge_new                    =>  gsm_convert_ericsson_vpmn_judge_new                   ,
convert_filter_drtype_pdppgsm                      =>  gsm_convert_filter_drtype_pdppgsm                     ,
convert_filter_national_sms                        =>  gsm_convert_filter_national_sms                       ,
convert_filter_roam_jtw                            =>  gsm_convert_filter_roam_jtw                           ,
convert_format_opp_number                          =>  gsm_convert_format_opp_number                         ,
convert_gsm_bill_indicate                          =>  gsm_convert_gsm_bill_indicate                         ,
convert_gsm_ericsson_otherparty                    =>  gsm_convert_gsm_ericsson_otherparty                   ,
convert_gsm_opp_number                             =>  gsm_convert_gsm_opp_number                            ,
convert_gsm_sequenceno_ericsson                    =>  gsm_convert_gsm_sequenceno_ericsson                   ,
convert_gsm_sequenceno_huawei                      =>  gsm_convert_gsm_sequenceno_huawei                     ,
convert_gsm_siemens_otherparty                     =>  gsm_convert_gsm_siemens_otherparty                    ,
convert_gsm_split_merge_by_sequenceno              =>  gsm_convert_gsm_split_merge_by_sequenceno             ,
convert_huawei_gsm_start_time                      =>  gsm_convert_huawei_gsm_start_time                     ,
convert_huawei_user_number_exchange                =>  gsm_convert_huawei_user_number_exchange               ,
convert_i_gsm_call_type                            =>  gsm_convert_i_gsm_call_type                           ,
convert_set_moc_id_null_when_vhe                   =>  gsm_convert_set_moc_id_null_when_vhe                  ,
convert_set_moc_id_null_when_vhe_ericsson          =>  gsm_convert_set_moc_id_null_when_vhe_ericsson         ,
convert_siemens_cell_lac                           =>  gsm_convert_siemens_cell_lac                          ,
convert_siemens_gsm_SupplementaryService           =>  gsm_convert_siemens_gsm_SupplementaryService          ,
convert_siemens_gsm_vpmn                           =>  gsm_convert_siemens_gsm_vpmn                          ,
convert_siemens_service_code                       =>  gsm_convert_siemens_service_code                      ,
convert_siemens_set_otherparty                     =>  gsm_convert_siemens_set_otherparty                    ,
convert_vhe_by_vpmn_judge                          =>  gsm_convert_vhe_by_vpmn_judge                         ,
convert_vhe_by_vpmn_judge_ericsson                 =>  gsm_convert_vhe_by_vpmn_judge_ericsson                ,
neimeng_convert_filter_gsm_someservice_from_msc    =>  gsm_neimeng_convert_filter_gsm_someservice_from_msc   ,
neimeng_convert_format_longtime_record             =>  gsm_neimeng_convert_format_longtime_record            ,
neimeng_convert_format_opp_number                  =>  gsm_neimeng_convert_format_opp_number                 ,
neimeng_convert_gsm_duration                       =>  gsm_neimeng_convert_gsm_duration                      ,
neimeng_convert_gsm_vpmn_cdr                       =>  gsm_neimeng_convert_gsm_vpmn_cdr                      ,
neimeng_convert_huawei_trunk_id                    =>  gsm_neimeng_convert_huawei_trunk_id                   ,
public_convert_Qcharge_by_servicetype              =>  gsm_public_convert_Qcharge_by_servicetype             ,
public_convert_check_pbx                           =>  gsm_public_convert_check_pbx                          ,
public_convert_cut_off_0_from_a_number_01008X      =>  gsm_public_convert_cut_off_0_from_a_number_01008X     ,
public_convert_cut_off_0_from_opp_number_01008X    =>  gsm_public_convert_cut_off_0_from_opp_number_01008X   ,        
public_convert_gsm_inboss_cdr_60                   =>  gsm_public_convert_gsm_inboss_cdr_60                  ,
public_convert_gsm_vpmn_60                         =>  gsm_public_convert_gsm_vpmn_60                        ,
public_convert_opp_number_159786_del               =>  gsm_public_convert_opp_number_159786_del              ,
public_convert_splite_pbx                          =>  gsm_public_convert_splite_pbx                         ,
zj_convert_bxf_dfile                               =>  gsm_zj_convert_bxf_dfile                              ,
zj_convert_huawei_filter_service                   =>  gsm_zj_convert_huawei_filter_service                  ,
zj_convert_ilr_add_basicfee                        =>  gsm_zj_convert_ilr_add_basicfee                       ,
zj_convert_intrunk_from_vpp_vpn                    =>  gsm_zj_convert_intrunk_from_vpp_vpn                   ,
zj_convert_judge_user_equal_opp                    =>  gsm_zj_convert_judge_user_equal_opp                   ,
zj_convert_pbx_from_vpmn                           =>  gsm_zj_convert_pbx_from_vpmn                          ,
zj_convert_set_mscid_according_filename            =>  gsm_zj_convert_set_mscid_according_filename           ,
zj_convert_siemens_call_type                       =>  gsm_zj_convert_siemens_call_type                      ,
zj_convert_siemens_filter_service                  =>  gsm_zj_convert_siemens_filter_service                 ,
zj_convert_siemens_smot_opp_number                 =>  gsm_zj_convert_siemens_smot_opp_number                ,
zj_convert_siemens_user_number                     =>  gsm_zj_convert_siemens_user_number                    ,
);

while((my $old, my $new)=each %old_new){
    @lines=`grep -r "$old" ng/*`;
    my $i=0;
    my $oldFind=FALSE;
    my $newfind=FALSE;
    while($i<$#lines){
        $oldFind=TRUE if ($lines[$i]=~m#.*$old.*#);
        $newFind=TRUE if ($lines[$i]=~m#.*$new.*#);
        $i = $i + 1; 
    }
    if ($oldFind eq TRUE && $newFind eq TRUE){
        $new="$new"." //$old";
        $new="\""."$new"."\"";
        $old="\""."$old"."\"";
        printf "%-50s => %-s ,\n", "$old", "$new";
    }
    else{
        print "$old is not the prefix gsm!!!\n";
    }
}


