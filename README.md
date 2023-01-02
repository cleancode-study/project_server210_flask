#### Document
- [요구사항](#요구사항)
- [기술스택](#기술스택)
- [데이터 다이어그램](#데이터-다이어그램)
- [스토리보드](#스토리보드)
- [트러블슈팅](#트러블슈팅)

---
### 요구사항
(프로젝트 완료 후 작성할 보고서)
- 사회 이슈 제기
- 목표 (가설과 근거)
  - 데이터 인사이트 (그래프 선정)
![이미지제목](/static/classification_example.png)
---
### 기술스택
- 개발환경
  - git / github : 모델과 데이터 소스 형상관리 툴 사용
  - Java1.7 (Python3.9 / Anaconda) : 한글 에러 대처 및 LTS버전, 21버전 대비 점층적 JAVA코드 적용과 spring boot 17이상 지원 
  - Gradle : 
  - IntelliJ (PyCharm / Jupyter lab)

- 서버환경
  - GCP Instance / Ubuntu18.04
  - Tomcat8.5 () (WSGI)

- 사용기술
  - Springboot web / Springboot JPA / Thymeleaf
  - Jquery
  - MySQL
  - MVC (route Component)
  - sklearn.preprocessing : 결측치, 이상치 처리를 위한 sklearn 라이브러리
  - sklearn.MLPClassifier / sklearn.tree.DecisionTreeClassifier
  - Pandas / Plotly (Dash) : 2차원 dataframe를 활용한 프로젝트에 적합한 pandas와 비교군에 비해 큰 커뮤니티와 공식문서의 ploty활용

---
### 데이터 다이어그램
(독립변수, 종속변수로 데이터 설명 등등)
![이미지제목](/static/classdiagram_example.png)

---
### 스토리보드
![이미지제목](/static/storyboard_example.png)

---
### 트러블슈팅
(*프로젝트 진행 중에 문제를 어떻게 해결했는지 기록)

| 진행상황   | 이슈                         | 해결                       | 완료날짜       |
|--------|----------------------------|--------------------------|------------|
| closed | data.go.kr 공공데이터 요청        | 포털사이트 접속 공식문서 참조         | 2022-12-12 |
| closed | Java 언어로 api데이터 받기 샘플코드 완성 | @Service 어노테이션 활용한 코드 작성 | 2022-12-12 |
| closed | -                          | -                        | -          |
|