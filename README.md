# Vue News Board
本项目参考了 [react-news-board](https://github.com/ethan-funny/react-news-board)。正好这段时间学习Vue.js，仿照着用Vue写了一个。

采用的技术栈：

* Flask 后台提供api
* Vue + Vuex 前端数据展示
* sqlite 用于储存数据


## 不同之处

如上面所说，本项目参考自 [react-news-board](https://github.com/ethan-funny/react-news-board)。在此基础上做了一些改动：

* 原项目采用实时爬取新闻放到前端展示，这样的效率不高，而且当用户量达到一定程度时，后端同时发出的请求太多，可能会被新闻源网站封IP。本项目采用定时更新新闻，并保存到数据库中，用户需要阅读新闻时从数据库中取。
* 原项目对移动端页面不太友好，苦于自己也是个前端苦手，所以，也只能力所能及地优化移动端页面。

## 后端
采用`flask-restful`提供api接口
目录结构如下：
```
➜  Vue_News_Board git:(master) tree ./server 
./server
├── api.py
├── app.py
├── config.py
├── __init__.py
├── spider
│   ├── ......
├── static
│   ├── ......
└── templates
    └── index.html
```
## 爬虫

爬虫代码放在spider目录下，目录结构如下：
```
➜  server git:(master) tree ./spider 
./spider
├── base.py
├── bobao_news.py
├── freebuf_news.py
├── hacker_news.py
├── __init__.py
├── jobbole_news.py
├── manage.py
├── models.py
└── news.db
```
运行`python manage.py` 即可开始爬取新闻并保存到`new.db`。

服务器上使用`crontab`来执行定时任务，每天8:00、12:00、16:00、20:00更新新闻。

## 前端

使用`vue-cli` Vue的脚手架编写，主要代码在`client/vue_news/src`下面。

##  效果
![PC端页面](https://ooo.0o0.ooo/2017/01/09/58733973caa5b.png)
![移动端页面](https://ooo.0o0.ooo/2017/01/09/58733972e8388.png)

## TODO
* 前端直接点击更新新闻
* 优化页面样式
* 添加更多新闻源
* ......


