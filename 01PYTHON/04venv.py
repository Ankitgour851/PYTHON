# if we want to install any version of python to run a program it will create a virtual env
# on that folder so that we can run that specific version of the python and run  that folder

# create a folder and install virtualenv on that folder
# pip install virtualenv
# want all the packages of python in that virtualev we can use---     virtualenv --system-site-packages harry
# virtualenv harry
# set-executionpolicy remotesigned
# harry\scripts\activates
# deactivate

# we want to sent file, and want to check what packages in that folder
# activate virtualenv
# pip freeze > requuirements.txt

# delete virtualenv
# del harry

# want to reinstall harry with all packages dont delete requuirements.txt
# create virtualenv of  harry
# pip install -r .\requirements.txt