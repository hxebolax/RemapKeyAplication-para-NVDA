@cls
@echo off
scons --clean
scons pot
git init
git add --all
git commit -m "Versión 0.4"
git push -u origin master
git tag 0.4
git push --tags
pause