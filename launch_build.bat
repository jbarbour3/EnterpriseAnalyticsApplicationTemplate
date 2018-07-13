

@ECHO off

cd C:\Users\jbarbour\PycharmProjects\GUITemplate\App
pyinstaller LastMileToolbox.py --onefile --noconsole --icon lmtb_h9h_icon.ico


For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
For /f "tokens=1-2 delims=/:" %%a in ("%TIME%") do (set mytime=%%a%%b)

ECHO "Creating folder %mydate%_%mytime%"
mkdir C:\Users\jbarbour\PycharmProjects\GUITemplate\Builds\%mydate%_%mytime%

PAUSE


REM "Moving build contents to new folder"
xcopy /s C:\Users\jbarbour\PycharmProjects\GUITemplate\App\build  C:\Users\jbarbour\PycharmProjects\GUITemplate\Builds\%mydate%_%mytime%
xcopy /s C:\Users\jbarbour\PycharmProjects\GUITemplate\App\dist   C:\Users\jbarbour\PycharmProjects\GUITemplate\Builds\%mydate%_%mytime%
move  C:\Users\jbarbour\PycharmProjects\GUITemplate\App\LastMileToolbox.spec   C:\Users\jbarbour\PycharmProjects\GUITemplate\Builds\%mydate%_%mytime%
rmdir /s /q "C:\Users\jbarbour\PycharmProjects\GUITemplate\App\build"
rmdir /s /q "C:\Users\jbarbour\PycharmProjects\GUITemplate\App\dist"


ECHO "Build Complete"
PAUSE