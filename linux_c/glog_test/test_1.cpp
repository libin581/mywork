#include <glog/logging.h>  
  
int main(int argc,char* argv[]) {  
   // If glog is used to parse the command line   
   // google::ParseCommandLineFlags(&argc, &argv, true);  
		    
   // Initialize Google's logging library.  
    google::InitGoogleLogging(argv[0]);  
					  
    //FLAGS_log_dir = "./log";  
	
    google::SetLogDestination(google::GLOG_INFO,"./log");  

    LOG(INFO) << "hello world";  
								  
    return 0;  
}  
