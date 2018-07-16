#include <string.h>
#include <stdio.h>
#include <stdlib.h>

long long atol64(const char * szStr)
{
  if ( szStr == NULL  ||  strcmp(szStr, "") == 0) return 0;
  long long llTmp;
  sscanf(szStr, "%lld", &llTmp);
  return llTmp;
}

int	str2str_divideStrRounding( 		const char* pIn,
								char* pOut,
								const char* szMulti)
{

	if( NULL == pOut )
	{
		return -1;
	}
	long long temp=(atol64(pIn)+0.0)/atol64(szMulti)+0.5;
	snprintf( pOut, 64, "%lld",  temp);
	return 0;

}

int str2str_divideOddStr( 		const char* pIn,
								char* pOut,
								const char* szMulti)
{

	if( NULL == pOut )
	{
		return -1;
	}

	snprintf( pOut, 64, "%lld", ( atol64( pIn ) / atol64( szMulti ) ) );

	return 0;

}

int   str2str_divideStrAdd(              const char* pIn,
                                                                char* pOut,
                                                                const char* szMulti)
{

        if( NULL == pOut )
        {
                return -1;
        }

	long long  llMulti = atol64(szMulti);
	if(0 == llMulti)
	{
		return -1;
	}

	long long  llPin = atol64(pIn);
	if(0 == llPin)
	{
		return 0;
	}

        if( 0 == (llPin % llMulti))
        {
                snprintf( pOut, 64, "%lld", (llPin / llMulti) );
        }
        else
        {
                snprintf( pOut, 64, "%lld", (llPin / llMulti + 1 ) );
        }
        return 0;

}

int convert_vpmn_cell_id(){
    char strCellIdKey2[64] = {0};
    strncpy(strCellIdKey2, "11111", 30);

    char *pszPointer2=new char[10];
    
    printf("convert_vpmn_cell_id, 1 pszPointer2=0x%X\n", pszPointer2);
    
    pszPointer2 = strchr(strCellIdKey2, ' ');

    printf("convert_vpmn_cell_id, 2 pszPointer2=0x%X\n", pszPointer2);
    
    if (pszPointer2)
    {

        int  len = strlen(pszPointer2);
        int  num=0;
        
        for(int i=0; i<len; i++)
        {
                if(     (pszPointer2[i] >= 'a' && pszPointer2[i] <= 'z') ||
                        (pszPointer2[i] >= 'A' && pszPointer2[i] <= 'Z') ||
                        (pszPointer2[i] >= '0' && pszPointer2[i] <= '9') )
                {
                        num++;
                }
        }

        if (num == 0)
        {
            pszPointer2=pszPointer2+4;
            char PTmp[20] ="0000";
            strcat(PTmp, pszPointer2);
            //xdrLacId.set_value(PTmp);
            //xdrRecord.insert_field( xdrFieldLacIdKey, xdrLacId );
            printf("convert_vpmn_cell_id, %s\n", PTmp);
        }
        else if (num == 1)
        {
            pszPointer2=pszPointer2+3;
            char PTmp[20] ="000";
            strcat(PTmp, pszPointer2);
            //xdrLacId.set_value(PTmp);
            //xdrRecord.insert_field( xdrFieldLacIdKey, xdrLacId );
            printf("convert_vpmn_cell_id, %s\n", PTmp);
        }
        else if (num == 2)
        {
            pszPointer2=pszPointer2+2;
            char PTmp[20] ="00";
            strcat(PTmp, pszPointer2);
            //xdrLacId.set_value(PTmp);
            //xdrRecord.insert_field( xdrFieldLacIdKey, xdrLacId );
            printf("convert_vpmn_cell_id, %s\n", PTmp);
        }
        else if (num == 3)
        {
            pszPointer2=pszPointer2+1;
            char PTmp[20] ="0";
            strcat(PTmp, pszPointer2);
            //xdrLacId.set_value(PTmp);
            //xdrRecord.insert_field( xdrFieldLacIdKey, xdrLacId );
            printf("convert_vpmn_cell_id, %s\n", PTmp);
        }
        
        printf("convert_vpmn_cell_id, num=%d\n", num);
    }
    
	delete[] pszPointer2;
    return 0;
}
    
int main(){
    
    char sIn[] = "1200";
    char sOut[10];
    char szMulti[] = "100";
    printf("%s/%s:\n", sIn, szMulti);
    
    int iret = str2str_divideStrRounding(sIn, sOut, szMulti);
    if (iret == 0){
        printf("str2str_divideStrRounding:%s\n",sOut);
    }
    else{
        printf("failed\n");
    }
    
    iret = str2str_divideOddStr(sIn, sOut, szMulti);
    if (iret == 0){
        printf("str2str_divideOddStr:%s\n",sOut);
    }
    else{
        printf("failed\n");
    }
    
    iret = str2str_divideStrAdd(sIn, sOut, szMulti);
    if (iret == 0){
        printf("str2str_divideStrAdd:%s\n",sOut);
    }
    else{
        printf("failed\n");
    }
    
    
    convert_vpmn_cell_id();
    printf("\n");
}

