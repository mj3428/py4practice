#参数配置
COM_NAME = '厦门毅昌科技' #公司名

TRANSFORMER = '东1#' #变压器名

KVA = 800 #变压器容量

STARTDAY = '2018年11月23日' #起始时间

ENDDAY = '2018年12月4日' #结束时间

HIGHRISK = 99 #高危数

HIDDENRISK = 120 #隐患数

ELECTRIC = {'200': 21.45, '250': 26.81, '315': 33.78, '400': 42.90, '500': 53.63, '630': 67.57,
            '800': 85.79, '1000': 107.24, '1250': 134.05, '1600': 171.58, '2000': 214.48, '2500': 268.10} #电流阈值

PATH = './data/yichang1_Dec.csv'

POWERYUN_MODEL = './text/poweryun_demo.docx'

NANDECLOUD_MODEL = './text/zjnad_demo.docx'

POWERYUN_BRAND = '电能卫士'

NANDECLOUD_BRAND = 'Nande Cloud电能大脑'
#但凡新的文件参照模板都需要创建ListCLF 清单1着色1; ListCLF2 清单2； ListCLF3清单1着色1； N1 六号加粗宋体 右对齐 1.2倍; 正文1.2倍;
