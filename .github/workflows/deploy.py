name: Deploy Application

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: self-hosted

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Deploy to Production
      env:
        SSH_PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}
        REMOTE_USER: ${{ secrets.REMOTE_USER }}
        REMOTE_HOST: ${{ secrets.REMOTE_HOST }}
        REMOTE_PATH: ${{ secrets.REMOTE_PATH }}
      run: |
        echo "$SSH_PRIVATE_KEY" | tr -d '\r' | ssh-add -
        ssh -o StrictHostKeyChecking=no $REMOTE_USER@$REMOTE_HOST 'mkdir -p $REMOTE_PATH'
        rsync -avz --delete --exclude '.git*' . $REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH
        ssh $REMOTE_USER@$REMOTE_HOST 'cd $REMOTE_PATH && ./deploy.sh'
