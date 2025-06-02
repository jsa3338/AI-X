-- [II] SELECT 문 - 조회 /* 여러줄 주석 */ 
-- 1. SELECT 문 작성법
SHOW USER;
    -- 현재 계정(실행 : CTRL + ENTER)
SELECT * FROM TAB; -- 현 계정이 가지고 있는 테이블들
SELECT * FROM EMP; -- EMP테이블의 모든 열, 모든 행 출력
SELECT * FROM DEPT; -- DEPT테이블의 모든 열, 모든 행 출력
SELECT * FROM SALGRADE;

-- 2. 특정열만 출력
DESC EMP;
    -- EMP 테이블 구조를 나타내는 오라클 명령어
SELECT EMPNO, ENAME, SAL, JOB FROM EMP;  -- EMPNO, ENAME, SAL, JOB 열의 모든 행 출력
SELECT EMPNO AS "사 번", ENAME AS "이름", SAL AS "급여", JOB AS "직책" FROM EMP;   -- AS = alias 의 약자
SELECT EMPNO  "사 번", ENAME  "이름", SAL  급여, JOB  "직책" FROM EMP;   -- " " 생략가능, 단 사번처럼 스페이스가 들어가려면 "" 필요
SELECT EMPNO NO, ENAME ENAME, SAL SALARY FROM EMP;

-- 3. 특정행만 출력 : WHERE절(조건절) 
-- 비교연산자 : 같다(=), 다르다(!=, ^=, <>), >, >=, <, <=
SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL = 3000;
SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL < 3000;
SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL ^= 3000;
SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL <> 3000;
SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL != 3000;
    -- 비교연산자는 숫자말고 문자, 날짜형 모두 가능
    -- EX1) 사원이름(ENAME)이 'A', 'B', 'C'로 시작하는 사원의 모든 필드
    -- 'A' < 'AA' < 'AAA' < 'AAAA' < 'B' < 'C' < 'D'
SELECT * FROM EMP WHERE ENAME < 'D';
    -- EX2) 82년도 이전에 입사한 사원의 모든 필드
SELECT * FROM EMP WHERE HIREDATE < '82/01/01';
    -- EX3) 부서번호(DEPTNO)가 10번인 사원의 모든 필드
SELECT * FROM EMP WHERE DEPTNO =10;
    -- EX4) 이름(ENAME)이 FORD 인 직원의 EMPNO, ENAME, MGR(상사의 사번)을 출력
SELECT EMPNO, ENAME, MGR 
    FROM EMP 
    WHERE ENAME='FORD';
    -- SQL문은 대소문자 구별 없음
select empno, ename, mgr from emp where ename='FORD'; -- 단 데이터는 대소문자 구별 있음
-- (X) select empno, ename, mgr from emp where ename='ford';

-- 4. 특정행 출력 : WHERE(조건절)  
-- 논리연산자 - AND, OR, NOT
    --EX1. 급여(SAL)가 2000 이상 3000이하인 직원의 모든 필드
SELECT * 
    FROM EMP
    WHERE SAL >= 2000 AND SAL <= 3000;
    -- EX2. 82년에도 입사한 사원의 모든 필드
SELECT * 
    FROM EMP
    WHERE HIREDATE >= '82/01/01' AND HIREDATE <= '82/12/31';
    
    -- 날짜 표기법 세팅(현재 : YY/MM/DD or RR/MM/DD)
ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD'; 
    -- 날짜 세팅을 고려한 82년도 사원의 모든 필드
SELECT *
    FROM EMP
    WHERE TO_CHAR(HIREDATE, 'YY/MM/DD') >= '82/01/01' AND 
        TO_CHAR(HIREDATE, 'YY/MM/DD') <= '82/12/31';
        -- 날짜 표기 원복
ALTER SESSION SET NLS_DATE_FORMAT = 'RR/MM/DD'; 

    --EX3. 연봉이 2400 이상인 직원의 ENAME, SAL, 연봉(SAL*12)를 출력
    -- (1) - (2) - (3) 순서대로 읽는다
SELECT ENAME, SAL, SAL*12 ANNUALSAL  -- (3)
    FROM EMP                     -- (1)
    WHERE SAL*12>=2400;     -- (2) WHERE 절에는 필드의 별칭 사용 불가

    -- EX4. 연봉이 3000이상인 직원의 ENAME, SAL, 연봉을 연봉순으로 출력
SELECT ENAME, SAL, SAL*12 ANNUALSAL  -- (3)
    FROM EMP                      -- (1)
    WHERE SAL*12>=3000       -- (2)
    ORDER BY ANNUALSAL;     -- (4) ORDER BY 절에는 필드의 별칭 사용 가능
    -- EX5. JOB이 MANAGER이거나 10번부서(DEPTNO)외의 직원 모든 필드
    SELECT * FROM EMP
        WHERE JOB='MANAGER' OR DEPTNO !=10;

