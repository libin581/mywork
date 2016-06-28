t_sOutPostFix		= "";
t_sOutDrType		= "dr_ismg";
t_sErrMsg		= "";

t_iTreatFlag		= 0;
t_iTradeMark		= 0;
t_iDrType		= 0;
t_iServiceID		= 50006;
t_iProductID		= 0;
t_iRateProdID		= 0;
t_sUserNumber		= "";
t_sSourceType		= "";
t_sSpcode		= "";
t_sServiceCode		= "";
t_sOperatorCode		= "";
t_sMessageLenth		= "";
t_iBillFlag		= 0;
t_sSendState		= "";
t_sSendPriority		= "";
t_sSequenceNo		= "";
t_sRecordType		= "";
t_sStopTime		= "";
t_sIsmgId		= "";
t_iForwardIsmgId	= 0;
t_sOppNumber		= "";
t_sOppType		= "";

t_iTreatFlag		= GetXdrIntValue("TREAT_FLAG");
t_iTradeMark		= GetXdrIntValue("TRADEMARK");
t_iDrType		= GetXdrIntValue("DR_TYPE");
t_iProductID		= GetXdrIntValue("PRODUCT_ID");
t_sRateProdID		= GetXdrStrValue("RATE_PROD_ID");
t_sUserNumber		= GetXdrStrValue("USER_NUMBER");
t_sSourceType		= GetXdrStrValue("SOURCE_TYPE");
t_sSpcode		= GetXdrStrValue("SP_CODE");
t_sServiceCode		= GetXdrStrValue("SERVICE_CODE");
t_sOperatorCode		= GetXdrStrValue("OPERATOR_CODE");
t_sMessageLenth		= GetXdrStrValue("MESSAGE_LENGTH");
t_iBillFlag		= GetXdrIntValue("BILL_FLAG");
t_sSendState		= GetXdrStrValue("SEND_STATE");
t_sSendPriority		= GetXdrStrValue("SEND_PRIORITY");
t_sSequenceNo		= GetXdrStrValue("SEQUENCE_NO");
t_iRecordType		= GetXdrIntValue("RECORD_TYPE");
t_sStopTime		= GetXdrStrValue("STOP_TIME");
t_sIsmgId		= GetXdrStrValue("ISMG_ID");
t_iForwardIsmgId	= GetXdrIntValue("FORWARD_ISMG_ID");
t_sOppNumber		= GetXdrStrValue("OPP_NUMBER");
t_sOppType		= GetXdrStrValue("OPP_TYPE");

//TRADEMARK default 0
PutXdrIntValue("TRADEMARK",	t_iTradeMark);

