#!/bin/sh -l

echo "entry point 진입"

# Grant execute permission to all files in the directory
chmod +x *

ls

cd /app

ls

python -m pip install --upgrade pip
pip install requests


python test.py
python kakaoTalkAlarm.py


echo "===============================================세부 명령 진입==============================================="


# # 기존 프로필 내용 읽기
# if [ "$GITHUB_EVENT_NAME" = "push" ]; then
#   if [ -f "profile.md" ]; then
#     EXISTING_CONTENT=$(cat profile.md)
#     echo "::set-output name=existing_content::$EXISTING_CONTENT"
#   else
#     echo "::set-output name=existing_content::"
#   fi
# fi

# # 새 프로필 내용 생성
# if [ "$EVENT_NAME" = "push" ]; then
#   NEW_CONTENT="## User Profile\n\n"
#   NEW_CONTENT+="### '$COMMIT_TIME'에 '$USER_NAME'님이 merge 하였음을 기록합니다\n\n"
#   NEW_CONTENT+="**Commit Message:** $COMMIT_MESSAGE\n\n"
#   # NEW_CONTENT+="${{ steps.read_existing.outputs.existing_content }}\n"
#   echo "::set-output name=new_content::$NEW_CONTENT"
# fi

# 새 프로필 내용 생성
if [ "$EVENT_NAME" = "push" ]; then
  NEW_CONTENT="## User Profile\n\n### '$COMMIT_TIME'에 '$USER_NAME'님이 merge 하였음을 기록합니다\n\n**Commit Message:** $COMMIT_MESSAGE\n\n"
  echo $NEW_CONTENT
fi


# 만약 existing_context가 비어있지 않다면 profile.md 파일 생성 후 내용 추가
if [ -n "$existing_context" ]; then
  echo "만약 existing_context가 비어있지 않다면 profile.md 파일 생성 후 내용 추가"
  echo "$existing_context" >> profile.md
fi

# 마크다운 파일 업데이트
echo "마크다운 파일 업데이트"
if [ -n "$new_content" ]; then
  if [ ! -f "profile.md" ]; then
    touch profile.md  # 파일이 없을 경우 생성
    echo "파일 생성"
  fi
  echo "$new_content" >> profile.md
fi


# 변경 사항 커밋 및 푸시
echo "변경 사항 커밋 및 푸시"
# if [ "$EVENT_NAME" = "push" ]; then
#   # Git 설정
#   git config --global user.name "GitHub Actions"
#   git config --global user.email "actions@github.com"

#   # 커밋 및 푸시
#   git add profile.md  # 변경된 파일을 추가
#   git commit -m "Update user profile"  # 커밋 메시지 설정
#   git push "https://$REPO_TOKEN@github.com/hyeonjeong-ko/test-marketplace.git" HEAD:main  # 토큰을 사용한 푸시
# fi

if [ "$EVENT_NAME" = "push" ]; then
  # Git 설정
  git init
  git clone https://$REPO_TOKEN@github.com/hyeonjeong-ko/test-marketplace.git
  cd test-marketplace
  
  git config --global user.email "YOUR EMAIL"
  git config --global user.name "YOUR NAME"
  git config --global init.defaultBranch main

  
  git add profile.md
  git commit -m "Update user profile"
  git push origin main
fi  

# python test.py
# python kakaoTalkAlarm.py

