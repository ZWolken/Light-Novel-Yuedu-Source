# **注意：该项目处在半维护周期内**

# 轻小说阅读书源合集
`Light-Novel-Yuedu-Source`

## 介绍

~~**由于多重原因，该项目处在非维护周期内，任何对于书源的无法正常使用等情况的报告issue，在正常情况下都不会进行解决。**~~<br>
**目前由 [@gongfuture](https://github.com/gongfuture) 转入半维护周期，由于能力不足和精力有限等原因，任何对于书源的issue，可能都不会及时进行解决。**

**欢迎 fork 本仓库修复维护后提出 PR 进行合并。**

> [!CAUTION]
> 内容转载请保持原说明。
> 书源转载整合请保持原源名称以及原源注释。

## 文件说明

1. `Japan_based_bookSource.json`：日轻小说书源文件
2. `China_based_bookSource.json`：国轻小说书源文件
3. `Japanese_original_bookSource.json`：日语原版轻小说书源文件
4. `All_bookSource.json`：日轻、国轻、日轻原版书源合集文件
5. `original_comment.md`：部分书源完整注释内容（文件位于`/old_ver`目录下）

## 使用说明

1. 使用这些源时不需要额外的净化规则
2. `真白萌`、`轻小说文库(.cc)`、`轻小说文库(.net)`和`有度轻小说`登录后方可正常使用
3. 部分源搜索存在问题，建议前往原网站找到所需阅读书籍的网址后，使用阅读APP主页面右上角菜单⠇内的`添加网址`功能导入书籍
4. 由于该项目处在非维护周期内，不保证书源的有效性
4. 日语原版轻小说书源文件的说明请见：[日本Web小说 Book Source](https://github.com/ZWolken/Light-Novel-Yuedu-Source/releases/tag/JA)
5. 详细原使用说明请见：[原README文件](/old_ver/README.md)

## 导入方法

### 书源导入

1. 访问[Release发行版](https://github.com/ZWolken/Light-Novel-Yuedu-Source/releases)，复制所需书源/书源合集的JSON文件的链接或者下载对应的文件
2. 打开阅读APP
3. 我的
4. 书源管理
5. 右上角菜单⠇
6. 网络导入/本地导入
7. 复制链接/选择文件
8. 确认

### 订阅源导入（测试）

> 使用规则订阅可便于更新书源

1. 于下方表格复制对应订阅源的链接
2. 打开阅读APP
3. 订阅
4. 规则订阅
5. 右上角添加+
6. 类型选择`书源`，填写任意名称，于`Url`框内粘贴链接
7. 确认

| 订阅源 | 链接 |
| ---: | :--- |
| [日轻小说](https://github.com/ZWolken/Light-Novel-Yuedu-Source/releases/latest/download/Japan_based_bookSource.json) | `https://github.com/ZWolken/Light-Novel-Yuedu-Source/releases/latest/download/Japan_based_bookSource.json` |
| [国轻小说](https://github.com/ZWolken/Light-Novel-Yuedu-Source/releases/latest/download/China_based_bookSource.json) | `https://github.com/ZWolken/Light-Novel-Yuedu-Source/releases/latest/download/China_based_bookSource.json` |
| [日语原版轻小说](https://github.com/ZWolken/Light-Novel-Yuedu-Source/releases/latest/download/Japanese_original_bookSource.json) | `https://github.com/ZWolken/Light-Novel-Yuedu-Source/releases/latest/download/Japanese_original_bookSource.json` |
| [所有书源](https://github.com/ZWolken/Light-Novel-Yuedu-Source/releases/latest/download/All_bookSource.json) | `https://github.com/ZWolken/Light-Novel-Yuedu-Source/releases/latest/download/All_bookSource.json` |

> [!TIP]
> 可以直接订阅所有书源，仅打开对应分组即可

## 登录方法

1. 发现页、管理书源、编辑书源三处菜单的“登录”均可使用
2. 登录完成后，点击右上方的√，保存返回后即可正常使用。

## 贡献者

<a href="https://github.com/ZWolken/Light-Novel-Yuedu-Source/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ZWolken/Light-Novel-Yuedu-Source"  alt="Light-Novel-Yuedu-Source Contributors"/>
</a>

## 备注

1. `哔哩轻小说`原始源缝合了源仓库里**叶落岚起+关耳/乃星**改的灰色章节可阅的规则脚本，后续又由**酷安@吉王义昊**以及**柚屿☆**等多位进行多次修正维护，但由于原网站使用了各种防爬措施以及字体混淆等，基本无法长期正常使用。
2. `动漫之家`的轻小说站如有需要可使用[动漫之家Flutter客户端](https://github.com/xiaoyaocz/dmzj_flutter)
3. （2022年前）`轻之国度(LK)`维护完毕后网站有所改动，先前的源全部失效，由[酷安@转义字符](http://www.coolapk.com/u/2060038) 以及 [酷安@金01461](http://www.coolapk.com/u/1208939)重新写了源，新源可正常使用
4. `ESJ`的源来自[酷安@户山香澄Official](http://www.coolapk.com/u/614507)的[帖子](https://www.coolapk.com/feed/33474742)并做了更新，详细使用说明请看[另一原帖](https://www.coolapk.com/feed/32715700)，发现若需正常使用请科学后登录
5. 本仓库内书源的发现使用了[酷安@关耳010225](http://www.coolapk.com/u/2379204)提供的方法进行了美化，大部分源的发现均有进行增加
6. 内容来源于酷安评论区、源仓库，未发帖公开的源均已得到原作者许可公开，~~并且筛选、修复解析和发现保证使用有效~~ 由于该项目处在非维护周期内，不保证书源的有效性
