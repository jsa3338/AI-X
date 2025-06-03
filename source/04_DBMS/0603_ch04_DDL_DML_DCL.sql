-- [IV] DDL, DCL, DML 
/* SQL
 - DCL 
    사용자 계정생성 CREATE USER, 권한부여 GRANT, 권한박탈 REVOKE, 사용자 계정삭제 DROP USER
    트랜젝션 명령어
 - DDL
    테이블 생성 CREATE TABLE , 테이블 삭제 DROP TABLE 
    테이블 구조변경 ALTER TABLE
 - DML
    데이터 삽입 INSERT, 조회 SELECT, 수정 UPDATE, 삭제 DELETE
*/
--------------------------
-------- ★ DDL ★ --------
--------------------------
-- 1. 테이블 생성(CREATE TABLE 테이블명) : 테이블 구조를 정의
CREATE TABLE BOOK(
    BOOKID NUMBER(4),  -- BOOKID 라는 필드에 숫자 4자리
    BOOKNAME VARCHAR2(20), -- BOOKNAME 필드의 타입은 문자 20BYTE
    PUBLISHER VARCHAR2(20),
    RDATE   DATE,           -- RDATE 필드의 타입은 DATE형
    PRICE    NUMBER(8,2),  -- PRICE 필드의 타입은 숫자 전체 자리 8자리 중 소숫점 2자리    
    PRIMARY KEY(BOOKID)  -- 프라이머리키 제약조건을 선언 (NOT NULL, UNIQUE)
    );
SELECT * FROM BOOK;
DESC BOOK;

DROP TABLE BOOK;  -- 2. 테이블 삭제

CREATE TABLE BOOK(   
    BID NUMBER(4) PRIMARY KEY,
    BNAME VARCHAR2(20),
    PUBLISHER VARCHAR2(20),
    RDATE DATE,
    PRICE NUMBER(8)
);

-- EX. DEPT01 테이블 만들기
CREATE TABLE DEPT01(
    DEPTNO NUMBER(2) PRIMARY KEY,
    DNAME VARCHAR2(14),
    LOC VARCHAR2(13)
    );
    
SELECT * FROM DEPT01;

SELECT * FROM DEPT;  -- 10, 20, 30, 40

SELECT DISTINCT DEPTNO FROM EMP; -- 10, 20, 30
DESC EMP;

INSERT INTO EMP (EMPNO, ENAME, DEPTNO) VALUES (9999, 'JINS', 40);
INSERT INTO EMP (EMPNO, ENAME, DEPTNO) VALUES (8888, 'HONG', 50);
SELECT * FROM EMP;
ROLLBACK; -- DML 취소 트랜젝션 명령어
SELECT * FROM EMP;
SELECT * FROM DEPT01;
CREATE TABLE EMP01(
    EMPNO NUMBER(4) PRIMARY KEY,
    ENAME VARCHAR2(10),
    SAL NUMBER(7,2),
    DEPTNO NUMBER(2) REFERENCES DEPT01(DEPTNO)  -- FK 제약조건
);

DESC EMP01;
DROP TABLE EMP01;
DROP TABLE DEPT01;

CREATE TABLE EMP01(
    EMPNO NUMBER(4),
    ENAME VARCHAR2(10),
    SAL NUMBER(7,2),
    DEPTNO NUMBER(2), 
    PRIMARY KEY (EMPNO),
    FOREIGN KEY (DEPTNO) REFERENCES DEPT01(DEPTNO)  -- FK 제약조건
);

--------------------------
-------- ★ DML ★ --------
--------------------------

-- 1. INSERT INTO 
    -- 1) INSERT INTO 테이블이름 (필드명1, 필드명2, 필드명3, ...) VALUES (값1, 값2, 값3, ...);  
       -- 필드를 정해서 집어넣는 방식, 앞의 필드명 수와 값 개수가 같아야함
    -- 2) INSERT INTO 테이블이름 VALUES (값1, 값2, 값3, ..., 값N);  
        -- 전체 필드에 값을 넣는 방식, 전체 필드 수 만큼 값 개수가 필요

SELECT * FROM DEPT01;
SELECT * FROM EMP01;
SELECT * FROM BOOK;

INSERT INTO DEPT01 (DEPTNO, DNAME, LOC) VALUES (15, '재무', 'SEOUL');
INSERT INTO DEPT01 VALUES (50, '설계', 'BUSAN');
INSERT INTO DEPT01 VALUES (60, '큐레이션', 'SILLIM');
INSERT INTO DEPT01 (DEPTNO, LOC, DNAME ) VALUES (45, 'INCHEON', '지원');
INSERT INTO DEPT01 (DEPTNO, DNAME  ) VALUES (55, '설계');    -- 묵시적으로 NULL 입력
INSERT INTO DEPT01 (DEPTNO, DNAME, LOC  ) VALUES (90, '고객센터', NULL); -- 명시적으로 NULL 입력
SELECT * FROM DEPT01;
COMMIT; -- 트랜젝션 영역에 쌓여있는 DML 명령어 수행
SELECT * FROM DEPT01;
-- 서브쿼리를 이용한 INSERT
    --EX. DEPT테이블에서 10~30 부서의 내용을 DEPT01 테이블에 INSERT
    INSERT INTO DEPT01 SELECT * FROM DEPT WHERE DEPTNO < 40;
    SELECT * FROM DEPT01;
    COMMIT;