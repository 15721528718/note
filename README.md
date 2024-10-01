# note

删除MAC自动生成的DS_Store文件
    本文主要记录如何删除MAC自动生成的DS_Store文件。
目录
删除MAC自动生成的DS_Store文件
1.步骤1
2.步骤2
3.步骤3
1.步骤1
    打开MAC自带的终端，并转到你想要删除的文件所在的目录，输入如下代码，将以".DS_Store"为后缀的文件都手动删除。

find . -name '*.DS_Store' -type f -delete
1
2.步骤2
    使用下面的代码设置：取消自动生成以".DS_Store"为后缀的文件。这样设置之后就不会再生成该文件了。

defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
1
3.步骤3
    如果想要恢复生成以".DS_Store"为后缀的文件，则使用下述代码即可恢复生成。

defaults delete com.apple.desktopservices DSDontWriteNetworkStores
1
上述结果亲测有效。
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
                        
原文链接：https://blog.csdn.net/weixin_43981621/article/details/122405264
