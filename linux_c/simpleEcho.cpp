// simpleEcho.cpp
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <vector>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>

#define SEVER_PORT 1314
#define MAX_LINE_LEN 1024

using namespace std;

int main()
{
    struct sockaddr_in cli_addr, server_addr;
    socklen_t sock_len;
    vector<int> client(FD_SETSIZE,-1);

    fd_set rset,allset;
    int listenfd, connfd, sockfd, maxfd, nready, ix,maxid, nrcv,one;
    char addr_str[INET_ADDRSTRLEN],buf[MAX_LINE_LEN];


    bzero(&server_addr,sizeof server_addr);
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    server_addr.sin_port = htons(SEVER_PORT);

    listenfd = socket(AF_INET,SOCK_STREAM,0);

    one = 1;
    setsockopt(listenfd, SOL_SOCKET, SO_REUSEADDR,&one, sizeof(one));


    if(bind (listenfd ,(struct sockaddr *)&server_addr ,sizeof server_addr) < 0 )
    {
        printf("socket bind error" );
        return 0;
    }
    
    listen(listenfd ,10);
    
    FD_ZERO(&allset);
    FD_SET(listenfd ,&allset );
    
    maxfd = listenfd ;
    maxid = -1 ;
    
    while(1 )
    {
        rset = allset; //!
        nready = select (maxfd + 1, &rset,NULL,NULL,NULL);
    
        if(nready < 0 )
        {
                printf("select error! \n" );
                exit(1 );
        }
    
        if(FD_ISSET (listenfd , &rset ))
        {
                sock_len = sizeof cli_addr;
                connfd = accept (listenfd ,(struct sockaddr *)&cli_addr , &sock_len);
    
                printf("recieve from : %s at port %d\n" , inet_ntop(AF_INET,&cli_addr .sin_addr ,addr_str ,INET_ADDRSTRLEN ),cli_addr .sin_port );
    
                for(ix = 0 ; ix < static_cast< int>(client .size()); ix++)
                {
                    if(client[ix] < 0 )
                    {
                            client[ix] = connfd ;
                            break;
                    }
                }
    
                printf("client[%d] = %d\n" ,ix ,connfd );
    
                if( FD_SETSIZE == ix)
                {
                    printf("too many client! \n" );
                    exit(1 );
                }
    
                if( connfd > maxfd)
                {
                    maxfd = connfd;
                }
    
                FD_SET(connfd, &allset );
    
                if(ix > maxid )
                {
                    maxid = ix;
                }
                
                if(--nready == 0)
                {
                    continue;
                }
    
        }
    
        for(ix = 0 ; ix <= maxid; ix++)  //<=
        {
                if((sockfd = client [ix ]) < 0)
                {
                    continue;
                }
    
                if(FD_ISSET (sockfd ,&rset ))
                {
                    if( 0 == (nrcv = read(sockfd,buf,MAX_LINE_LEN )))
                    {
                            close(sockfd);
                            client[ix] = -1 ;
                            FD_CLR(sockfd ,&allset );
                    }
                    else
                    {
                            printf("RECIEVE: %s \n" ,buf );
                            write(sockfd,buf,nrcv);
                    }
                }
    
                if(--nready == 0)
                {
                    break;
                }
        }

    }
    
    return 0;
} 



