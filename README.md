# 국민학식GO 개발문서

python + django + 카카오톡 옐로아이디 api

비전공자도 개발 할 수 있는 자동응답기 개발문서
## 목차
1. 들어가는 말
2. python이란?
3. 왜 프로그래밍을 배워야 하는가?
4. django(장고)란?
5. 서버와 클라이언트의 이해
6. 카카오톡 옐로아이디 api
7. 개발

## 들어가는 말
안녕하세요 국민학식GO개발자입니다!

사실 너무 작은 서비스이고 개발한 코딩양도 너무 적어서 개발자라고 소개하는것 자체가 조금 부끄럽습니다.
국민대 컴퓨터공학과(현 소프트웨어학부) 고학번의 학생이라면 구글 검색과 여러가지 문서를 참고해서 쉽게 개발 할 수 있지만(정말..?)
이렇게 개발문서를 따로 작성하게 된 이유는 2015년도 부터 국민대학교가 소프트웨어중심 학교로 선정되면서 15학번 학부생분들부터
python을 교양필수로 수강해야한다는 것을 알고 작성하게 되었습니다.

국대전의 글을 보거나 파이썬 조교분들에게 얘기를 들어보면서 수업에 있어서 많은 애로사항이 있다는것을 알게 되었었습니다.
그러면서 자연스럽게 컴퓨터전공생이 아닌 입장에서 파이썬을 배우는것이 얼마나 힘든 일인지 느낄 수 있었습니다.
조금이나마 파이썬이 무엇인지 프로그래밍이 무엇인지, 프로그래밍을 왜 배워야 하는지에 대해 함께 나누고 개발의 즐거움(?)을 나누어 보려 작성해보았습니다.

* 2,3,4장은 비전공자도 쉽게 보실 수 있는 내용이고 5,6장은 개발에 특화된 내용입니다.
>위의 내용은 전적으로 저의 개인적인 의견이며 어느 단체도 어느 학생도 대변하는 말이 아님을 알려드립니다.

## python이란?
![대체텍스트](/img/py1.png "이미지제목")

무려 네이버에 파이썬을 검색했을 때 첫번째로 나오는 네이버사전에 나오는 내용이다.
>**국민대**, 성균관대 등 국내 대학에서도 프로그래밍 **교양** **수업**이 늘어나는 추세다.

사실 파이썬이이 무엇인지 조금만 검색해보면 너무나도 많은 내용이 나온다. 파이썬을 검색 할 때마다 가장 큰 장점으로 나오는 내용이
간결한 문법과 표현구조가 인간의 사고 체계와 닮았다는 내용이다. 전공자라면 그러려니 하고 넘길 수 있는 내용이다. 하지만 비전공자들이
본다면 쉽게 이해가 가지 않을 뿐더러 공감이 1도 되지 않을 것 같다.

그래서 다음으로는 프로그래밍이란 무엇이고, 프로그래밍 언어란 무엇인지 이것을 도대체 왜 전공자도 아닌 내가 배워야하는지에 대해서 알아보도록 하겠다.

아래는 파이썬에 대해 좀더 알아보고 싶은 분들은 꼭 읽어보길 바란다.
  <https://wikidocs.net/book/1>
<http://navercast.naver.com/contents.nhn?rid=122&contents_id=122897>