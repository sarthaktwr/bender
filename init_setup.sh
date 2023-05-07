
echo [$(date)] : 'START'
echo [$(date)] : 'CREATE ENVIRONMENT'
conda create --prefix ./env python=3.8 -y
echo [$(date)] : 'ENVIRONMENT CREATED'
echo [$(data)] : 'ACTIVATE ENVIRONMENT'
source activate ./env
echo [$(date)] : 'ENVIRONMENT ACTIVATED'
echo [$(date)] : 'INSTALL DEPENDENCIES'
pip install -r requirements.txt
echo [$(date)] : 'DEPENDENCIES INSTALLED'
echo [$(date)] : 'END'
