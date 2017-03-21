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

## 1. 들어가는 말
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

## 2. python이란?
![](/img/py1.png "이미지제목")

무려 네이버에 파이썬을 검색했을 때 첫번째로 나오는 네이버사전에 나오는 내용이다.
>**국민대**, 성균관대 등 국내 대학에서도 프로그래밍 **교양** **수업**이 늘어나는 추세다.

사실 파이썬이이 무엇인지 조금만 검색해보면 너무나도 많은 내용이 나온다. 파이썬을 검색 할 때마다 가장 큰 장점으로 나오는 내용이
간결한 문법과 표현구조가 인간의 사고 체계와 닮았다는 내용이다. 전공자라면 그러려니 하고 넘길 수 있는 내용이다. 하지만 비전공자들이
본다면 쉽게 이해가 가지 않을 뿐더러 공감이 1도 되지 않을 것 같다.

그래서 다음으로는 프로그래밍이란 무엇이고, 프로그래밍 언어란 무엇인지 이것을 도대체 왜 전공자도 아닌 내가 배워야하는지에 대해서 알아보도록 하겠다.

아래는 파이썬에 대해 좀더 알아보고 싶은 분들은 꼭 읽어보길 바란다.

<https://wikidocs.net/book/1>
<http://navercast.naver.com/contents.nhn?rid=122&contents_id=122897>

## 3. 왜 프로그래밍을 배워야 하는가?
### 프로그래밍이란?
![](/img/py2.jpg "이미지제목")

프로그래밍이란 간단하게 얘기하면 컴퓨터와의 대화라고 할 수 있겠다.(컴파일러 기계어 등등 중간에 많은 과정들이 있지만) 사람들 사이에서도 대화를 하기 위해서는
언어의 문법과 발음 일정한 약속들이 필요하다. 언어는 사람과 사람사이에서 커뮤니케이션하기위한 약속인 것이다. 그렇다면? 컴퓨터와 대화하기 위해서는 역시 약속이 필요하다.

컴퓨터와의 대화라고 해서 인간이 사용하는 자연어와 다를 것이 없다. 문법과 일정한 약속들이 필요하다. 그리고 그 약속들을 특정한 목적과 용도에 맞게 모아서 책처럼 만든 것이
프로그래밍 언어 인것이다. 프로그래밍 언어에는 많은 종류가 있다. java, c, c++, c#, php등등 그리고 파이썬은 수많은 컴퓨터 프로그래밍 언어중에 하나이다.

2장에서 말했듯이 파이썬언어가 가지는 특징은 '문법과 표현구조가 인간의 사고 체계와 닮았다'였다. 즉 약속과 문법들이 인간이 사용하는 자연어와 가장 흡사하다는 얘기이다.
이것은 누구나 쉽게 접근 할 수 있는 프로그래밍 언어가되는 이유이기도 하다.

### 그렇다면 프로그래밍을 왜! 배워야 하는가
Apple의 아이폰 아이패드를 한번도 들어보지 못한 분은 없을거라고 생각한다. 스티브 잡스또한 한번도 들어보지 못한분은 없을거라고 생각한다.
개인적으로 스티브 잡스는 컴퓨터 분야 뿐만이 아니라 사실상 현존하는 모든 학문에 영향을 미쳤다고 평가해본다. 서점에서 어떠한 책을 뽑아 읽더라도
스티브 잡스의 이름이 없는 책은 거의 없을 정도이다.

왜 갑자기 스티브 잡스 얘기를 하는지 궁금한 분이 있을 것같다. 스티브 잡스 : 더 로스트 인터뷰라는 영화가 있다. 무려 20년전에 스티브 잡스가 인터뷰한 내용을 영화로 만든 영화이다.

>무려 20년 전...

![](/img/py3.png "이미지제목")
![](/img/py4.png "이미지제목")
![](/img/py5.png "이미지제목")
![](/img/py6.png "이미지제목")

영상출처<https://www.youtube.com/watch?v=3JI9WuRSXGc&list=PL1580Q_HQLAx-wypPqJFzmv-5x0PBosUT>

현재 스티브 잡스가 디자이너인지 개발자인지 CEO인지 어떠한 직업으로도 분류 할 수 없을 정도로 많은 업적을 남긴 그가 무려 20년전에 했던 인터뷰 내용이다. 물론 스티브 잡스가 개발자로
개발을 하기 시작했기 때문에 저렇게 말했을지도 모른다. 하지만 필자도 컴퓨터를 배우고 지금은 졸업을 했지만 스티브 잡스가 했던 저 인터뷰내용이 지금은 조금이나마 이해가 간다.

자신의 전공에서 어떠한 문제가 주어지면 해결하는 방법이 머리속에 있을 것이다.(어떠한 옷을 만들어야 하거나 새로운 연기를 하거나)

프로그래밍을 배운다는 것은 어떠한 문제를 만나더라도 머리속에서 흐릿하게 또는 어렴풋이 돌아다니는 자신의 생각을 직접 손으로 또는 컴퓨터로 "논리적"으로 작성하면서
흐릿했던 해결법을 구체화 시켜 손에 거머쥘수 있다는 것이다.

필자는 1년 프로그래밍 필수교양과목에서 이런것을 먼저 배워야한다고 생각한다. 파이썬이나 스크레치는 도구(언어)일 뿐이다.

>컴퓨터를 '자신의 사고 과정을 보여주는 거울'로써 사용..

>그래서 저는 컴퓨터를 교양학으로 봅니다.

>모두가 배워야 한다고 생각해요.

>모두가 일생중 1년정도는 프로그래밍을 배우는데 할애해야 한다고 생각합니다.

어찌됐든... 국민대에서는 2015학년 학부생분들 부터 파이썬을 배워야한다... 조금(?) 슬프고 힘든 현실 일수도 있겠다. 하지만 정말 그 수업시간에 프로그래밍에 대해서 1이라도 배운다면 **개핵이득**인 것이다.

>개 핵 이 득

## 4. django란?
django란 framework이다!!

프레임워크란 프로그래밍 언어로 어떠한 프로그램을 만들때 도와주는 도구이다. 예를 들어보자.

옷을 만들 때 어떤 옷을 만들지 생각을 하고 만들기 시작할 때 옷감이 필요할 것이고 천이나 재료들이 필요할 것이다. 여기서 옷감들을 실로 하나하나 다 만들면서 하지는 않을 것이다.
이미 있는 옷감들을 동대문이나 인터넷을 통해 사고 그 옷감들을 자르고 붙여서 옷을 만들 것이다.

프레임워크란 여기서 옷감과 비슷하다고 할 수 있다. 프로그램을 만들때 꼭 필요한 것 자주 사용 되는 것들을 모아둔 것이다.

그렇다면 django는??

![](/img/d.gif "이미지제목")
