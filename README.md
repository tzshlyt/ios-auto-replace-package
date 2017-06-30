
### 使用场景

为不同客户做定制化开发同一款app，功能相同，图片素材、显示的文字、配置和证书不同，每次人工替换素材和更换证书打包费时费力，所以使用python脚本实现自动化替换资源，自动化打包。

### 文件说明
*Config.py*  &emsp;&emsp; 配置脚本

*AutoPackage.py*  &emsp;&emsp;  自动化脚本

*PrepareImagesTool.py* &emsp;&emsp; 拷贝工程中的图片结构出来用来更换后准备替换

### 客户需要提供
1、app的中英文名字

2、服务器的ip地址

3、反馈邮箱

4、微信和QQ的分享Id，用于支持分享文件到微信和qq，需要到微信和qq开发者平台申请

5、到apple developer平台申请4个App Id并下载描述文件,如`Config.y`中所示

6、在mac电脑中导出p12文件

7、*customization* 文件夹中 *Contents.json* 描述大小和同名的图片素材,并放在对应目录下


### 功能流程说明
`替换图片资源`-->`替换文字资源`-->`替换 group id`-->`替换微信和qq分享 id`-->`替换反馈邮箱`-->`设置服务器地址`-->`修改配置文件重新签名不同的scheme`-->`打包ipa`

### 使用说明(ios开发者）

#### 准备阶段

+ 执行`$ python PrepareImagesTool.py`,将工程中的图片拷贝到 *customization* 目录下，用于提供给客户提供定制化的图片

#### 打包阶段

+ 1、安装`pip`
	+ 安装命令：`$ python get-pip.py`

+ 2、安装Python虚拟环境virtualenv
	+ `$ sudo pip install virtualenv`

+ 3、进入当前文件目录

   + 为一个工程创建一个虚拟环境
	
		`$ virtualenv env` 
	
	+ 激活虚拟环境  
	
		`$ source env/bin/activate` 
		
+ 4、安装所需Python包

	```
	$ pip install -v Pillow==4.0.0   // 用于比较图片大小
	$ pip install -v pbxproj==2.0.5  // 用于处理xcode配置文件
	
	```

+ 5、配置项目
	+ 将图片放入 *customization* 文件夹下(按照目录结构)
	+ 修改`Config.py`配置文件
	
+ 6、自动打包
	+ 执行`$ python AutoPackage.py`
	
+ 7、打包好的文件保存在 *history* 目录下

	 
### 参考

[https://github.com/xx-li/iOSAutoPackaging](https://github.com/xx-li/iOSAutoPackaging)
