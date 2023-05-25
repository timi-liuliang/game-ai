REM upgrade pip
python -m pip install --upgrade pip

REM install virtual env
pip install virtualenv

REM create environment
python -m venv street-fight-ai-env

REM activate myenv
source ./street-fight-ai-env/Scripts/activate

REM install requirements
pip install -r requirements.txt

pause