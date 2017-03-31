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
}
