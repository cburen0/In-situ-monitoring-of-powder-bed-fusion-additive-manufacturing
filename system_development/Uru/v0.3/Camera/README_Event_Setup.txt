Installation Guide. Since the files to be able to control the event camera are over 5ish GB I can't to upload them to the GitHub. 
1. Follow the guide: https://docs.prophesee.ai/stable/installation/windows_openeb.html#chapter-installation-windows-openeb
	1.1 Install git
	1.2 Install CMake 3.26 (more recent versions might not be compatible)
	1.3 Install Microsoft Visual C++ compiler (MSVC, 64-bit version) included in Visual Studio 2022 - Fall 2023 LTSC (version 17.8). 	    If you install the Build Tools only, make sure Windows 10 SDK is checked, and add English Language Pack.
	1.4 Enable long paths by 
		1. Hit the Windows key, type gpedit.msc and press Enter
		2. Navigate to Local Computer Policy > Computer Configuration > Administrative Templates > System > Filesystem
		3. Double-click the “Enable Win32 long paths” option, select the “Enabled” option and click “OK”

2. Clone the repos:
	a) openb: https://github.com/prophesee-ai/openeb
		-The install location will be referred to <openb>
			-Ex: C:\Users\CBUREN\Documents\GitHub\vcpkg
	b) https://github.com/microsoft/vcpkg
		-The install location will be referred to <vcpkg>
			-Ex: C:\Users\CBUREN\Documents\GitHub\openeb

3. Using powershell do the following
	3.1 cd <vcpkg>
	3.2 .\bootstrap-vcpkg.bat
	    .\vcpkg update
	3.3 git pull
	3.4 .\vcpkg install boost-thread:x64-windows
	

4. Then go to C:\<openb>\utils\windows and copy the vcpkg-openeb.json into <vcpkg> and change the name to vcpkg.json
	4.1 Open the file and copy the COPYTHIS.txt into it

5. Then using PowerShell again in the cd vcpkg enter ".\vcpkg install --triplet x64-windows"

6. If failed then do the following
	6.1 .\vcpkg remove boost-thread --recurse
	6.2 .\vcpkg remove boost --recurse
	6.3 Remove-Item -Recurse -Force .\buildtrees
	6.4 Remove-Item -Recurse -Force .\packages
	6.5 Remove-Item -Recurse -Force .\installed
	6.6 Then use update and git pull
	6.7 If these steps didn't work then find error that what was listed and go to the error logs 
		-The error logs can be found in <vcpkg>\buildtrees. Then go to the file that corresponds to the error. 

7. Download and setup Python
	7.1 Must be 3.12
	7.2 Virtual Environment
		7.2.1 Launch Visual Studio and open the terminal
		7.2.2 In the terminal type "python -m venv C:\tmp\prophesee\py3venv --system-site-package
	
