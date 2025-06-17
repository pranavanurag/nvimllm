source .venv/bin/activate
export OPENAI_API_KEY=$(cat KEY)
nohup python service.py > /dev/null 2>&1 &
