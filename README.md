# <img src="https://play-lh.googleusercontent.com/Ob9Ys8yKMeyKzZvl3cB9JNSTui1lJwjSKD60IVYnlvU2DsahysGENJE-txiRIW9_72Vd" style="height: 32px;"> Kakao Alarm Bot</div>

<div align="center">
<p>
  <img src="https://github.com/2020311920/packiging-test/assets/80453145/520f6ca8-ce6d-4381-876e-be6994f805ab" style = "height: 300px;">
  <img src="https://github.com/hyeonjeong-ko/skku-git-assignment-1/assets/80453145/d24bf58c-7042-45d4-a281-55907835afb2" style = "height: 300px;">
  <img src="https://github.com/hyeonjeong-ko/skku-git-assignment-1/assets/80453145/ffbb93c4-be88-415c-889c-43bdb07b517c" style = "height: 100px;">
  <img src="https://github.com/hyeonjeong-ko/skku-git-assignment-1/assets/80453145/af5dda32-10f6-42cf-b303-1c9ac42b7229" style = "height: 100px;">
</p>
</div>
<p>
  더 이상 팀원에게 따로 일일이 직접 연락 하지 마세요!<br> Github Action을 활용하여 만든 Kakao Alarm Bot과 함께라면 실시간으로 작업내용을 팀원에게 알려줄 수 있습니다!
</p>

## <img src="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ftistory1.daumcdn.net%2Ftistory%2F4346785%2Fattach%2F6018d9cab34440c6bccec9dee83bbc57" style="height: 32px;"> 사전 설정 - Kakao Developer</div>

