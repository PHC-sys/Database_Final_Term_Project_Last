# Database_Final_Term_Project_Last
2019147006, 2019147021, 2019147027

Using pymysql library with mysql data schema
Requirement: pymysql, datetime, pandas

Sequence for Using this code.
1. create_schema (should check the mysql password(environment path) & dbName & filename)
2. initialize
3. logIn

<dbModule.py>
class : Database - 데이터베이스 객체 (조교님이 주신 파일 변형하여 사용함)
  method:
    init: db 연결 및 cursor 설정
    logcheck: id, password 입력 받아서 데이터 베이스와 체크 후 로그인 확인
    get_list: TableName, columnName(개수제한x) 입력 받아서 해당 테이블 내 지정된 컬럼 데이터들 전부 다 딕셔너리로 출력
    get_primary_keys_info: TableName 입력 받아서 해당 테이블의 Primary Key 리스트로 출력
    sign_up: PhoneNumber, id, Password, , SchoolMail 입력 받아서 회원가입 실행(실제로 customer 테이블에 Insert)
    survey_submission: 개인이 수요조사를 하면서 입력한 데이터들을 데이터베이스 demand_survey 테이블에 Insert
    menu_evaluation_taste: 맛 관련 사후 만족도 조사에 대한 데이터들을 menu_evaluation_taste 테이블에 Insert
    menu_evaluation_quantity: 양 관련 사후 만족도 조사에 대한 데이터들을 menu_evaluation_taste 테이블에 Insert
    execute: sql문 입력받아서 실행
    executeOne: 실행 후 커서가 데이터 1개 반환
    executeAll: 실행 후 커서가 모든 데이터 반환
    commit: 커밋
    close: 데이터베이스 닫음
    
<sandbox>
    convertor: *arg(다중인자)를 입력 받아 튜플형태를 문자열 합으로 변환

<create_schema.py>
    create-schema: db에 스키마 생성
    create-tables: sql file 입력 받아서 create 명령 실행(데이터 테이블 생성)
    
<initialize.py>
    initialize: Database 객체 입력 받아서 각 테이블 별 랜덤 데이터들 생성

<generator.py>
    customer_info_generator: 랜덤으로 회원 데이터 채워주는 함수
    days_meal_generator: 기간값을 입력받아 오늘부터 이전 몇 일까지 days_meal Insert(Initialize에 사용)
    update_days_meal_generator: 기간값을 입력받아 오늘부터 몇 일 뒤까지의 days_meal Insert(Initialize에 사용)
    initial_leftover_generator: leftover 랜덤 데이터 생성
    initial_menu_management_generator: 일별 메뉴 데이터 생성
    initial_demand_survey_generator: 수요조사 랜덤 데이터 생성
    initial_menu_evaluation_generator: 만족도조사 랜덤 데이터 생성 
   
<everyday_update.py>
    everyday_update: days_meal, leftover, menu_management 테이블 데이터 오늘 날짜까지 업데이트
    update_menu_management: days_meal, menu_management 테이블 일주일 뒤 데이터까지 업데이트

<delete_data.py>
    delete_data: Database 객체와 tableName 입력받고, 추가적인 pk data를 input으로 받아 테이블의 pk value에 따른 칼럼들 삭제
    
<logIn.py>
    log_in: 맨처음 로그인 창 실행 - 로그인, 회원가입, 나가기 선택 가능
    customer_service: 로그인 이후 Announcement, Demand Survey, Menu Evaluation, Withdrawl, Go Back 지원
    demand_survey: 메뉴 조회, 수요조사 참여 가능
    menu_evaluation: 맛, 양에 따른 만족도 조사 참여 가능
