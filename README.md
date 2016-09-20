# macaowin
准备去澳门玩比大小，采取*正缆(Martinagle)输后加倍下注系统*策略（详见[赌徒谬论](http://baike.baidu.com/link?url=EarWTdUIPjB6GVJPVigSUdR-x3Wegg-1iP4_qi58SPODLRsUH2Ci8ptwYdjmsWwe09_DprV7KtnLyflzFGP0uq)），看看赢率与风险如何

## 运行环境
* python2.7 / python3.5
* win/mac不限

## 安装

```
git clone http://github.com/daimon99/macaowin
cd macaowin
pip install -r req.txt
```

or

直接下载编译后的可执行文件

[win版本](http://github.com/daimon99/macaowin/dist/macaowin.zip)
[mac版本](http://github.com/daimon99/macaowin/dist/macaowin)

## 运行

你要带10000元，起初赌注1000元，看看结果
```
cd dist
macaowin
```

```
python macaowin.py --wallet 100000 --bet 1000
```

也可以：
```
python macaowin.py
带多少钱去澳门 [100000]:
每次基础下注金额 [1000]:
```

帮助：
```
python macaowin.py --help
```

## 示例
```
python macaowin.py
你带了 10000 元, 起始赌注: 1000
开始赌局...
Turn 1: LOSE, 我身上带了 10000 元, 这次下注 1000 元, 钱包还剩 9000 元(最多时钱包有 10000 元, 最多连输次数 1, 累计赢 0, 累计输 1, 赢率: 0 )
Turn 2: LOSE, 我身上带了 10000 元, 这次下注 2000 元, 钱包还剩 7000 元(最多时钱包有 10000 元, 最多连输次数 2, 累计赢 0, 累计输 2, 赢率: 0 )
Turn 3: LOSE, 我身上带了 10000 元, 这次下注 4000 元, 钱包还剩 3000 元(最多时钱包有 10000 元, 最多连输次数 3, 累计赢 0, 累计输 3, 赢率: 0 )
Turn 4: LOSE, 我身上带了 10000 元, 这次下注 8000 元, 钱包还剩 -5000 元(最多时钱包有 10000 元, 最多连输次数 4, 累计赢 0, 累计输 4, 赢率: 0 )
没钱了。。。
但你曾经是 1 倍神!
```
