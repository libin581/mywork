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
    
}

