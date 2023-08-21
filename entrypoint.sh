#!/bin/sh -l

echo "Hello entry~!"

# Grant execute permission to all files in the directory
chmod +x *

ls

cd /app

ls

python -m pip install --upgrade pip
pip install requests

echo "===============================================명령어 진입==============================================="

# 이벤트 이름에 따라 환경 변수 설정
if [ "$GITHUB_EVENT_NAME" = "pull_request" ]; then
  echo "EVENT_NAME=Pull Request" >> $GITHUB_ENV
  echo "MERGED_STATUS=${{ github.event.pull_request.merged }}" >> $GITHUB_ENV
elif [ "$GITHUB_EVENT_NAME" = "push" ]; then
  echo "EVENT_NAME=Push" >> $GITHUB_ENV
elif [ "$GITHUB_EVENT_NAME" = "workflow_run" ]; then
  echo "EVENT_NAME=Workflow Run" >> $GITHUB_ENV
fi

# # 이벤트에 따라 유저 정보 설정
# if [ "$GITHUB_EVENT_NAME" = "push" ]; then
#   USER_NAME=$(git log -1 --pretty=format:'%an')
#   COMMIT_TIME=$(git log -1 --pretty=format:'%ci')
#   COMMIT_MESSAGE=$(git log -1 --pretty=format:'%s')
#   FROM_BRANCH=$(git symbolic-ref --short HEAD)  # 현재 브랜치 이름 가져오기
#   TO_BRANCH=${GITHUB_REF#refs/heads/}  # GITHUB_REF에서 "refs/heads/" 접두사 제거
#   echo "USER_NAME=$USER_NAME" >> $GITHUB_ENV
#   echo "COMMIT_TIME=$COMMIT_TIME" >> $GITHUB_ENV
#   echo "COMMIT_MESSAGE=$COMMIT_MESSAGE" >> $GITHUB_ENV
#   echo "FROM_BRANCH=$FROM_BRANCH" >> $GITHUB_ENV
#   echo "TO_BRANCH=$TO_BRANCH" >> $GITHUB_ENV
# fi

# if [ "$GITHUB_EVENT_NAME" = "pull_request" ]; then
#   USER_NAME=$(git log -1 --pretty=format:'%an')
#   COMMIT_TIME=$(git log -1 --pretty=format:'%ci')
#   COMMIT_MESSAGE="${{ github.event.pull_request.title }}"  # 풀 리퀘스트 제목 사용
#   FROM_BRANCH=${{ github.event.pull_request.head.ref }}
#   TO_BRANCH=${{ github.event.pull_request.base.ref }}
#   echo "USER_NAME=$USER_NAME" >> $GITHUB_ENV
#   echo "COMMIT_TIME=$COMMIT_TIME" >> $GITHUB_ENV
#   echo "COMMIT_MESSAGE=$COMMIT_MESSAGE" >> $GITHUB_ENV
#   echo "FROM_BRANCH=$FROM_BRANCH" >> $GITHUB_ENV
#   echo "TO_BRANCH=$TO_BRANCH" >> $GITHUB_ENV
# fi

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
# if [ "$GITHUB_EVENT_NAME" = "push" ]; then
#   NEW_CONTENT="## User Profile\n\n"
#   NEW_CONTENT+="### '$COMMIT_TIME'에 '$USER_NAME'님이 merge 하였음을 기록합니다\n\n"
#   NEW_CONTENT+="**Commit Message:** $COMMIT_MESSAGE\n\n"
#   NEW_CONTENT+="${{ steps.read_existing.outputs.existing_content }}\n"
#   NEW_CONTENT+="${{ steps.new_content.outputs.new_content }}\n"
#   echo "::set-output name=new_content::$NEW_CONTENT"
# fi

# # 마크다운 파일 업데이트
# if [ "$GITHUB_EVENT_NAME" = "push" ]; then
#   echo "${{ steps.new_content.outputs.new_content }}" > profile.md
# fi

# # 변경 사항 커밋 및 푸시
# if [ "$GITHUB_EVENT_NAME" = "push" ]; then
#   git config --global user.name "GitHub Actions"
#   git config --global user.email "actions@github.com"
#   git add profile.md
#   git commit -m "Update user profile"
#   git push
# fi

python test.py
python kakaoTalkAlarm.py


