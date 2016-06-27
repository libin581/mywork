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
#include <errno.h>
#include <sys/epoll.h>
using namespace std;
#define PORT 1314
#define MAX_LINE_LEN 1024
#define EPOLL_EVENTS 1024

int main()   
{
    struct sockaddr_in cli_addr, server_addr;
    socklen_t addr_len;
    int one,flags,nrcv,nwrite,nready;
    
    int listenfd,epollfd,connfd;
    char buf[MAX_LINE_LEN],addr_str[INET_ADDRSTRLEN];
    
    struct epoll_event ev;
    std::vector<struct epoll_event> eventsArray(16);

    bzero(&server_addr, sizeof server_addr);
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    
    listenfd = socket(AF_INET, SOCK_STREAM, 0);
    
    if( listenfd < 0)
    {
        perror("socket open error! \n");
        exit(1);
    }
    
    
    one = 1;
    setsockopt(listenfd,SOL_SOCKET,SO_REUSEADDR, &one, sizeof one);
    
    flags = fcntl(listenfd,F_GETFL,0);
    fcntl(listenfd, F_SETFL, flags | O_NONBLOCK);
    
    if(bind(listenfd,reinterpret_cast<struct sockaddr *>(&server_addr),sizeof(server_addr)) < 0)
    {
        perror("Bind error! \n");
        exit(1);
    }
    
    listen(listenfd, 100);
    
    epollfd = epoll_create(EPOLL_EVENTS);
    
    if(epollfd < 0)
    {
        printf("epoll_create error: %s \n",strerror(errno));
        exit(1);
    }
    
    ev.events = EPOLLIN;
    ev.data.fd = listenfd;
    
    if(epoll_ctl(epollfd, EPOLL_CTL_ADD,listenfd,&ev) < 0)
    {
        printf("register listenfd failed: %s",strerror(errno));
        exit(1);
    }
    
    while(1)
    {
        nready = epoll_wait(epollfd,&(*eventsArray.begin()),static_cast<int>(eventsArray.size()),-1);
        
        if(nready < 0)
        {
            printf("epoll_wait error: %s \n",strerror(errno));
        }
        
        for( int i = 0; i < nready; i++)
        {
            if(eventsArray[i].data.fd == listenfd)
            {
                addr_len = sizeof cli_addr;
                connfd = accept(listenfd, reinterpret_cast<struct sockaddr *>(&cli_addr),&addr_len);
                
                if( connfd < 0)
                {
                    if( errno != ECONNABORTED || errno != EWOULDBLOCK || errno != EINTR)
                    {
                        printf("accept socket aborted: %s \n",strerror(errno));
                        continue;
                    }
                }
                
                flags = fcntl(connfd, F_GETFL, 0);
                fcntl(connfd,F_SETFL, flags | O_NONBLOCK);
                
                ev.events = EPOLLIN;
                ev.data.fd = connfd;
                
                if(epoll_ctl(epollfd,EPOLL_CTL_ADD,connfd,&ev) < 0)
                {
                    printf("epoll add error: %s",strerror(errno));
                }
                
                printf("recieve from : %s at port %d\n", inet_ntop(AF_INET,&cli_addr.sin_addr,addr_str,INET_ADDRSTRLEN),cli_addr.sin_port);
                
                if(--nready < 0)
                {
                    continue;
                }
        
            }
            else
            {
                ev = eventsArray[i];
                
                printf("fd = %d \n",ev.data.fd);
                
                memset(buf,0,MAX_LINE_LEN);
                
                if( (nrcv = read(ev.data.fd, buf, MAX_LINE_LEN)) < 0)
                {
                    if(errno != EWOULDBLOCK || errno != EAGAIN || errno != EINTR)
                    {
                        printf("read error: %s\n",strerror(errno));
                    }
                }
                else if( 0 == nrcv)
                {
                    close(ev.data.fd);
                    printf("close: %d fd \n",ev.data.fd);
                    eventsArray.erase(eventsArray.begin() + i);
                }
                else
                {
                    printf("nrcv, content: %s\n",buf);
                    nwrite = write(ev.data.fd, buf, nrcv);
                    if( nwrite < 0)
                    {
                        if(errno != EAGAIN || errno != EWOULDBLOCK)
                            printf("write error: %s\n",strerror(errno));
                    }
                    printf("nwrite = %d\n",nwrite);
                }
            }
        }
    }
    
    return 0;
}



