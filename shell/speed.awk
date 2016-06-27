#!/bin/awk -f
{
    gsub(/-/,"",$1);
    gsub(/:/,"",$2)
    gsub(/[a-zA-Z"=]/,"",$14);
           gsub(/[a-zA-Z"=]/,"",$15);
    cdrnum=500
           if ($14>cdrnum)
    {
        tag=$1substr($2,1,2);
        total[tag]=total[tag]+$14;
        sum[tag]=sum[tag]+$14*$15;
        fileNum1[tag]=fileNum1[tag]+1;
    }
    else
    {
        fileNum2[tag]=fileNum2[tag]+1;
    }
}
END {
    slen=asorti(total,a_total);
    printf("配置统计话单文件输入数大于%d的话单处理速度信息\n",cdrnum);
    for (i=1; i<=slen; i++)
    {
        printf("当前统计时间:%d年%d月%d日 %d段\n",substr(a_total[i],1,4),substr(a_total[i],5,2),substr(a_total[i],7,2),substr(a_total[i],9));
        printf("话单数:%d\n", total[a_total[i]]);
        printf(">%d条记录文件个数:%d，<=%d条记录文件个数:%d\n", cdrnum, fileNum1[a_total[i]], cdrnum, fileNum2[a_total[i]]);
        printf("处理效率:%.2f\n",sum[a_total[i]]/total[a_total[i]]);
        printf("\n");
    }
}

#cat de_ggprs_iot_cngo_2102.3579.4_165324 | awk -f /billapp/users/libin3/speed.awk
