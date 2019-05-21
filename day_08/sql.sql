use mydb;

select *
from mytable;

-- 테이블 내부의 데이터 수정을 위한 update 절
-- update 테이블명
-- set 수정할컬럼명1 = 수정할값1 [수정할컬럼명N = 수정할값N]
-- where 조건식(특정 컬럼명에 대한 조건식)
update mytable
set age = 0
where id = 2;

select *
from mytable;

update mytable
set age = age + 1;

-- 테이블의 레코드를 삭제할 수 있는 delete 절
-- (테이블 자체를 삭제하는 것이 아닌 레코드만 삭제)
-- delete from 테이블명
-- where 조건식
delete from mytable
where id > 10;





