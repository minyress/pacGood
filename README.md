# 好用的PAC列表
gfwlist不好用，我基于网络上的列表修改了一个适用自己的规则。
# 地址
[固定地址](https://raw.githubusercontent.com/WillGhost/pacGood/master/pac.txt) 因与Tor端口冲突，端口我改成了2080
# 分流策略
### 策略
1. 命中`bypass`的域名走代理
2. 命中`mainland`的域名走直连
3. 命中这些域名后缀`cn`,`com`,`net`,`fm`,`gs`,`[0-9]`(IP访问)，走直连
4. 以上都未命中走代理
### 特色
无论新增还是存量的`org`或`io`后缀都会走代理，但是遇到站点在境内的话需要加入`mainlan`
# 使用方法
### Windows10
`开始` `设置` `网络和Internet 代理`

启用`使用设置脚本`添加`脚本地址`并`保存`
确认本地SOCKS监听的端口与pac一致
重启浏览器测试 [http://ip111.cn/](http://ip111.cn/)
### 其他系统参考Win10
