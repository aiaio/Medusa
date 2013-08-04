<<<<<<< HEAD
from __future__ import with_statement
from fabric.api import run, sudo, cd, env


def setup(setup_type):
	if setup_type == 'stage':
		env.hosts = stagingServer
	elif name == 'QA':
		env.hosts = qaServer
	else:
		raise ValueError('Invalid Setup Type')

def update(user, environment, local_branch, remote_branch):
	setup(environment)
	run('sudo su - %s -c \'cd ~/%s/ && git checkout  %s\'' % (user,environment,local_branch,)) 
	run('sudo su - %s -c \'cd ~/%s/ && git pull %s\'' % (user,env,remote_branch,)) 

def clone(user, path, gitpath):
	setup(environment)
	env.user = user	
	with cd(path):
		run('git init')
		run('git clone %s' % gitpath)
		
def updatewithsupport(user,directory, branch):
	setup(environment)
	run('sudo su - %s -c \'cd ~/%s && git pull\''% (user,directory,))

def status(user,location):
	run('sudo su - %s -c \'cd ~/%s && git status\''% (user,location))

def clone_with_support(user, location, gitpath):
	setup(environment)
	run('sudo su - %s -c \'mkdir -p %s\''% location)
	run('sudo su - %s -c \'cd %s && git init && git clone %s\''% (user,location,gitpath,)) 

def branch(user, location):
	setup(environment)
    run('sudo su - %s -c \'cd %s && git branch\''% (user,location))

=======
from __future__ import with_statement
from fabric.api import run, sudo, cd, env



def setup(setup_type):
    if setup_type == 'stage':
        env.hosts = setup_type.stagingServer
    elif name == 'QA':
        env.hosts = setup_type.qaServer
    else:
        raise ValueError('Invalid Setup Type')

#Run commands through sudo - username

def update(user, environment, local_branch, remote_branch):
    setup(environment)
    run('sudo su - %s -c \'cd ~/%s/ && git checkout  %s\'' %
        (user, environment, local_branch, ))
    run('sudo su - %s -c \'cd ~/%s/ && git pull %s\'' %
        (user, env, remote_branch,))

def clone(user, path, gitpath):
    setup(env)
    env.user = user
    with cd(path):
        run('git init')
        run('git clone %s' % gitpath)

def updatewithsupport(user, directory, branch):
    setup(environment)
    run('sudo su - %s -c \'cd ~/%s && git pull\'' %
        (user, directory,))

def status(user,location):
    run('sudo su - %s -c \'cd ~/%s && git status\'' %
        (user, location))

def clone_with_support(user, location, gitpath):
    setup(environment)
    run('sudo su - %s -c \'mkdir -p %s\'' % location)
    run('sudo su - %s -c \'cd %s && git init && git clone %s\'' %
        (user,location,gitpath,))

def branch(user, location):
    setup(environment)
    run('sudo su - %s -c \'cd %s && git branch\'' %
        (user, location))
>>>>>>> 7bb4520d42051263123a2639b8c80456d8935c85
