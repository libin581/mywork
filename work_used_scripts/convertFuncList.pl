#! /usr/bin/perl

@olddcdlist = &getolddcdlist();

@newdcdlist = &getnewdcdlist();

foreach $olddcd(@olddcdlist){
     my $isfound=FALSE;
     foreach $newdcd(@newdcdlist){
        if ($newdcd=~m#.*$olddcd.*#){
            print "$olddcd is in new list\n";
            $isfound=TRUE;
            last;
        }
     }
    
     if ($isfound eq FALSE){
         print "$olddcd is not in new list\n";
     }
}

sub getolddcdlist(){
my @olddcdlist=qw(
ericsson_gsm.dcd
siemens_gsm_v9.dcd
ericsson_gsm.dcd
huawei_gsm_252.dcd
siemens_gsm_v9.dcd
ericsson_gsm.dcd
huawei_gsm_252.dcd
huawei_gsm_252_gw.dcd
d_gsm.dcd
q_gsm.dcd
i_gsm.dcd
k_gsm.dcd
r_gsm.dcd
rd_gsm.dcd
idcm_gsm.dcd
id_gsm.dcd
multi_voice.dcd
inboss_sd_gsm.dcd
inboss_uploader_d_gsm.dcd
inboss_siemens_gsm_v9.dcd
ic_gsm.dcd
huawei_cs.dcd
ericsson_gsm_ng_block.dcd
inboss_d_gsm.dcd
ims_as.dcd
gsm_400.dcd
ericsson_gsm.dcd
inboss_q_gsm.dcd
inboss_huawei_gsm_252.dcd
inboss_ericsson_gsm.dcd
ericsson_gsm_ng.dcd
ed_gsm.dcd
dm_gsm.dcd
eq_gsm.dcd
pd_pp_gsm.dcd     
po_pp_gsm.dcd
pi_pp_gsm.dcd
pps_pp_gsm.dcd
sd_gsm.dcd
iuser_ipr.dcd
iuser_rnt.dcd
iuser_rec.dcd
ip_card.dcd
ippay_pip.dcd
ippay_gip.dcd
ippay_bip.dcd
vcard_vc_pps.dcd
vc_sett.dcd
vcard_scp.dcd
iuser_gif.dcd
);

return @olddcdlist;
}


sub getnewdcdlist(){
my @newdcdlist=qw(
ip_card.dcd 
ericsson_gsm.dcd
huawei_cs.dcd
huawei_gsm_252.dcd
huawei_gsm_252_gw.dcd
vpmn_vpn_cdr.dcd
vpmn_gsm.dcd
ed_gsm.dcd
eq_gsm.dcd
d_gsm.dcd
gsm_400.dcd
i_gsm.dcd
q_gsm.dcd
mvp.dcd
ims_as.dcd
uploader_d_gsm.dcd
r_gsm.dcd
sd_gsm.dcd
d_vpmn_scp.dcd
rd_gsm.dcd
hu_roam.dcd
hd_roam.dcd
vcard_vc_pps.dcd
vcard_scp.dcd
vc_sett.dcd  
huawei_sms.dcd
sms_inter.dcd
ismg_smg.dcd
ismg_smg_telecom.dcd
sms_iot.dcd
sms_vpmn.dcd
sms_zte.dcd
ismg_cm_down.dcd
voice_magazine.dcd
ussd.dcd
ussd_local_base.dcd
ussd_local_busi.dcd
ismg_ismg.dcd
sms_regard_inter.dcd
pim_down.dcd
cring.dcd
magic_voice.dcd
ismg_ym_down.dcd
ismg_yx_down.dcd
mobile_map.dcd
video_cring_down.dcd
ismg_caiyun.dcd
ismg_pm_down.dcd
ismg_m_down.dcd
ismg_ci_down.dcd
ismg_hywg.dcd
ismg_qyyx.dcd
bboss_mrdread.dcd
sms_bboss.dcd
pgm_smsmms.dcd
mth_iot.dcd
wireless_card.dcd
wireless_card_cring.dcd
magic_voice_ch.dcd
ismg_12580_down.dcd
wap.dcd
mobile_cartoon.dcd
mrd.dcd
mrddb.dcd
mobile_flash.dcd
pda.dcd
wap_local.dcd
widget.dcd
ippay_pip.dcd
ippay_gip.dcd
ippay_bip.dcd
mms.dcd
mms_inter.dcd
mms_union.dcd
mms_ori.dcd
mms_ci_down.dcd
mms_bboss.dcd
mms_hywg.dcd
wlan.dcd
wlan_iwlan.dcd
wlan_wt.dcd
wlan_wli.dcd
wlan_kjh.dcd
gp_down.dcd
mp.dcd
mobile_navigation_gd.dcd
mobile_market.dcd
dkxf_down.dcd
poc.dcd
multi_voice.dcd
addvalue_meeting.dcd
cas.dcd
ctd.dcd
efp.dcd
stream_down.dcd
ip_ggprs.dcd
ip_ggprs_w.dcd
ericsson_LTE_ps.dcd
huawei_ps.dcd
huawei_LTE_ps.dcd
gprs_cngd_down.dcd
gprs_cngd_down_lte.dcd
gprs_tap3.dcd
gprs_tap3_lte.dcd
ggprs_iot_cngo.dcd
ggprs_iot_cngd.dcd
gmrd.dcd
gprs_g3nb.dcd
idc_ips.dcd
ericsson_ps.dcd
ericsson_ps.dcd
huawei_ps.dcd
huawei_ps.dcd
huawei_LTE_ps.dcd
ericsson_LTE_ps.dcd
gg_gprs.dcd
g_gprs.dcd
ggprs_group_bill.dcd
ggprs_group_bill_local.dcd


);

return @newdcdlist;
}


