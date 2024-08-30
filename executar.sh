#! /bin/bash    
cd /home/ubuntu/RPA_Python
python3 -m venv my_env
source my_env/bin/activate

# virtualenv is now active, which means your PATH has been modified.
# Don't try to run python from /usr/bin/python, just run "python" and
# let the PATH figure out which version to run (based on what your
# virtualenv has configured).

python3 RPACotacao.py