-- 5. 산술연산자(SELECT 절, 조건절, ORDER BY 절)
    -- 모든 사원의 10% 인상된 월급과 사번(EMPNO), 이름(ENAME)을 출력
    SELECT EMPNO, ENAME, SAL*1.1 FROM EMP;
    -- 모든 사원의 이름(ENAME), 월급(SAL), 상여(COMM), 연봉(SAL*12+COMM)
    SELECT ENAME, SAL, COMM, (SAL*12)+COMM ANNUALSAL FROM EMP;
     -- 산술연산의 결과는 NULL을 포함하면 결과도 NULL이 된다
     -- NVL(NULL일수 있는 필드명, NULL이면 대체할 값) - 단 두 매개변수의 데이터 타입이 일치해야함
    SELECT ENAME, SAL, COMM, (SAL*12)+NVL(COMM, 0) ANNUALSAL FROM EMP;
    -- 모든 사원의 사번, 이름 상사사번(상사의 사번이 없는 직원은 'CEO'로 출력
    SELECT EMPNO, ENAME, NVL(MGR, 'CEO') FROM EMP;
    SELECT EMPNO, ENAME, NVL(TO_CHAR(MGR), 'CEO') FROM EMP;

-- 6. 연결연산자(||) : 필드 값이나 문자를 연결
SELECT ENAME || ' is a ' || JOB EMPLOYEE FROM EMP;

-- 7. 중복제거(DISTINCT)
SELECT DISTINCT JOB FROM EMP;
SELECT DISTINCT DEPTNO FROM EMP;

-- 연습문제 꼭 풀기
--1. emp 테이블의 구조 출력
    DESC EMP;
--2. emp 테이블의 모든 내용을 출력 
    SELECT * FROM EMP;
--3. 현 scott 계정에서 사용가능한 테이블 출력
    SELECT * FROM TAB;
--4. emp 테이블에서 사번, 이름, 급여, 업무, 입사일 출력
    SELECT EMPNO, ENAME, SAL, JOB, HIREDATE FROM EMP;
--5. emp 테이블에서 급여가 2000미만인 사람의 사번, 이름, 급여 출력
    SELECT EMPNO, ENAME, SAL 
        FROM EMP
        WHERE SAL <2000;
--6. 입사일이 81/02이후에 입사한 사람의 사번, 이름, 업무, 입사일 출력
    SELECT EMPNO, ENAME, JOB, HIREDATE
        FROM EMP
        WHERE TO_CHAR(hiredate, 'YY/MM/DD') >= '81/02/01';
--7. 업무가 SALESMAN인 사람들 모든 자료 출력
    SELECT *
        FROM EMP
        WHERE JOB = 'SALESMAN';
--8. 업무가 CLERK이 아닌 사람들 모든 자료 출력
    SELECT *
        FROM EMP
        WHERE JOB ^= 'CLERK';
--9. 급여가 1500이상이고 3000이하인 사람의 사번, 이름, 급여 출력
    SELECT EMPNO, ENAME, SAL
        FROM EMP
        -- WHERE SAL >=1500 AND SAL <=3000;
        WHERE SAL BETWEEN 1500 AND 3000;
--10. 부서코드가 10번이거나 30인 사람의 사번, 이름, 업무, 부서코드 출력
    SELECT EMPNO, ENAME, JOB, DEPTNO 
        FROM EMP
        -- WHERE DEPTNO=10 OR deptno=30;
        WHERE DEPTNO IN (10, 30);
--11. 업무가 SALESMAN이거나 급여가 3000이상인 사람의 사번, 이름, 업무, 부서코드 출력
    SELECT EMPNO, ENAME, JOB, DEPTNO
        FROM EMP
        WHERE JOB = 'SALESMAN' OR SAL >= 3000;
--12. 급여가 2500이상이고 업무가 MANAGER인 사람의 사번, 이름, 업무, 급여 출력
    SELECT EMPNO, ENAME, JOB, SAL
        FROM EMP
        WHERE SAL >= 2500 AND JOB = 'MANAGER';
--13.“ename은 XXX 업무이고 연봉은 XX다” 스타일로 모두 출력(연봉은 SAL*12+COMM)
    SELECT ENAME || '은 ' || JOB || ' 업무이고 연봉은 ' || (SAL*12+NVL(COMM, 0)) || '다' "EMPLOYEES"
        FROM EMP;
        
-- ※ 연습문제 끝

-- 8. SQL 연산자(BETWEEN, IN, LIKE, IN NULL)
    -- (1) BETWEEN A AND B : A부터 B까지(A,B 포함)
        -- EX1. SAL 1500이상 3000이하인 직원의 사번 이름 급여
        SELECT EMPNO, ENAME, SAL
            FROM EMP
            -- WHERE SAL >=1500 AND SAL <=3000;
            WHERE SAL BETWEEN 1500 AND 3000;
        -- EX2. SAL이 1500 미만, 3000천 초과 
        SELECT EMPNO, ENAME, SAL
            FROM EMP
            WHERE  SAL NOT BETWEEN 1500 AND 3000;
        -- EX3. 이름이 'A', 'B', 'C'로 시작하는 직원의 모든 필드
        SELECT * 
            FROM EMP 
            WHERE ENAME BETWEEN 'A' AND 'D' AND ENAME !='D';
        -- EX4. 82년도에 입사한 직원의 모든 필드
        SELECT *
            FROM EMP
            WHERE TO_CHAR(HIREDATE, 'RR/MM/DD') BETWEEN '82/01/01' AND '82/12/31';
    
    -- (2) 필드명 IN (값1, 값2, .., 값N)
        -- EX1.  부서번호(DEPTNO)가 10, 30, 40 인 직원의 사번, 이름   
        SELECT EMPNO, ENAME, JOB, DEPTNO 
            FROM EMP
            -- WHERE DEPTNO=10 OR deptno=30 OR deptno=40;
            WHERE DEPTNO IN (10, 30, 40);
            -- WHERE DEPTNO NOT IN (10, 30, 40);
        -- EX2. 직책(JOB)이 MANAGER OR ANALYST인 사원의 모든 필드
        SELECT *
            FROM EMP
            WHERE JOB IN ('MANAGER', 'ANALYST');

    -- (3) 필드명 LIKE 패턴 : %(0글자 이상), _(1글자)를 포함한 패턴
        --EX1. 이름이 'M'으로 시작하는 사원의 모든필드
        SELECT *
            FROM EMP
            WHERE ENAME LIKE 'M%';
        -- EX2. 이름에 N이 들어가거나 JOB에 N이 들어가는 직원의 모든 필드
        SELECT *
            FROM EMP
            WHERE ENAME LIKE '%N%' OR JOB LIKE '%N%';
        -- EX3. 급여가 5로 끝나는 사원의 모든 필드
        SELECT *
            FROM EMP
            WHERE SAL LIKE '%5';
        -- EX4. 입사일이 82년도로 시작하는 사원의 모든 필드
        SELECT *
            FROM EMP
            WHERE TO_CHAR(HIREDATE, 'YY/MM/DD') LIKE '81%';
        -- EX5. 1월에 입사한 사원의 모든 필드
        SELECT *
            FROM EMP
            WHERE TO_CHAR(HIREDATE, 'YY/MM/DD') LIKE '__/01/__';
            
    -- (4) 필드명 IS NULL (해당 필드가 NULL인지 여부, TRUE/FALSE 반환)
        -- EX1. 상여금을 받지 않는 사원의 모든 필드 출력
        SELECT * FROM EMP
            WHERE COMM =0 OR COMM IS NULL;
        -- EX1. 상여금을 받는 사원의 모든 필드 출력
        SELECT * FROM EMP
            -- WHERE NOT COMM IS  NULL AND NOT COMM =0 ;
            WHERE COMM IS NOT NULL AND COMM !=0 ;

-- 9. 정렬(오름차순, 내림차순) : ORDER BY절
SELECT * 
    FROM EMP 
    ORDER BY SAL;           -- SAL 기준 오름차순 정렬
SELECT *
    FROM EMP
    ORDER BY SAL, COMM; -- SAL 기준 오름차순 정렬(SAL이 같으면 COMM 기준 오름차순)
SELECT * 
    FROM EMP 
    ORDER BY SAL DESC; -- SAL기준 내림차순 정렬  
SELECT *
    FROM EMP
    ORDER BY SAL DESC , HIREDATE DESC;   -- SAL 기준 내림차순 정렬(SAL이 같으면 HIREDATE 기준 내림차순)         
    
-- 연습문제 전 형변환 함수 : TO_CHAR, TO_DATE
-- ※ 날짜형(HIREDATE)을 문자형으로 변환 : TO_CHAR(날짜형데이터, 패턴)
    -- YY, YYYY, RR: 년도 / MM : 월 / DD : 일  / DY 월 / DAY 월요일
    -- HH24, HH12, HH : 시 / AM이나 PM / MI 분 / SS초
    SELECT ENAME, TO_CHAR(HIREDATE, 'YY/MM/DD HH24:MI:SS') FROM EMP;
    -- 82년 전에 입사한 사원의 데이터
    SELECT * FROM EMP WHERE TO_CHAR(HIREDATE, 'RR/MM/DD') < '82/01/01';
    SELECT * FROM EMP WHERE HIREDATE < TO_DATE('82/01/01', 'RR/MM/DD');


-- <총 연습문제>
--1.	EMP 테이블에서 sal이 3000이상인 사원의 empno, ename, job, sal을 출력
SELECT EMPNO, ENAME, JOB, SAL
    FROM EMP
    WHERE SAL >=3000;
--2.	EMP 테이블에서 empno가 7788인 사원의 ename과 deptno를 출력
SELECT ENAME, DEPTNO
    FROM EMP
    WHERE EMPNO = 7788;
--3.	연봉(SAL*12+COMM)이 24000이상인 사번, 이름, 급여 출력 (급여순정렬)
SELECT EMPNO, ENAME, SAL
    FROM EMP
    WHERE SAL*12+NVL(COMM,0) >= 24000
    ORDER BY SAL;
--4.	입사일이 1981년 2월 20과 1981년 5월 1일 사이에 입사한 사원의 사원명, 직책, 입사일을 출력 (단 hiredate 순으로 출력)
SELECT ENAME, JOB, HIREDATE
    FROM EMP
    WHERE TO_CHAR(HIREDATE, 'RR/MM/DD') BETWEEN '81/02/20' AND '81/05/01'
    ORDER BY HIREDATE;
--5.	deptno가 10,20인 사원의 모든 정보를 출력 (단 ename순으로 정렬)
SELECT *
    FROM EMP
    WHERE DEPTNO IN (10, 20)
    ORDER BY ENAME;
--6.	sal이 1500이상이고 deptno가 10,30인 사원의 ename과 sal를 출력
-- (단 출력되는 결과의 타이틀을 employee과 Monthly Salary로 출력)
SELECT ENAME EMPLOYEE, SAL "Monthly Salary"
    FROM EMP
    WHERE SAL >=1500 AND DEPTNO IN (10,30);

--7.	hiredate가 1982년인 사원의 모든 정보를 출력
SELECT *
    FROM EMP
    WHERE HIREDATE LIKE '82%';

--8.	이름의 첫자가 C부터  P로 시작하는 사람의 이름, 급여 이름순 정렬
SELECT  ENAME, SAL
    FROM EMP
    WHERE ENAME BETWEEN 'C' AND 'Q' AND ENAME != 'Q'
    ORDER BY ENAME, SAL;
    
--9.	comm이 sal보다 10%가 많은 모든 사원에 대하여 이름, 급여, 상여금을 
--출력하는 SELECT 문을 작성
SELECT ENAME, SAL, COMM
    FROM EMP
    WHERE COMM>=SAL*1.1;
    
--10.	job이 CLERK이거나 ANALYST이고 sal이 1000,3000,5000이 아닌 모든 사원의 정보를 출력
SELECT *
    FROM EMP
    WHERE JOB IN ('CLERK', 'ANALYST') AND SAL NOT IN (1000, 3000, 5000);
--11.	ename에 L이 두 자가 있고 deptno가 30이거나 또는 mgr이 7782인 사원의 
--모든 정보를 출력하는 SELECT 문을 작성하여라.
SELECT *
    FROM EMP
    WHERE ENAME LIKE '%L%L%' AND DEPTNO=30 OR MGR=7782;

--12.	입사일이 81년도인 직원의 사번, 사원명, 입사일, 업무, 급여를 출력
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL
    FROM EMP
    WHERE HIREDATE LIKE '81%';
--13.	입사일이81년이고 업무가 'SALESMAN'이 아닌 직원의 사번, 사원명, 입사일, 
-- 업무, 급여를 검색하시오.
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL
    FROM EMP
    -- WHERE HIREDATE LIKE '81%' 
    WHERE TO_CHAR(HIREDATE, 'RR') = '81' 
        AND JOB!='SALESMAN';
    
--14.	사번, 사원명, 입사일, 업무, 급여를 급여가 높은 순으로 정렬하고, 
-- 급여가 같으면 입사일이 빠른 사원으로 정렬하시오.
SELECT EMPNO, ENAME, HIREDATE, JOB, SAL
    FROM EMP
    ORDER BY SAL DESC, HIREDATE;

--15.	사원명의 세 번째 알파벳이 'N'인 사원의 사번, 사원명을 검색하시오
SELECT EMPNO, ENAME 
    FROM EMP
    WHERE ENAME LIKE '__N%';
--16.	사원명에 'A'가 들어간 사원의 사번, 사원명을 출력
SELECT EMPNO, ENAME 
    FROM EMP
    WHERE ENAME LIKE '%A%';
--17.	연봉(SAL*12)이 35000 이상인 사번, 사원명, 연봉을 검색 하시오.
SELECT EMPNO 사번, ENAME 사원명, SAL*12 연봉
    FROM EMP
    WHERE SAL*12>=35000;
    
    
    
    