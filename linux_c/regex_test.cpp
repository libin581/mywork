//C语言中的正则匹配， 包含regex.h头文件就可以
//在/home/ut/study/mywork/linux_c中，寻找*.txt文件

#include <stdio.h>
#include <regex.h> 
#include <string>
#include <iostream>
#include <sys/stat.h>
#include <dirent.h>
#include <string.h>
#include <vector>
#include <errno.h>

using namespace std;

int main(){
    
    
    regex_t tRegex;
	int iFileNum	= 0;
    vector<string> listFiles;

	if(regcomp(&tRegex, "[a-z]+.txt", REG_EXTENDED | REG_NOSUB) != 0)
	{
		cout<<"contains regular expression, but Invalid"<<endl;
		return -1;
	}
    
    string strInput = "/home/ut/study/mywork/linux_c";
	printf("input_dir: %s\n", strInput.c_str());
	DIR *dir = opendir(strInput.c_str());
	if(!dir)
	{
		printf("error: can't open folder %s", strInput.c_str());
		regfree(&tRegex);
		return -1;
	}

	int iPathLen = strInput.size();
	char *pEntry = new char[iPathLen + 256];
	memset(pEntry, 0x0, iPathLen + 256);
	//snprintf(pEntry, iPathLen+1, "%s/", strInput.c_str());//snprintf will automaticly add \0 for the last one, so be care
	sprintf(pEntry, "%s/", strInput.c_str());
	struct dirent *result;
	struct stat entryInfo;
	struct dirent entry;
    int maxFileOnce = 10;
	while( (maxFileOnce == 0 || maxFileOnce > iFileNum ) && readdir_r(dir, &entry, &result) == 0 && result != 0 )
	{
		if(entry.d_name[0] == '.')//don't list the hidden files and folders
			continue;
		memset(pEntry + iPathLen + 1, 0x0, 255);
		//snprintf(pEntry + iPathLen + 1, 255, "%s", entry.d_name);
		sprintf(pEntry + iPathLen + 1, "%s", entry.d_name);
		if(stat(pEntry, &entryInfo) != 0)
		{
			printf("Error statting %s: %s\n", pEntry, strerror(errno));
			continue;
		}
		if(S_ISDIR(entryInfo.st_mode))
		{
			continue;
		}
		if(S_ISREG(entryInfo.st_mode))
		{
			if(regexec(&tRegex, entry.d_name, 0, 0, 0) != 0)
			continue;
			//entryInfo.st_mtime;//time of last modification
			listFiles.push_back(entry.d_name);
			iFileNum++;
		}
	}//end while

	regfree(&tRegex);
	closedir(dir);
	if(pEntry)
		delete pEntry;
	pEntry = NULL;
    
    for (vector<string>::iterator it = listFiles.begin(); it!= listFiles.end(); it++){
            printf("%s\n", (*it).c_str());
    }


	//===============================================================
    const char *pAudio;
    const char *pVideo;
    const char *pValue;
    int nAudioFlag = 0;
    int nVideoFlag = 0;
    regex_t rePort;
    regex_t reAudio;
    regex_t reVideo;
    regmatch_t matchPort[1];
    regmatch_t matchAudio[1];
    regmatch_t matchVideo[1];
    vector<string> vecAudioPort;
    vector<string> vecVideoPort;
    char strMatch[20];
    char errbuf[1024];
    
    const char * srcString1 = "M,20170303121035,audio 44016  RTP/AVP  8  101";

    const char* patternPort = "[0-9]+"; 
    if ( regcomp(&rePort, patternPort, REG_EXTENDED ) != 0 ){
        printf("regcomp() error!, pattern:%s\n", patternPort);
        return 0;
    }

    const char* patternAudio = "audio\\s+[0-9]+";
    if ( regcomp(&reAudio, patternAudio, REG_EXTENDED ) != 0 ){
        printf("regcomp() error!, pattern:%s\n", patternAudio);
        return 0;
    }

    const char* patternVideo = "video\\s+[0-9]+";
    if ( regcomp(&reVideo, patternVideo, REG_EXTENDED ) != 0 ){
        printf("regcomp() error!, pattern:%s\n", patternVideo);
        return 0;
    }
    
    pValue = srcString1;
    printf("VIDEO:\n%s\n", pValue);
    while(1)
    {
        int err = regexec(&reAudio, pValue, 1, matchAudio, 0);
        if(err == REG_NOMATCH){
            //printf("no audio-port match\n");
            break;
        }
        else if (err){
            regerror(err,&reAudio,errbuf,sizeof(errbuf));
            printf("err:%s\n",errbuf);
            printf("regexec() error 1!\n");
            return 0;            
        }
        
        pAudio = pValue + matchAudio[0].rm_so;
        nAudioFlag++;
        
        //printf("%d\n",nAudioFlag);
        //return 0;
        
        err = regexec(&rePort, pAudio, 1, matchPort, 0);
        if(err == REG_NOMATCH){
            printf("regexec() error 2!\n");
            return 0; 
        }
        else if (err){
            regerror(err,&rePort,errbuf,sizeof(errbuf));
            printf("err:%s\n",errbuf);
            printf("regexec() error 2!\n");
            return 0;            
        }
        
        
        unsigned len = matchPort[0].rm_eo - matchPort[0].rm_so;
        strncpy(strMatch, pAudio + matchPort[0].rm_so, len);
        strMatch[len]=0;

        vecAudioPort.push_back(strMatch);
        
        pValue = pAudio + matchPort[0].rm_so;
    }

    pValue = srcString1;
    while(1)
    {
        int err = regexec(&reVideo, pValue, 1, matchVideo, 0);
        if(err == REG_NOMATCH){
            //printf("no vedio-port match\n");
            break;
        }
        else if (err){
            regerror(err,&reVideo,errbuf,sizeof(errbuf));
            printf("err:%s\n",errbuf);
            printf("regexec() error 3!\n");
            return 0;            
        }
        
        
        pVideo = pValue + matchVideo[0].rm_so;
        nVideoFlag++;
        
        err = regexec(&rePort, pVideo, 1, matchPort, 0);
        if(err == REG_NOMATCH){
            printf("regexec() error 4!\n");
            return 0; 
        }
        else if (err){
            regerror(err,&rePort,errbuf,sizeof(errbuf));
            printf("err:%s\n",errbuf);
            printf("regexec() error 4!\n");
            return 0;            
        }
        
        
        unsigned len = matchPort[0].rm_eo - matchPort[0].rm_so;
        strncpy(strMatch, pVideo + matchPort[0].rm_so, len);
        strMatch[len]=0;

        vecVideoPort.push_back(strMatch);
        
        pValue = pVideo + matchPort[0].rm_eo;
    }

    regfree(&rePort);
    regfree(&reAudio);
    regfree(&reVideo);

    printf("audio num:%d\n", nAudioFlag);
    printf("audio port:\n");
    for (vector<string>::iterator it=vecAudioPort.begin(); it !=vecAudioPort.end(); it++) {
        printf("%s\n", (*it).c_str());
    }

    printf("video num:%d\n", nVideoFlag);
    printf("video port:\n");
    for (vector<string>::iterator it=vecVideoPort.begin(); it !=vecVideoPort.end(); it++) {
        printf("%s\n", (*it).c_str());
    }

    //====================================================
    string lastVideoPort = "2134";
    string strVideoPort = "video ";
    strVideoPort += lastVideoPort;
    
    pValue = "  as  video 2134ddd Inactive  ";
    pVideo = strstr(pValue, strVideoPort.c_str());
    if (pVideo == NULL){
        printf("%s not found\n", strVideoPort.c_str());
        return 0;
    }
    else if (NULL != strstr(pVideo, "Inactive")){

        printf("Inactive found\n");
        return 0;
    }
    
}
