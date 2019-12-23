-- 查询所有学生的信息
select * from tb_student;

-- 查询所有课程名称和学分(投影和别名)
select couname, credit from tb_cource;
-- 加上别名
select couname as 课程名字, credit as 学分 from tb_cource;

-- 查询所有学生的的姓名和性别(条件运算)
select stuname as 姓名, case sex when 1 then '男' else '女' end as 性别 from tb_student;
select stuname as 姓名, if(sex, '男','女') as 性别 from tb_student;

-- 查询所有女学生的出生日期和姓名(筛选)
select stuname, birth from tb_student where sex=0;

-- 查询所有80后学生的姓名，性别和出生日期(姓名)
select stuname, if(sex, '男', '女'), birth from tb_student where birth>='1980-1-1' and birth<='1989-12-31';
select stuname, if(sex, '男', '女'), birth from tb_student where birth between '1980-1-1' and '1989-12-31';

-- 查询所有姓杨的学生姓名和出生日期(模糊)
-- %匹配任意个字
select stuname, birth from tb_student where stuname like '杨%';

-- 查询姓杨的名字的两个字的同学
-- _匹配一个字
select stuname, birth from tb_student where stuname like '杨_';

-- 查询姓杨且名字为3个字的同学(模糊)
select stuname, birth from tb_student where stuname like '杨__';

-- 查询名字中有"不"字或"嫣"字的学生的姓名(模糊)
select stuname, birth from tb_student where stuname like '%不%' or stuname like '%嫣%';

-- 查询没有录入家庭住址的学生(空值)
-- is用来和数据结构的相同， is null 意义为null ，= null 意义为字符串的值就是null
select stuname, sex, birth, collid from tb_student where addr is null;

-- 查询录入了家庭住址的学生(空值)
select stuname, sex, birth, collid from tb_student where addr is not null;

-- 查询学生选课的所有日期(去重)
select distinct seldate from tb_record;

-- 查询学生的家庭住址(去重)
select distinct addr from tb_student where addr is not null;

-- 查询男学生的姓名和生日，按照年龄大小排序(排序)
-- datediff 返回两个日期的时间
-- curdate 返回当前时间
-- div 除以
-- desc 表示降序
-- asc 表示升序
select stuname as 姓名, datediff(curdate(), birth) div 365 as 年龄 from tb_student where sex=1 order by 年龄 desc;

-- 查询年龄最大的学生的出生日期(聚合函数)
select min(birth) from tb_student;

-- 查询年龄最小的学生的出生日期(聚合函数)
select max(birth) from tb_student;
select max(birth), sex from tb_student group by sex;

-- 查询男女学生的人数(分组和聚合函数)
select if(sex, '男', '女') as 性别, count(*) from tb_student group by sex;

-- 查询课程id为1111的平均成绩(筛选加聚合函数)
select avg(score) from tb_record where cid=1111;

-- 列出每一节课的平均分
select avg(score),cid from tb_record where score is not null group by cid;

-- 查询学号为1001的学生的所有课程的评分(筛选加聚合))
select avg(score) from tb_record where sid=1001;

--查询所有学生的平均分
select avg(score) as 平均分, sid from tb_record group by sid order by 平均分 desc;

-- 查询平均成绩大于等于90分的学生的学号和平均成绩
-- 分组以前的筛选使用where子句 / 分组以后的筛选使用having子句
select sid as 学号, avg(score) as 平均分 from tb_record group by sid having 平均分>=90;

-- 查询年龄最大的学生的姓名(子查询/嵌套的查询)
select stuname, birth from tb_student where birth=(select min(birth) from tb_student);

-- 查询年龄最大的学生的年龄和姓(子查询和运算)
select stuname as 姓名, datediff(curdate(), birth) div 365 as 年龄 from tb_student where birth=(select min(birth) from tb_student);

-- 查询选择了两门课以上的学生(子查询，分组条件，集合运算)
-- 首先是从tb_record那里选择出sid>2（选择了两门）的学生id
select sid from tb_record group by sid having count(sid)>2;

-- 然后通过判断sid是否在上面的结果中，以选出所有符合的学生
-- in 表示是否在某个表中
select * from tb_student where stuid in (select sid from tb_record group by sid having count(sid)>2);

-- 使用in的例子：
-- 找出棉铃最小的男生和女生，并且显示他们的所有信息
select * from tb_student where birth in (select max(birth) from tb_student group by sex);

-- 查询学生姓名，课程名称，分数（多表查询  即笛卡尔查询）
select stuname, couname, score from tb_student, tb_cource, tb_record where stuid=sid and couid=cid and score is not null;

-- 查询学生姓名、课程名称以及成绩按成绩从高到低查询第11-15条记录(内连接+分页)
select stuname as sn, 
    couname as cn,
    score 
    from tb_student as ts
    inner join tb_record as tr on ts.stuid=tr.sid 
    inner join tb_cource as tc on tr.cid=tc.couid
    where score is not null
    order by score desc 
    limit 5 offset 10; -- 指定翻页

select stuname as sn,
    couname as cn,
    score
    from tb_student as ts
    inner join tb_record as tr on ts.stuid = tr.sid
    inner join tb_cource as tc on tr.cid=tc.couid
    where score > 60
    order by score desc
    limit 5, 10;

-- 查询选课学生的姓名和平均成绩(子查询和连接查询)
-- 使用多表查询
select stuname as 姓名,
    avgscore as 平均分
    from tb_student as ts, 
    (select avg(score) as avgscore, sid  from tb_record group by sid) as scoretable 
    where scoretable.sid=ts.stuid
    order by 平均分 desc;

-- 使用内联查询
select stuname as 姓名,
    avgscore as 平均分
    from tb_student as ts
    inner join (select avg(score) as avgscore, sid from tb_record group by sid) as avgresult
    where ts.stuid = avgresult.sid
    order by avgscore desc;

-- 内联查询方法
-- 先确定主表，仍然使用FROM <表1>的语法；
-- 再确定需要连接的表，使用INNER JOIN <表2>的语法；
-- 然后确定连接条件，使用ON <条件...>，这里的条件是s.class_id = c.id，表示students表的class_id列与classes表的id列相同的行需要连接；
-- 可选：加上WHERE子句、ORDER BY等子句

-- 查询每个学生的姓名和选课数量
-- 以下是思路：
-- 1.我们先写出：所有学生的选课数量
select count(*), sid from tb_record group by sid;
-- 2.再把上面的表和学生的表连接一起
-- 用内连接合的话，会把没有选课的学生忽略掉
select ts.stuname, ccount from tb_student as ts inner join 
    (select count(*) as ccount, sid from tb_record group by sid) as counts
    on ts.stuid = counts.sid;

-- 如果用外连接，就不会有这样的问题
select ts.stuname, ifnull(ccount, 0) as 选课数量 from tb_student as ts left join 
    (select count(*) as ccount, sid from tb_record group by sid) as counts
    on ts.stuid = counts.sid;

