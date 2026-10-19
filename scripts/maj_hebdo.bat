@echo off
rem Pipeline hebdomadaire Comparer 2027 — appele par la tache planifiee
cd /d "C:\Users\gille\CascadeProjects\Portfolio\Projects\Election2027"
if not exist logs mkdir logs
python -X utf8 editorial\outils\pipeline_dimanche.py >> logs\pipeline-%DATE:~6,4%-%DATE:~3,2%-%DATE:~0,2%.log 2>&1