//gansu
//DEAL_PARA1 = 0   ,1102,1103,1322,1104,60101,8002,103,104,304,105, 5,1123,90508,8001,8007,8003,90604,787,5600,5601,1312,80404,90515,106,8011, 709,other
//DEAL_PARA2 = HYWG,ISMG,ISMG,ISMG,ISMG, ISMG,ISMG,MMS,WAP,WAP,WAP,KJ, STM,  WAP,  KJ,  KJ,  KJ,  MMS,MMS,ISMG,ISMG,ISMG, ISMG, ISMG,MMS,  KJ,ISMG,OTHER
//jiangxi
//DEAL_PARA1 = 0   ,60002,1102,1122,1312,1103,1322,1104,60101,8002,1126,90515,103,1402,90604,104,304,105,7104,90502, 5,60301,8007,1123,8011,8003,90416,90605,90508,other
//DEAL_PARA2 = HYWG, ISMG,ISMG,ISMG,ISMG,ISMG,ISMG,ISMG, ISMG,ISMG,ISMG, ISMG,MMS, MMS,  MMS,WAP,WAP,WAP, WAP,  WAP,KJ,   KJ,  KJ, STM,  KJ,  KJ, ISMG,  MMS,  WAP,OTHER
//neimeng
//DEAL_PARA1 =   0,880602,   ,,other   60002,1124,981102,881102,1102,1312,1103,1105,1322,709,1104, 60101,8002,  103,106,80601,880601,90604  731,104,304,105,90508,90516,  5,729,8007,60301,8011,8003,  1123
//DEAL_PARA2 =   HYWG,HYWG,  OTHER     ISMG, ISMG,ISMG,  ISMG,  ISMG,ISMG,ISMG,ISMG,ISMG,ISMG,ISMG,ISMG, ISMG,  MMS,MMS,MMS,  MMS,   MMS,   WAP,WAP,WAP,WAP,WAP,  WAP,    KJ,KJ,KJ,   KJ,  KJ,  KJ,    STM,
if ( t_iDrType == 1102		|| t_iDrType == 1103 	|| t_iDrType == 1322 || t_iDrType == 1104
        || t_iDrType == 60101	|| t_iDrType == 8002 	|| t_iDrType == 1312 || t_iDrType == 90515	//ISMG
        || t_iDrType == 90520                                                                           //add 个人彩云订购关系计费 20121116
        || t_iDrType == 5600	|| t_iDrType == 5601 	|| t_iDrType == 80404|| t_iDrType == 709	//gansu add
        || t_iDrType == 90416	|| t_iDrType == 1126 	|| t_iDrType == 1122 || t_iDrType == 60002	//jiangx add
        || t_iDrType == 1124	|| t_iDrType == 981102	|| t_iDrType == 881102	//neimeng add
        || t_iDrType == 732004 )	//xizang add
{
    t_sOutDrType	= "dr_ismg";
    t_sOutPostFix	= ".ismg";
    t_iServiceID	= 50006;

    //FIELD_DUP_XDR_FIELD_NAME = OPP_NUMBER
    PutXdrStrValue("OPP_NUMBER"		,	t_sUserNumber	);
    PutXdrIntValue("SEND_STATE"		,	0		);
    PutXdrIntValue("SEND_PRIORITY"		,	0		);
}
else if (t_iDrType == 0		//HYWG
         || t_iDrType == 1222 || t_iDrType == 81701 || t_iDrType == 81702	//xizang add
         || t_iDrType == 880602)	//neimeng add
{
    t_sOutDrType	= "dr_ismg";
    t_sOutPostFix	= ".hywg";
    t_iServiceID	= 50006;

    t_iDrType	= 1222;
    PutXdrIntValue("DR_TYPE"		,	t_iDrType	);
    //FIELD_DUP_XDR_FIELD_NAME = OPP_NUMBER
    PutXdrStrValue("OPP_NUMBER"		,	t_sUserNumber	);
    PutXdrStrValue("SEND_STATE"		,	t_sSendState	);
    PutXdrStrValue("SEND_PRIORITY"		,	t_sSendPriority	);
}
else if (t_iDrType == 103 || t_iDrType == 90604		//MMS
         || t_iDrType == 787 || t_iDrType == 106		//gansu add
         || t_iDrType == 90605 || t_iDrType == 1402	//jiangx add
         || t_iDrType == 80601 || t_iDrType == 880601 )	//neimeng add
{
    t_sOutDrType	= "dr_mms";
    t_sOutPostFix	= ".mms";
    t_iServiceID	= 50014;
    if (t_sRateProdID == "")
    {
        t_sRateProdID	= "50014001";
    }

    //RECORD_XDR_OUTPUT INFO_TYPE = 0
    //RECORD_XDR_OUTPUT APP_TYPE = 0
    //RECORD_XDR_OUTPUT TRANSMIT_TYPE = 0
    //RECORD_XDR_OUTPUT CARRY_TYPE = 0
    //RECORD_XDR_OUTPUT SEND_STATUS =1
    //RECORD_XDR_OUTPUT STORE_TIME =1
    PutXdrIntValue("INFO_TYPE"		,	0	);
    PutXdrIntValue("APP_TYPE"		,	0	);
    PutXdrIntValue("TRANSMIT_TYPE"		,	0	);
    PutXdrIntValue("CARRY_TYPE"		,	0	);
    PutXdrIntValue("SEND_STATUS"		,	1	);
    PutXdrIntValue("STORE_TIME"		,	1	);

    PutXdrStrValue("MM_SEQ"			,	t_sSequenceNo	);
    if (t_iRecordType == 1)
    {
        t_iRecordType = 3;
    }
    PutXdrIntValue("MM_TYPE"		,	t_iRecordType	);
    PutXdrStrValue("RECEIVE_ADDRESS"	,	t_sOppNumber	);
    PutXdrStrValue("SER_CODE"		,	t_sServiceCode	);
    PutXdrStrValue("OPER_CODE"		,	t_sOperatorCode	);
    if (t_iBillFlag == 1)
    {
        t_iBillFlag = 0;
    }
    else if (t_iBillFlag == 2)
    {
        t_iBillFlag = 1;
    }
    else if (t_iBillFlag == 3)
    {
        t_iBillFlag = 2;
    }
    PutXdrIntValue("CHARGE_TYPE"		,	t_iBillFlag	);
    PutXdrStrValue("MM_LENGTH"		,	t_sMessageLenth);
    PutXdrStrValue("RECEIVE_TIME"		,	t_sStopTime);
}
else if ( t_iDrType == 104 || t_iDrType == 304 || t_iDrType == 105 || t_iDrType == 90508	//WAP
          || t_iDrType == 90502 || t_iDrType == 7104	//jiangx add
          || t_iDrType == 731 || t_iDrType == 90516 )
{
    t_sOutDrType	= "dr_wap";
    t_sOutPostFix	= ".wap";
    t_iServiceID	= 50007;
    if (t_sRateProdID == "")
    {
        t_sRateProdID	= "50007001";
    }


    PutXdrStrValue("SERVICE_CODE"		,	t_sOperatorCode	);
    PutXdrIntValue("CHARGE_TYPE"		,	3	);

    if (t_iBillFlag == 1 || t_iBillFlag == 2)
    {
        t_iBillFlag = 0;
    }
    else if (t_iBillFlag == 3)
    {
        t_iBillFlag = 10;
    }
    else if (t_iBillFlag == 4)
    {
        t_iBillFlag = 11;
    }
    PutXdrIntValue("RECORD_TYPE"		,	t_iBillFlag	);
    PutXdrStrValue("CDR_STATE"		,	t_sSendState	);
    PutXdrStrValue("GATEWAY_ID"		,	t_sIsmgId	);
}
else if (t_iDrType == 5 || t_iDrType == 8007 || t_iDrType == 8003 || t_iDrType == 8011	//KJ
         || t_iDrType == 8001	//gansu add
         || t_iDrType == 60301	//jiangx add
         || t_iDrType == 729 )	//neimeng add
{
    t_sOutDrType	= "dr_kj";
    t_sOutPostFix	= ".kj";
    t_iServiceID	= 50017;
    if (t_sRateProdID == "")
    {
        t_sRateProdID	= "50017001";
    }

    //RECORD_XDR_OUTPUT APP_TYPE = 0
    //RECORD_XDR_OUTPUT SRC_TYPE = 0
    //RECORD_XDR_OUTPUT DNLOAD_DURATION = 0
    //RECORD_XDR_OUTPUT VALID_TIMES = 0
    //RECORD_XDR_OUTPUT ONLINE_DURATION = 0
    //RECORD_XDR_OUTPUT CARRY_TYPE = 0
    //RECORD_XDR_OUTPUT OPP_TYPE = 0
    PutXdrIntValue("APP_TYPE"		,	0	);
    PutXdrIntValue("SRC_TYPE"		,	0	);
    PutXdrIntValue("DNLOAD_DURATION"	,	0	);
    PutXdrIntValue("VALID_TIMES"		,	0	);
    PutXdrIntValue("ONLINE_DURATION"	,	0	);
    PutXdrIntValue("CARRY_TYPE"		,	0	);
    PutXdrIntValue("OPP_TYPE"		,	0	);

    PutXdrStrValue("SERVICE_CODE"		,	t_sOperatorCode	);
    PutXdrStrValue("OPER_CODE"		,	t_sOperatorCode	);
    PutXdrIntValue("CHARGE_TYPE"		,	3	);
    if (t_iBillFlag == 1)
    {
        t_iBillFlag = 0;
    }
    else if (t_iBillFlag == 2)
    {
        t_iBillFlag = 1;
    }
    else if (t_iBillFlag == 3)
    {
        t_iBillFlag = 4;
    }
    PutXdrIntValue("CHARGE_TYPE"		,	t_iBillFlag	);
    PutXdrStrValue("CDR_STATE"		,	t_sSendState	);
    PutXdrStrValue("PRIORITY"		,	t_sSendPriority	);
    PutXdrStrValue("DATA_SIZE"		,	t_sMessageLenth	);
    if (t_iForwardIsmgId == 1)
    {
        t_iForwardIsmgId = 99;
    }
    PutXdrIntValue("DISCOUNT"		,	t_iForwardIsmgId);
}
else if (t_iDrType == 1123)	//STM
{
    t_sOutDrType	= "dr_cbs";
    t_sOutPostFix	= ".stm";
    t_iServiceID	= 50050;
    //t_sRateProdID	= "50017001";

    //RECORD_XDR_OUTPUT SERVICE_TYPE = 0
    //RECORD_XDR_OUTPUT OPP_NUMBER = 0
    //RECORD_XDR_OUTPUT VOLUME = 0
    //RECORD_XDR_OUTPUT UP_VOLUME1 = 0
    //RECORD_XDR_OUTPUT DN_VOLUME1 = 0
    //RECORD_XDR_OUTPUT APP_TYPE = 0
    //RECORD_XDR_OUTPUT DN_VOLUME2 = 0
    //RECORD_XDR_OUTPUT UP_VOLUME2 = 0
    //RECORD_XDR_OUTPUT APNNI_CODE = 0
    PutXdrIntValue("PRODUCT_ID"		,	50050001);
    PutXdrIntValue("SERVICE_TYPE"		,	0	);
    PutXdrIntValue("OPP_NUMBER"		,	0	);
    PutXdrIntValue("VOLUME"			,	0	);
    PutXdrIntValue("UP_VOLUME1"		,	0	);
    PutXdrIntValue("DN_VOLUME1"		,	0	);
    PutXdrIntValue("APP_TYPE"		,	0	);
    PutXdrIntValue("UP_VOLUME2"		,	0	);
    PutXdrIntValue("DN_VOLUME2"		,	0	);
    PutXdrIntValue("APNNI_CODE"		,	0	);

    PutXdrStrValue("CP_CODE"		,	t_sSpcode	);
    PutXdrStrValue("SP_CODE"		,	""	);
    PutXdrStrValue("SERVICE_PACKET_CODE"	,	t_sServiceCode	);
    PutXdrStrValue("DURATION"		,	t_sMessageLenth	);
    PutXdrIntValue("CHARGE_TYPE"		,	t_iBillFlag	);
}
else
{
    t_sOutDrType	= "dr_ismg";
    t_sOutPostFix	= "";
    t_iServiceID	= 50006;

    PutXdrIntValue("TREAT_FLAG",1);
    t_sErrMsg	= "E000:filter cdr whith dr_type is " + itoa(t_iDrType);
    PutXdrStrValue("ERR_CODE",t_sErrMsg);
}

PutXdrIntValue("SERVICE_ID"		,	t_iServiceID	);
PutXdrStrValue("RATE_PROD_ID"		,	t_sRateProdID	);
PutXdrStrValue("XDR_OUT_DR_TYPE"	, 	t_sOutDrType	);
PutXdrStrValue("XDR_OUT_POSTFIX"	,	t_sOutPostFix	);

return;
}
