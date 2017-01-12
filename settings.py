DOWNLOAD_DELAY = 1 # 添加下载延迟配置
ITEM_PIPELINES = {'mzt.pipelines.MztImagesPipeline': 1} # 添加图片下载 pipeline
IMAGES_STORE = '.' # 设置图片保存目录