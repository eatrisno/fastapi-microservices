#create venv
python3 -m venv venv

#set venv path
source venv/bin/activate

#setup
python -m pip install --upgrade pip

pip install -r requirements.txt

cd 'services/app'
bash init.sh

_MSG='run your app (f5 with vscode)'
echo $_MSG