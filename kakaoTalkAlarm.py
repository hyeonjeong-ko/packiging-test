import requests
import json
import os
from datetime import datetime, timedelta

event_name = os.environ.get('EVENT_NAME')
merged_status = os.environ.get('MERGED_STATUS')
send_to_function = os.environ.get('SEND_TO_FUNCTION') #이거 yml에서 분기되는거라 좀 고쳐야 할듯
rest_api_key = os.environ.get('REST_API_KEY') #ㅇㅇ
msg_template = os.environ.get('MSG_TEMPLATE') #ㅇㅇ

access_token = os.environ.get('ACCESS_TOKEN')
refresh_token = os.environ.get('REFRESH_TOKEN')

# Get user information from environment variables
user_name = os.environ.get('USER_NAME')
commit_time = os.environ.get('COMMIT_TIME')
commit_message = os.environ.get('COMMIT_MESSAGE')
from_branch = os.environ.get('FROM_BRANCH')
to_branch = os.environ.get('TO_BRANCH')
repo_url = os.environ.get('REPO_URL')
msg_img = os.environ.get('MSG_IMG')

if msg_img == None:
    msg_img = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Font_Awesome_5_brands_github.svg/1200px-Font_Awesome_5_brands_github.svg.png"


# Print the user information
print("User Name:", user_name)
print("Commit Time:", commit_time)
#print("New Commit Time:", new_commit_time)
print("Commit Message:", commit_message)
print("From Branch:", from_branch)
print("To Branch:", to_branch)
print("MSG_TEMPLATE", msg_template)
print("REPO_URL", repo_url)

if event_name == 'pull_request':
    if merged_status == 'true':
        print("This is a merged Pull Request.")
        event_name = 'Merge'
    else:
        print("This is an open Pull Request.")
elif event_name == 'push':
    print("This is a Push event.")
else:
    print("Event type:", event_name)


description=""
# 조건문을 사용하여 데이터 준비
if event_name == "push":
    description += f"{to_branch}(으)로 push 완료\n'{commit_message}'"
elif event_name == "pull_request":
    description += f"{from_branch}→{to_branch}\n'{commit_message}'"


# 나에게 보내기
if send_to_function == 'send_to_me':
    
    print(access_token)
    
    # kakao_code.json 파일 저장
    # with open("kakao_code.json", "w") as fp:
    #     json.dump(tokens, fp)

    
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization": "Bearer " + access_token # {access token}
    }
    
    
    # 사용자 템플릿 변수에 따라 텍스트, 피드 설정 - 개인 테스트용
    
    print("description:" + description)

    print("메시지부분시작!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    print("msg_template: " + msg_template)
    
    if msg_template == "feed":
        data = {
            "template_object" : json.dumps({ "object_type" : "feed",
                                             "content":{
                                                 "title":f"{user_name}님이 {event_name}(을)를 했어요!",
                                                 "description": description,
                                                 "image_url": msg_img,
                                                 "link": {
                                                        "web_url": repo_url,
                                                        "mobile_web_url": repo_url
                                                  }
                                             },
                                            "button_title": "깃헙으로 이동하기"                            
            })
        }
    elif msg_template == "text":
        print("메시지 템플릿 텍스트 분기 진입")
        data = {
            "template_object" : json.dumps({ "object_type" : "text",
                                             "text" : f"{user_name}님이 {event_name}을 했어요!\n{description}",
                                             "link" : {
                                                         "web_url" : repo_url,
                                                         "mobile_web_url" : repo_url
                                                      },
                                            "buttons": [
                                                {
                                                    "title": "깃헙으로 이동하기",
                                                    "link": {
                                                    "web_url": repo_url,
                                                      "mobile_web_url": repo_url
                                                    }
                                                }
                                              ]
                                             
            })
        }
    
    response = requests.post(url, headers=headers, data=data)
    if response.json().get('result_code') == 0:
        print('메시지를 성공적으로 보냈습니다.')
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))


