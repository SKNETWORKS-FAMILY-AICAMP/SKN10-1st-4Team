DROP DATABASE IF EXISTS SKN10_4team_1st;
DROP USER IF EXISTS 'SKN10_4team'@'%';

USE mysql;

CREATE USER 'SKN10_4team'@'%' identified BY 'skn1234';
CREATE DATABASE SKN10_4team_1st;

-- SHOW DATABASES;

USE SKN10_4team_1st;

GRANT ALL PRIVILEGES ON SKN10_4team_1st.* TO 'SKN10_4team'@'%';

CREATE TABLE SKN10_4team_1st.Car (
    Year varchar(10) NOT NULL COMMENT '연도',
    CityID varchar(50) NOT NULL COMMENT '지역ID',
    CarCount INT NULL COMMENT '자동차 등록 수',
    CONSTRAINT Car_PK PRIMARY KEY (CityID,Year)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci
COMMENT='지역별 연도별 자동차 등록 수';

CREATE TABLE SKN10_4team_1st.City (
    CityID varchar(50) NOT NULL COMMENT '지역ID',
    CItyName varchar(100) NULL COMMENT '지역명',
    CONSTRAINT City_PK PRIMARY KEY (CityID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci
COMMENT='지역 정보';

SHOW TABLES;