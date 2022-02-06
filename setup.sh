#create venv
python3 -m venv venv

#set venv path
source venv/bin/activate

#setup
python -m pip install --upgrade pip

pip install -r requirements.txt

bash services/app/scripts/init.sh
#run your app (f5 with vscode)