# 친구에게 보내기
elif send_to_function == 'send_to_friends':
    print("친구에게 보내기!!!!!!!!!!!!!!!!!!!!!!")
    print("refresh_token"+ refresh_token)

    # 카카오톡 메시지 API
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": rest_api_key,
        "refresh_token": refresh_token
    }
    response = requests.post(url, data=data)
    tokens = response.json()
    
    # kakao_code.json 파일 저장
    with open("kakao_code.json", "w") as fp:
        json.dump(tokens, fp)
    
    # 카카오 API 엑세스 토큰
    with open("kakao_code.json", "r") as fp:
        tokens = json.load(fp)
    print(tokens["access_token"])

    url = "https://kapi.kakao.com/v1/api/talk/friends" #친구 목록 가져오기
    header = {"Authorization": 'Bearer ' + tokens["access_token"]}
    result = json.loads(requests.get(url, headers=header).text)
    friends_list = result.get("elements")
    print(friends_list)
    
    friend_id = friends_list[0].get("uuid")
    print(friend_id)
    
    # 카카오톡 메시지
    url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
    header = {"Authorization": 'Bearer ' + tokens["access_token"]}
    
    # Git Action에서 받은 정보를 사용하여 메시지 내용 구성
    #(sc가 추가)근데 user_info_pull_request인지 user_info_push인지 체크
    #if event_name == 'pull_request':
    #    user_name = "'${{ steps.user_info_pull_request.outputs.user_name }}'"
    #    commit_time = "'${{ steps.user_info_pull_request.outputs.commit_time }}'"
    #    commit_message = "'${{ steps.user_info_pull_request.outputs.commit_message }}'"
    
    #else:
    #    user_name = "'${{ steps.user_info_push.outputs.user_name }}'"
    #    commit_time = "'${{ steps.user_info_push.outputs.commit_time }}'"
    #    commit_message = "'${{ steps.user_info_push.outputs.commit_message }}'"
    
    # Get user information from environment variables
    user_name = os.environ.get('USER_NAME')
    commit_time = os.environ.get('COMMIT_TIME')
    commit_message = os.environ.get('COMMIT_MESSAGE')
    #origin_branch = os.environ.get('ORIGIN_BRANCH')
    #branch_name = os.environ.get('BRANCH_NAME')
    from_branch = os.environ.get('FROM_BRANCH')
    to_branch = os.environ.get('TO_BRANCH')
    
    # pull request과정에서의 시간 변수는 시차 존재
    # Commit time을 문자열에서 datetime 객체로 변환
    commit_time_datetime = datetime.strptime(commit_time, '%Y-%m-%d %H:%M:%S %z')
    
    # 9시간을 추가하여 새로운 datetime 객체 생성
    new_commit_time_datetime = commit_time_datetime + timedelta(hours=9)
    
    # new_commit_time을 원하는 형식으로 변환하여 출력
    new_commit_time = new_commit_time_datetime.strftime('%Y-%m-%d %H:%M:%S')
    
    
    #print!!
    print("User Name:", user_name)
    print("Commit Time:", commit_time)
    print("New Commit Time:", new_commit_time)
    print("Commit Message:", commit_message)
    print("From Branch:", from_branch)
    print("To Branch:", to_branch)

    #친구가 여러명이면 list에서 반복문
    for friend_id in friedns_list: 
        # 조건문을 사용하여 데이터 준비
        if event_name == 'push':
            description = f"{to_branch}로 push 완료\n'{commit_message}'"
        elif event_name == 'pull_request':
            description = f"{from_branch}→{to_branch}\n'{commit_message}'"
    
        if msg_template == 'feed':
            data = {
                'receiver_uuids': f'["{friend_id}"]',
                "template_object": json.dumps({
                    "object_type": "feed",
                    "content": {
                        "title": f"{user_name}님이 {event_name}을 했어요!",
                        "description": description,
                        "image_url": msg_img,
                        "link":{
                            "web_url": repo_url,
                            "mobile_web_url": repo_url
                        }
                    },
                    "button_title": "깃헙으로 이동하기"
                })
            }
        elif msg_template == 'text':
            data={
                'receiver_uuids': '["{}"]'.format(friend_id),
                "template_object": json.dumps({
                    "object_type":"text",
                    "text":f"{user_name}님이 {event_name}을 했어요!\n{description}",
                    "link":{
                        "web_url" : repo_url,
                        "mobile_web_url" : repo_url
                    },
                    "button_title": "깃헙으로 이동하기"
                })
            }
        
    
    print(f"메시지:'{commit_message}'\n시간:'{commit_time}'\n")
    
    response = requests.post(url, headers=header, data=data)
    response.status_code
