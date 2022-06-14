# Summer 2022 - Python Tutorial
Simple Python/ROOT Tutorial for CMS@Rice Summer 2022

## Logging into a Cluster
### Lxplus
Lxplus is the CERN computing cluster based in Geneva. Using your cern credentials to login,
```
ssh <username>@lxplus.cern.ch>
(Prompted to put password)
```
### cmslpc
cmslpc is the FNAL computing cluster based in Chicago. Login requires downloading a Kerberos configuration file and modifying your .ssh. Directions can be found [here](https://uscms.org/uscms_at_work/computing/getstarted/uaf.shtml)
Using your FNAL credentials you then do,
```
kinit <username>@FNAL.gov
(Prompted to put password)

ssh -Y <username>@cmslpc-sl7.fnal.gov
```

## Setting Up CMSSW
CMSSW is CMS SoftWare that will create an evironment for development and running code. Use `scram list -a` to list all releases of CMSSW. On cmslpc you first need to do `source /cvmfs/cms.cern.ch/cmsset_default.sh`.

```
cd <working_dir>
cmsrel CMSSW_12_0_1
cd CMSSW_12_0_1/src/

cmsenv
```

## Setting Up GitHub
First thing is to generate a key pair using the command using your GitHub email
```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
Press `return` and set passphrase. Copy the contents of `~/.ssh/<file_name>.pub`. Open GitHub>Settings>SSH keys then click Add SSH Key and paste the contents. 

## Pulling from GitHub
Fork this repository using the button in the top right. This will create your own version of the repository for you to edit.

Now you can clone the repository to the cluster using,
```
git clone git@github.com:<github_username>/Summer2022-PythonTutorial.git
cd Summer2022-PythonTutorial
```

Now you can create your own branch for development using,
```
git checkout -b <your_new_branch_name>
git push origin <your_new_branch_name>
```

## Pushing to GitHub After Changes
After making changes to the code you can `add`, `commit`, then `push` your changes to your new branch on your fork.
```
git add .
git commit -m "Write Some Message"
git push
```
