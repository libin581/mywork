FIELD //TRADEMARK
{
    FIELD_NAME = BEGIN
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm1
    FIELD_XDRKEY = TRADEMARK
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //SERVICE_ID
{
    FIELD_NAME = gsm1
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm2
    FIELD_XDRKEY = SERVICE_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //DR_TYPE
{
    FIELD_NAME = gsm2
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm3
    FIELD_XDRKEY = DR_TYPE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //BILL_MONTH
{
    FIELD_NAME = gsm3
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm4
    FIELD_XDRKEY = BILL_MONTH
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //VALID_RATE_PROD_ID
{
    FIELD_NAME = gsm4
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm5
    FIELD_XDRKEY = VALID_RATE_PROD_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //RATE_PROD_ID
{
    FIELD_NAME = gsm5
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm6
    FIELD_XDRKEY = RATE_PROD_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //PRODUCT_ID
{
    FIELD_NAME = gsm6
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm7
    FIELD_XDRKEY = PRODUCT_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //PROMOTION_PRODS
{
    FIELD_NAME = gsm7
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm8
    FIELD_XDRKEY = PROMOTION_PRODS
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //PLAN_ID
{
    FIELD_NAME = gsm8
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm9
    FIELD_XDRKEY = PLAN_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //OPP_RATE_PROD_ID
{
    FIELD_NAME = gsm9
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm10
    FIELD_XDRKEY = OPP_RATE_PROD_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //CUST_ID
{
    FIELD_NAME = gsm10
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm11
    FIELD_XDRKEY = CUST_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ACC_ID
{
    FIELD_NAME = gsm11
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm12
    FIELD_XDRKEY = ACC_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //USER_ID
{
    FIELD_NAME = gsm12
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm13
    FIELD_XDRKEY = USER_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //IMSI
{
    FIELD_NAME = gsm13
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm14
    FIELD_XDRKEY = IMSI
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //USER_NUMBER
{
    FIELD_NAME = gsm14
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm15
    FIELD_XDRKEY = USER_NUMBER
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //BILL_INDICATE
{
    FIELD_NAME = gsm15
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm16
    FIELD_XDRKEY = BILL_INDICATE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //OPP_NUMBER
{
    FIELD_NAME = gsm16
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm17
    FIELD_XDRKEY = OPP_NUMBER
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //OPP_USER_NUMBER
{
    FIELD_NAME = gsm17
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm18
    FIELD_XDRKEY = OPP_USER_NUMBER
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //A_NUMBER
{
    FIELD_NAME = gsm18
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm19
    FIELD_XDRKEY = A_NUMBER
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //START_TIME
{
    FIELD_NAME = gsm19
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm20
    FIELD_XDRKEY = START_TIME
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //DURATION
{
    FIELD_NAME = gsm20
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm21
    FIELD_XDRKEY = DURATION
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //RATING_RES
{
    FIELD_NAME = gsm21
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm22
    FIELD_XDRKEY = RATING_RES
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //CALL_TYPE
{
    FIELD_NAME = gsm22
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm23
    FIELD_XDRKEY = CALL_TYPE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ROAM_TYPE
{
    FIELD_NAME = gsm23
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm24
    FIELD_XDRKEY = ROAM_TYPE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //OPP_ACCESS_TYPE
{
    FIELD_NAME = gsm24
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm25
    FIELD_XDRKEY = OPP_ACCESS_TYPE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //OPP_NUMBER_TYPE
{
    FIELD_NAME = gsm25
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm26
    FIELD_XDRKEY = OPP_NUMBER_TYPE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //sp_rela_TYPE
{
    FIELD_NAME = gsm26
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm27
    FIELD_XDRKEY = sp_rela_TYPE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //HPLMN1
{
    FIELD_NAME = gsm27
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm28
    FIELD_XDRKEY = HPLMN1
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //HPLMN2
{
    FIELD_NAME = gsm28
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm29
    FIELD_XDRKEY = HPLMN2
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //HPLMN3
{
    FIELD_NAME = gsm29
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm30
    FIELD_XDRKEY = HPLMN3
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //VPLMN1
{
    FIELD_NAME = gsm30
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm31
    FIELD_XDRKEY = VPLMN1
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //VPLMN2
{
    FIELD_NAME = gsm31
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm32
    FIELD_XDRKEY = VPLMN2
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ROAM_NET_TYPE
{
    FIELD_NAME = gsm32
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm33
    FIELD_XDRKEY = ROAM_NET_TYPE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //RATING_FLAG
{
    FIELD_NAME = gsm33
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm34
    FIELD_XDRKEY = RATING_FLAG
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ITem_code1
{
    FIELD_NAME = gsm34
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm35
    FIELD_XDRKEY = ITem_code1
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //CHARGE1
{
    FIELD_NAME = gsm35
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm36
    FIELD_XDRKEY = CHARGE1
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //CHARGE1_DISC
{
    FIELD_NAME = gsm36
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm37
    FIELD_XDRKEY = CHARGE1_DISC
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ITem_code2
{
    FIELD_NAME = gsm37
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm38
    FIELD_XDRKEY = ITem_code2
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //CHARGE2
{
    FIELD_NAME = gsm38
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm39
    FIELD_XDRKEY = CHARGE2
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //CHARGE2_DISC
{
    FIELD_NAME = gsm39
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm40
    FIELD_XDRKEY = CHARGE2_DISC
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ITem_code3
{
    FIELD_NAME = gsm40
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm41
    FIELD_XDRKEY = ITem_code3
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //CHARGE3
{
    FIELD_NAME = gsm41
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm42
    FIELD_XDRKEY = CHARGE3
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //CHARGE3_DISC
{
    FIELD_NAME = gsm42
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm43
    FIELD_XDRKEY = CHARGE3_DISC
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ITem_code4
{
    FIELD_NAME = gsm43
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm44
    FIELD_XDRKEY = ITem_code4
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //CHARGE4
{
    FIELD_NAME = gsm44
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm45
    FIELD_XDRKEY = CHARGE4
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //CHARGE4_DISC
{
    FIELD_NAME = gsm45
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm46
    FIELD_XDRKEY = CHARGE4_DISC
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //FREE_RES_VAL
{
    FIELD_NAME = gsm46
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm47
    FIELD_XDRKEY = FREE_RES_VAL
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ADDUP_RES_VAL
{
    FIELD_NAME = gsm47
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm48
    FIELD_XDRKEY = ADDUP_RES_VAL
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //STD_unit
{
    FIELD_NAME = gsm48
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm49
    FIELD_XDRKEY = STD_unit
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //TOLL_STD_unit
{
    FIELD_NAME = gsm49
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm50
    FIELD_XDRKEY = TOLL_STD_unit
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ori_basic_charge
{
    FIELD_NAME = gsm50
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm51
    FIELD_XDRKEY = ori_basic_charge
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ori_toll_charge
{
    FIELD_NAME = gsm51
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm52
    FIELD_XDRKEY = ori_toll_charge
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ORI_OTHER_CHARGE
{
    FIELD_NAME = gsm52
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm53
    FIELD_XDRKEY = ORI_OTHER_CHARGE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //STD_BASIC_CHARGE
{
    FIELD_NAME = gsm53
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm54
    FIELD_XDRKEY = STD_BASIC_CHARGE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //STD_TOLL_CHARGE
{
    FIELD_NAME = gsm54
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm55
    FIELD_XDRKEY = STD_TOLL_CHARGE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //STD_OTHER_CHARGE
{
    FIELD_NAME = gsm55
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm56
    FIELD_XDRKEY = STD_OTHER_CHARGE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ADDUP_RES
{
    FIELD_NAME = gsm56
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm57
    FIELD_XDRKEY = ADDUP_RES
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //OPP_CONDITION_ID
{
    FIELD_NAME = gsm57
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm58
    FIELD_XDRKEY = OPP_CONDITION_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //CONDITION_ID
{
    FIELD_NAME = gsm58
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm59
    FIELD_XDRKEY = CONDITION_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //NETCALL_FLAG
{
    FIELD_NAME = gsm59
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm60
    FIELD_XDRKEY = NETCALL_FLAG
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ESN
{
    FIELD_NAME = gsm60
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm61
    FIELD_XDRKEY = ESN
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //SEQUENCE_NO
{
    FIELD_NAME = gsm61
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm62
    FIELD_XDRKEY = SEQUENCE_NO
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //MODIFICATION_IND
{
    FIELD_NAME = gsm62
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm63
    FIELD_XDRKEY = MODIFICATION_IND
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //OPP_ROAM_AREACODE
{
    FIELD_NAME = gsm63
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm64
    FIELD_XDRKEY = OPP_ROAM_AREACODE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //OPP_HOME_AREACODE
{
    FIELD_NAME = gsm64
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm65
    FIELD_XDRKEY = OPP_HOME_AREACODE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //TOLL_TYPE
{
    FIELD_NAME = gsm65
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm66
    FIELD_XDRKEY = TOLL_TYPE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //TOLL_TYPE2
{
    FIELD_NAME = gsm66
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm67
    FIELD_XDRKEY = TOLL_TYPE2
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //MSRN
{
    FIELD_NAME = gsm67
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm68
    FIELD_XDRKEY = MSRN
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //MSC_ID
{
    FIELD_NAME = gsm68
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm69
    FIELD_XDRKEY = MSC_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //SCP_ID
{
    FIELD_NAME = gsm69
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm70
    FIELD_XDRKEY = SCP_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //LAC_ID
{
    FIELD_NAME = gsm70
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm71
    FIELD_XDRKEY = LAC_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //CELL_ID
{
    FIELD_NAME = gsm71
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm72
    FIELD_XDRKEY = CELL_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //SERVICE_TYPE
{
    FIELD_NAME = gsm72
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm73
    FIELD_XDRKEY = SERVICE_TYPE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //SERVICE_CODE
{
    FIELD_NAME = gsm73
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm74
    FIELD_XDRKEY = SERVICE_CODE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //SERVICE_KEY
{
    FIELD_NAME = gsm74
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm75
    FIELD_XDRKEY = SERVICE_KEY
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //STOP_CAUSE
{
    FIELD_NAME = gsm75
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm76
    FIELD_XDRKEY = STOP_CAUSE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //IN_TRUNKID
{
    FIELD_NAME = gsm76
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm77
    FIELD_XDRKEY = IN_TRUNKID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //OUT_TRUNKID
{
    FIELD_NAME = gsm77
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm78
    FIELD_XDRKEY = OUT_TRUNKID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //GROUP_ID
{
    FIELD_NAME = gsm78
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm79
    FIELD_XDRKEY = GROUP_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //MOC_ID
{
    FIELD_NAME = gsm79
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm80
    FIELD_XDRKEY = MOC_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //MTC_ID
{
    FIELD_NAME = gsm80
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm81
    FIELD_XDRKEY = MTC_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //PROCESS_TIME
{
    FIELD_NAME = gsm81
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm82
    FIELD_XDRKEY = PROCESS_TIME
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //BACKUP_DATE
{
    FIELD_NAME = gsm82
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm83
    FIELD_XDRKEY = BACKUP_DATE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ORIGINAL_FILE
{
    FIELD_NAME = gsm83
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm84
    FIELD_XDRKEY = ORIGINAL_FILE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //USER_TYPE
{
    FIELD_NAME = gsm84
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm85
    FIELD_XDRKEY = USER_TYPE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //VPLMN3
{
    FIELD_NAME = gsm85
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm86
    FIELD_XDRKEY = VPLMN3
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //OPP_PLAN_ID
{
    FIELD_NAME = gsm86
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm87
    FIELD_XDRKEY = OPP_PLAN_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //COLLECTION_ITEM
{
    FIELD_NAME = gsm87
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm88
    FIELD_XDRKEY = COLLECTION_ITEM
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //OPP_NOACCESS_NUMBER
{
    FIELD_NAME = gsm88
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm89
    FIELD_XDRKEY = OPP_NOACCESS_NUMBER
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //REDO_FLAG
{
    FIELD_NAME = gsm89
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm90
    FIELD_XDRKEY = REDO_FLAG
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //RESERVE1
{
    FIELD_NAME = gsm90
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm91
    FIELD_XDRKEY = RESERVE1
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //RESERVE2
{
    FIELD_NAME = gsm91
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm92
    FIELD_XDRKEY = RESERVE2
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //RESERVE3
{
    FIELD_NAME = gsm92
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm93
    FIELD_XDRKEY = RESERVE3
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //RESERVE4
{
    FIELD_NAME = gsm93
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm94
    FIELD_XDRKEY = RESERVE4
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //VIDEO_TYPE
{
    FIELD_NAME = gsm94
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm95
    FIELD_XDRKEY = VIDEO_TYPE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //MNS_TYPE
{
    FIELD_NAME = gsm95
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm96
    FIELD_XDRKEY = MNS_TYPE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //USER_PROPERTY
{
    FIELD_NAME = gsm96
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm97
    FIELD_XDRKEY = USER_PROPERTY
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //OPP_PROPERTY
{
    FIELD_NAME = gsm97
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm98
    FIELD_XDRKEY = OPP_PROPERTY
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //CALL_REFNUM
{
    FIELD_NAME = gsm98
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm99
    FIELD_XDRKEY = CALL_REFNUM
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //FCI_TYPE
{
    FIELD_NAME = gsm99
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm100
    FIELD_XDRKEY = FCI_TYPE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //MONITOR_CDR
{
    FIELD_NAME = gsm100
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm101
    FIELD_XDRKEY = MONITOR_CDR
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //STD_ERR_CODE
{
    FIELD_NAME = gsm101
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm102
    FIELD_XDRKEY = STD_ERR_CODE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //CREATE_DATE
{
    FIELD_NAME = gsm102
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm103
    FIELD_XDRKEY = CREATE_DATE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ALL_PROMOTION_PRODS
{
    FIELD_NAME = gsm103
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm104
    FIELD_XDRKEY = ALL_PROMOTION_PRODS
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //PARTIAL_ID
{
    FIELD_NAME = gsm104
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm105
    FIELD_XDRKEY = PARTIAL_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //FIRSTCDR_START_TIME
{
    FIELD_NAME = gsm105
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm106
    FIELD_XDRKEY = FIRSTCDR_START_TIME
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ADDUP_FLAG
{
    FIELD_NAME = gsm106
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm107
    FIELD_XDRKEY = ADDUP_FLAG
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //MEMBER_MSISDN
{
    FIELD_NAME = gsm107
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm108
    FIELD_XDRKEY = MEMBER_MSISDN
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //MEDIA_LIST
{
    FIELD_NAME = gsm108
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm109
    FIELD_XDRKEY = MEDIA_LIST
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //INPUT_TAB_NAME
{
    FIELD_NAME = gsm109
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm110
    FIELD_XDRKEY = INPUT_TAB_NAME
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //CDR_QUERY_FLAG
{
    FIELD_NAME = gsm110
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm111
    FIELD_XDRKEY = CDR_QUERY_FLAG
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //USER_BILL_DAY
{
    FIELD_NAME = gsm111
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm112
    FIELD_XDRKEY = USER_BILL_DAY
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //USER_PROP_INFO
{
    FIELD_NAME = gsm112
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm113
    FIELD_XDRKEY = USER_PROP_INFO
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ANALYSE_FLAG
{
    FIELD_NAME = gsm113
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm114
    FIELD_XDRKEY = ANALYSE_FLAG
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //HPLMN4
{
    FIELD_NAME = gsm114
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm115
    FIELD_XDRKEY = HPLMN4
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //OPP_RESOURSE_AREACODE
{
    FIELD_NAME = gsm115
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm116
    FIELD_XDRKEY = OPP_RESOURSE_AREACODE
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //USER_GROUP_INFO
{
    FIELD_NAME = gsm116
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm117
    FIELD_XDRKEY = USER_GROUP_INFO
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //NP_FLAG
{
    FIELD_NAME = gsm117
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm118
    FIELD_XDRKEY = NP_FLAG
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //OPP_NP_FLAG
{
    FIELD_NAME = gsm118
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm119
    FIELD_XDRKEY = OPP_NP_FLAG
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //LATE_LINK
{
    FIELD_NAME = gsm119
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm120
    FIELD_XDRKEY = LATE_LINK
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //INPUT_TIME
{
    FIELD_NAME = gsm120
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm121
    FIELD_XDRKEY = INPUT_TIME
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
FIELD //ROW_ID
{
    FIELD_NAME = gsm121
    FIELD_LEAF = YES
    FIELD_NEXT_FIELD = gsm122
    FIELD_XDRKEY = ROW_ID
    DECODE
    {
        DECODE_FUNC_TYPE = decode_asc
        DECODE_SPLIT = ;
    }
}
