StatKey
=======

Get the status of a git repo with a one key command:

$ cd ~/mygitrepo
$ s
    On branch master
    Your branch is up-to-date with 'origin/master'.
    
    nothing to commit, working directory clean

Or a mercurial repo, and it will show a diff for either type of repo if it is < 80 lines:

$ cd ~/mymercurialrepo
$ s
     diff -r d511abd3422a bin/p
    --- a/bin/p	Thu Feb 19 21:25:35 2015 +0800
    +++ b/bin/p	Thu Feb 19 23:52:35 2015 +0800
    @@ -25,8 +25,8 @@
     fi
     
     
    -#if [ "$1" == "d" ]; then
    -#    cd $PROJECTDIR
    -#    bash
    -#fi
    +if [ "$1" == "d" ]; then
    +    cd $PROJECTDIR
    +    bash
    +fi
     
    ==========
    M bin/p


Install
=======

First ensure you have python pip installed, then run:

$ sudo pip install statkey
