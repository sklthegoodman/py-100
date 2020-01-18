-- 创建索引

-- 在学生名字那里创建索引
create index inx_student_name on tb_student(stuname);
-- 解释
explain select * from tb_student where stuname='猪儒'\G

--删除索引
alter table tb_student drop index inx_student_name
--另一个写法
drop index inx_student_name on tb_student