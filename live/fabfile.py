from __future__ import with_statement
from fabric.api import *


env.user = 'support'

def update(user, environment, local_branch, remote_branch):
	run('sudo su - %s -c \'cd ~/%s/ && git checkout  %s\'' % (user,environment,local_branch,)) 
	run('sudo su - %s -c \'cd ~/%s/ && git pull %s\'' % (user,env,remote_branch,)) 

def clone(user, path, gitpath):
	env.user = user	
	with cd(path):
		run('git init')
		run('git clone %s' % gitpath)
		

def updatewithsupport(user,directory, branch):
	#run('sudo su - %s -c \'cd ~/%s/ && git checkout %s && git pull\'' % (user,directory, branch,)) 
	run('sudo su - %s -c \'cd ~/%s && git pull\''% (user,directory,))

def status(user,location):
	run('sudo su - %s -c \'cd ~/%s && git status\''% (user,location))

def clone_with_support(user, location, gitpath):
	run('sudo su - %s -c \'mkdir -p %s\''% location)
	run('sudo su - %s -c \'cd %s && git init && git clone %s\''% (user,location,gitpath,)) 
def branch(user, location):
    run('sudo su - %s -c \'cd %s && git branch\''% (user,location))

"""
def deploy(user,env,branch):
	run('sudo su - %s -c \'cd ~/%s/ && git clone
"""

"""
def checkSSHAccess():



def isReady():
	checkVMs()
	checkCon()

def checkVMs():
	print ("checking VMs")

def checkCon():
	print ("checking internet con")
"""

