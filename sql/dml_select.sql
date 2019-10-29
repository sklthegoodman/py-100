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