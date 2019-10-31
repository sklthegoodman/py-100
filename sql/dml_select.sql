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
select stuname, birth from tb_student where stuname like '杨%';

-- 查询姓杨的名字的两个字的同学
select stuname, birth from tb_student where stuname like '杨_';

-- 查询姓杨且名字为3个字的同学(模糊)
select stuname, birth from tb_student where stuname like '杨__';

-- 查询名字中有"不"字或"嫣"字的学生的姓名(模糊)
select stuname, birth from tb_student where stuname like '%不%' or stuname like '%嫣%';

-- 查询没有录入家庭住址的学生(空值)
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