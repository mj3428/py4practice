#redis中数据库默认是多少个db 及作用？  
redis下，数据库是由一个整数索引标识，而不是由一个数据库名称。默认情况下，一个客户端连接到数据库0。  
redis配置文件中下面的参数来控制数据库总数：  
/etc/redis/redis.conf  
文件中，有个配置项 databases = 16 //默认有16个数据库