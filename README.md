# samcli-pyscript
## simple hello world using a python script than runs on command line
### make sure before executing the code
- samcli is installed
- do "aws configure" to cofigure with aws access/secret key
### have all code ready (everything on the folder), app.py, hw.py and template.yaml, packaged.yaml will be created automatically one the code is executed.
- the main file is hw.py to run
- app.py is the lambda function
- template.yaml is the config
### make sure you have aws IAM ready and need the following roles attached
- AWSS3FullAccess
### Once everything ready, follow the steps:
- run sam build
- run sam deploy
- run hw.py [python3 hw.py]
- run the following cli to check whether the stack is created: ``` aws cloudformation describe-stacks --stack-name HelloWorldStack --query "Stacks[0].Outputs" ``` >> this will produce a link, copy paste and hit enter will show the ```Hello, World!```
