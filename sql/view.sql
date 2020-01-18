-- 创建视图
create view vm_score 
as
select sid, round(avg(score), 1) as avgscore from tb_record group by sid;

create view vm_student_score
as 
select stuname, avgscore from tb_student, vm_score where stuid=sid;

-- 使用视图
select * from vm_student_score;

-- 删除视图
drop vm_student_score