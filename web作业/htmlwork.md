1,简答什么是html语义化

HTML结构是用相对应的有一定语义的英文字母（标签）表示的，标记的，因为HTML本身就是标记语言。不仅对自己来说，容易阅读，书写。别人看你的代码和结构也容易理解，甚至对一些不是做网页开发的人来说，也容易阅读。

2,html标签和元素的区别

标签就是用来标记HTML元素的。位于起始标签和结束标签之间的文本就是HTML元素的内容

3,简答浏览器获取网页的完整大体流程

1,接收html代码，并处理html标签并构建DOM树

2，处理CSS标记并构建cssom树

3，将DOM,CSSOM合并成渲染树

4，根据渲染树来布局，并计算每个节点的信息

5，将各个节点绘制在屏幕上

4,html css js的区别和功能是什么？

HTML是超文本标记语言，文本中包含了所谓的“链接点”HTML利用超链接的方法，将各种不同空间的文字信息组织在一起的网状文本。

CSS是层叠样式表单。是将样式信息与网页内容分离的一种标记语言。我们在牛腩新闻发布系统中，我们使用过CSS文件，对一些标签的样式进行修改

Javascript是一种基于对象(Object)和事件驱动(Event Driven)并具有安全性能的脚本语言。使用它的目的是与HTML超文本标记语言、Java脚本语言(Java小程序)一起实现在一个Web页面中链接多个对象，与Web客户交互作用。

5,标记语言是什么意思?请再写出两种编辑语言并说明他们的用途

标记语言，是一种将文本以及文本相关的其他信息结合起来，展现出关于文档结构和数据处理细节的电脑文字编码

SGML（Standard Generalized Markup Language，标准通用标记语言）

XML（eXtensible Markup Language，可扩展的标记语言）具备了SGML的核心特性，又非常的简洁

6,h5播放器和 flash播放器的有什么不同点

flash必须要flash播放器或容器，所以要看flash的东西要装浏览器插件否则看不了。

html5就是html的新标准也就是网页的基本，所有设备都可以观看，不封闭可以随意调用

7,如何区分 HTML 和 HTML5

1、在文档类型声明上

HTML声明：

　　<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
　　<html xmlns="http://www.w3.org/1999/xhtml">
　　

HTML5声明：

<!doctype html>
　　上面的两种声明,HTML5声明简洁方便人们的记忆，HTML声明太长了并且很难记住这段代码。

　　
2、在结构语义上

　　HTML:没有体现结构语义化的标签，通常都是这样来命名的<div id="header"></div>，这样表示网站的头部。
　　
　　HTML5:在语义上却有很大的优势，提供了一些新的HTML5标签比如: article、footer、header、nav、section，这些通俗易懂。

























