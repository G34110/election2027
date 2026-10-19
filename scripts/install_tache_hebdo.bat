@echo off
rem Installe la tache planifiee Windows : chaque dimanche a 18h00.
rem A executer UNE SEULE FOIS (double-clic suffit, pas besoin d'admin).
schtasks /create /tn "Comparer2027-MAJ-hebdo" /sc weekly /d SUN /st 18:00 /tr "\"C:\Users\gille\CascadeProjects\Portfolio\Projects\Election2027\scripts\maj_hebdo.bat\"" /f
echo.
echo Tache "Comparer2027-MAJ-hebdo" installee : chaque dimanche a 18h00.
echo Pour verifier : schtasks /query /tn "Comparer2027-MAJ-hebdo"
echo Pour supprimer : schtasks /delete /tn "Comparer2027-MAJ-hebdo" /f
pause
