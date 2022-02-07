# streeter

### ⚠️注意
1.本程序的工作原理是先通过输入的地址获取经纬度，然后再周边搜索最近的街道办事处，因此搜索结果不保证准确，也不保证一定有搜索结果！
2.仅限查询中国地区的街道

#### 介绍
利用高德地图api通过地址获取所属街道办

#### 安装教程

1.pip安装requests, jieba
2.下载仓库中的streeter.py

#### 使用说明

1.请在streeter.py顶部KEY和CITY变量处填写能够访问高德地图webapi的key和所属城市（省级及以下，市级及以上即可）
2.以任意方式调用streeter中的get_streeter，函数会返回一个列表包含可能的结果(1~3个)，大多数情况下列表只会包含一个结果，当有多个结果时一般第一个是正确结果。或者直接打开streeter.py，输入地址即可看到返回结果。
3.每次查询大概需要1s，主要用于jieba分词来从地址中组合街道名（首先编程水平也是）

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request