1. [Kakao Developers](https://developers.kakao.com/)에 들어가 내 애플리케이션에 들어간다.<br>
> <img src="https://github.com/hyeonjeong-ko/skku-git-assignment-1/assets/80453145/9af6470a-cb3b-4870-afe5-46d633ebda96" style = "width: 700px;">
<br>

2. 애플리케이션이 없다면 새로 만듭니다.<br>
> <img src="https://github.com/hyeonjeong-ko/skku-git-assignment-1/assets/80453145/11a52288-e856-4d6b-a69e-f25cb3902022" style = "width: 700px;">
<br>

3. 좌측 "팀 관리"에서 본인 팀원의 카카오톡 ID를 입력하여 팀원을 초대하세요.<br>
> <img src = "https://github.com/hyeonjeong-ko/skku-git-assignment-1/assets/80453145/ba4d7ace-0ff5-4acd-a625-e5ab73ac1316" style = "width: 700px;">
<br>

4. 좌측의 "플랫폼" >> "WEB"에서 "https://github.com" 를 추가해주세요.<br>
> !중요 전제조건! 반드시 **기본링크**만 가능합니다. ex)https://github.com/user_name/.... -> 불가!!!<br>
> 나중에 메시지나 버튼을 클릭해서 링크를 이동할 때, **"본인 리포지터리"** 로 이동하려면 깃헙으로 설정해야합니다.<br>
> 또한 단순한 테스트라면 Google이나 타 링크도 가능합니다.<br>
> ![platform_web_url](https://github.com/hyeonjeong-ko/skku-git-assignment-1/assets/80453145/6ee11402-cef1-45a3-a2db-033d70101cb9)
<br>

5. 4와 마찬가지로 좌측의 "카카오 로그인"에서 "활성화를 시킨 이후, 아래에 "Redirect URL"에 "https://localhost:3000"을 추가해주세요<br>
> Access Token을 받기 위한 절차입니다
> ![kakao_developer_login_statusON](https://github.com/hyeonjeong-ko/skku-git-assignment-1/assets/80453145/bcf327d4-5379-4327-8a31-5aa6e78c87c0)
> ![kakao_developer_login_RedirectURL](https://github.com/hyeonjeong-ko/skku-git-assignment-1/assets/80453145/fb3f9d25-0670-4bfc-8fe3-1c21fd762e4c)

6. 마지막 단계입니다. 현재 위치하는 "카카오 로그인"에서 하위 항목 중 "동의항목"에 들어가서 개인정보들 중 수집할 것을 설정합니다.<br>
> 동의 목적은 아무렇게나 써도 됩니다. ex) 개발목적

| 항목이름                  	| 상태         	|
|---------------------------	|--------------	|
| 닉네임                    	| 필수 동의    	|
| 카카오 서비스 내 친구목록 	| 이용 중 동의 	|
| 카카오톡 메시지 전송      	| 이용 중 동의 	|

![kakao_developer_login_Agreement](https://github.com/hyeonjeong-ko/skku-git-assignment-1/assets/80453145/aa218215-c643-4616-8318-132fd1d09c02)

## <img src="https://seeklogo.com/images/G/github-actions-logo-031704BDC6-seeklogo.com.png" style="height: 32px;"> 토큰 받기</div>

1. REST API
> <img src = "https://github.com/2020311920/gitAction_marketplace_test1/assets/80453145/987e0634-4877-44a9-aef0-f17243156db8" style = "width: 700px;">

2. CODE KEY
> 아래의 주소를 크롬 **새 시크릿 탭**에서 실행합니다. ({REST API 키}에는 1번의 REST API로 대체합니다)

`https://kauth.kakao.com/oauth/authorize?client_id={REST API 키}&redirect_uri=https://localhost:3000&response_type=code&scope=talk_message`

> 들어가면 **카카오 로그인** 창이 뜰 것입니다. 로그인 하고, **모두 동의** 를 해주세요.
> 그러면 약 10초 정도 후에 아래와 같은 창이 뜰 것입니다.<br>**오류 아닙니다. 정상이에요**
![image](https://github.com/2020311920/packiging-test/assets/80453145/ec05f591-e563-4f7f-8017-ddc72acf43d6)
> 여기서 주소의 `code=...` 부분이 바로 CODE KEY입니다.
![CODE_KEY_URL](https://github.com/2020311920/packiging-test/assets/80453145/6c458bd2-c56d-45cd-af0b-91df8c646f8d)


3. ACCESS TOKEN & REFRESH_TOKEN
> 마지막 단계입니다! Kakao developers에서 **카카오톡 메시지 API**를 통해서 ACCESS TOKEN 과 REFRESH_TOKEN 를 얻어내주세요.
![Access Refresh_Token](https://github.com/2020311920/packiging-test/assets/80453145/605732c5-5218-4b72-bc9c-abef5ab73300)

## <img src="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ftistory1.daumcdn.net%2Ftistory%2F4346785%2Fattach%2F6018d9cab34440c6bccec9dee83bbc57" style="height: 32px;"> **축하합니다!** 이제 카카오 알림 봇을 사용할 일만 남았습니다!</div>

<p>
  메시지 내용<br>
  1. User가 누군지<br>
  2. pull request인지 push(merge)인지<br>
  3. pull request라면 from_branch → to_branch / push(merge)라면 "무슨 브랜치"로 merge하는지<br>
  4. Commit Message가 뭔지<br>

  이 모든 내용을 자동으로 팀원에게 카카오톡 메시지를 보내보세요!<br>
</p>

### 사용자 커스터마이징 설명

|      **이름**      	|                                                   **설명**                                                   	| **필수여부** 	| **Default** 	|   	|
|:------------------:	|:------------------------------------------------------------------------------------------------------------:	|:------------:	|:-----------:	|:-:	|
| `send-to-function` 	|              **나에게 보내기** `send_to_me` 또는 - **친구에게 보내기** `send_to_friends` 중 택 1             	|       ○      	|      -      	|   	|
|     `repo-url`     	|                            카카오톡 메시지 내의 버튼 및 이미지 클릭시 연결될 링크                            	|       ○      	|      -      	|   	|
|   `access-token`   	|  1번에서 **나에게 보내기**를 선택한 경우 필수로 넣어주셔야 합니다. **토큰 받기** 단계의 3단계를 참고하세요.  	|       △      	|      -      	|   	|
|   `refresh-token`  	| 1번에서 **친구에게 보내기**를 선택한 경우 필수로 넣어주셔야 합니다. **토큰 받기** 단계의 3단계를 참고하세요. 	|       △      	|      -      	|   	|
|   `msg-template`   	|                   피드(feed)형식인지(좌) 텍스트(text)형식인지(우) 골라서 넣어주시면 됩니다.                  	|       ×      	|     text    	|   	|
|      `msg-img`     	|    피드로 설정할 경우 피드 이미지에 사용자가 원하는 이미지를 넣을 수 있습니다. 이미지 주소를 입력해주세요.   	|       ×      	| octocat.img 	|   	|

<div align="center">
<p>
  <img src="https://github.com/2020311920/gitAction_marketplace_test1/assets/80453145/135f36dd-f769-45f0-ba54-6760bd6c8bd8" style = "height: 300px;">
  <img src="https://github.com/hyeonjeong-ko/skku-git-assignment-1/assets/80453145/ffbb93c4-be88-415c-889c-43bdb07b517c" style = "height: 100px;">
</p>
</div>

```yml
name: Example for show

on:
  push:
    branches:
      - main

jobs:
  run-hjk-test-v1:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v2
      
    - name: Run kakaoAlarmBot action
      uses: hyeonjeong-ko/packiging-test@5.7
      with:
        repo-url: "your repository url (link sent with the message) "
        send-to-function: "send_to_me" or "send_to_friends"
        access-token: "your kakaotalk access-token key (send_to_me)"
        refresh-token: "your kakaotalk refresh-token key (send_to_friends)"
        msg-template: "text" or "feed" ＊default: text"
        msg-img: "Specifying an image for sending in feed format."
```

## <img src="https://seeklogo.com/images/G/github-actions-logo-031704BDC6-seeklogo.com.png" style="height: 32px;"> 사용예시</div>
> 위의 커스터마이징을 제외한 부분들은 그대로 복사붙여넣기 해주시면 됩니다. 신경쓰지 말아주세요.

```yml
name: My GitHub Action

on:
  push:
    branches:
      - 'main'
      - 'master'
  pull_request:
    types:
      - opened
      - synchronize
    branches:
      - '*'


jobs:
  run-hjk-test-v1:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set User Information
      if: github.event_name == 'push'
      id: user_info_push
      run: |
        USER_NAME=$(git log -1 --pretty=format:'%an')
        COMMIT_TIME=$(git log -1 --pretty=format:'%ci')
        COMMIT_MESSAGE=$(git log -1 --pretty=format:'%s')
        FROM_BRANCH=$(git symbolic-ref --short HEAD)  # Get the current branch name
        TO_BRANCH=${GITHUB_REF#refs/heads/}  # Remove the "refs/heads/" prefix from GITHUB_REF
        echo "USER_NAME=$USER_NAME" >> $GITHUB_ENV
        echo "COMMIT_TIME=$COMMIT_TIME" >> $GITHUB_ENV
        echo "COMMIT_MESSAGE=$COMMIT_MESSAGE" >> $GITHUB_ENV
        echo "FROM_BRANCH=$FROM_BRANCH" >> $GITHUB_ENV
        echo "TO_BRANCH=$TO_BRANCH" >> $GITHUB_ENV

    - name: Set User Information
      if: github.event_name == 'pull_request'
      id: user_info_pull_request
      run: |
        USER_NAME=$(git log -1 --pretty=format:'%an')
        COMMIT_TIME=$(git log -1 --pretty=format:'%ci')
        COMMIT_MESSAGE="${{ github.event.pull_request.title }}"  # Use the pull request title
        FROM_BRANCH=${{ github.event.pull_request.head.ref }}
        TO_BRANCH=${{ github.event.pull_request.base.ref }}
        echo "USER_NAME=$USER_NAME" >> $GITHUB_ENV
        echo "COMMIT_TIME=$COMMIT_TIME" >> $GITHUB_ENV
        echo "COMMIT_MESSAGE=$COMMIT_MESSAGE" >> $GITHUB_ENV
        echo "FROM_BRANCH=$FROM_BRANCH" >> $GITHUB_ENV
        echo "TO_BRANCH=$TO_BRANCH" >> $GITHUB_ENV
      
    - name: Run hjk-test-v1 action
      uses: hyeonjeong-ko/packiging-test@7.4
      with:
        test-variable: "테스트입니다"
        send-to-function: "send_to_friends"
        rest-api-key: "152831f2d43d3d3c3b003a24ec2fa088"
        access-token: "JMStwWRZP369t5LiLCRc_nOlnxDcDJpcRQwCJzheCj10mQAAAYoYr6WV"
        refresh-token: "oHemIwSYyb2OJz5nSX7qQKUTIhQ2w1Pokyooj_XjCj10mQAAAYoYr6WU"
        msg-template: "feed"
        repo-url: "https://github.com/hyeonjeong-ko/test-marketplace"
        msg-img: "https://item.kakaocdn.net/do/416976b0c05bde28d706525b7c6c97ed41d1a2caccd0c566eab28b91e2e5d306"

        
        event_name: ${{ github.event_name }}
        MERGED_STATUS: ${{ github.event.pull_request.merged }}
        USER_NAME: $USER_NAME
        COMMIT_TIME: $COMMIT_TIME
        COMMIT_MESSAGE: $COMMIT_MESSAGE
        FROM_BRANCH: $FROM_BRANCH
        TO_BRANCH: $TO_BRANCH
```

## 라이센스
이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 LICENSE 파일을 참고하세요.
