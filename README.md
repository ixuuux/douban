# Douban Book TOP250

TOP250 榜单是如何产生的？
> 豆瓣用户每天都在对“读过”的书进行“很差”到“力荐”的评价，豆瓣根据每本书读过的人数以及该书所得的评价等综合数据，通过算法分析产生了豆瓣图书前250名。

- 分析目标站点

站点：https://book.douban.com/top250?start=0  极易抓取，数据量也不大，几秒就可以跑完，start=0代表页数，起到了翻页的作用，以25为递增，榜单共10页，所以最后一页是start=225

使用for循环可以很方便的构造出10页的网址
