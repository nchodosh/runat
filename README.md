# RUNAT

This is a hacky way of running commands at a specified time with the current environment. It's useful when working on a system that does not contain the "at" command or when it's important to recreate the current environment for a scheduled job.

## Overview

The basic usage of this command is
```runat [TIME] [COMMAND]```
which will run COMMAND at TIME where TIME can be written in most formats (parsed by dateutil) but only the minute hour and day will be used. The command will execute with your current environment in a bash login shell (so your .bashrc aliases will be there). The command will print the exact time selected upon termination so you can check to be sure it is correct. You can also use the `--dry-run` flag to check what will be setup without actually doing anything. 

When run, a file will be created at ~/.at/<JOBID>.env containing the current environment and an entry will be added to your crontab file to run the command. NOTE, this does mean your crontab will be polluted with old entries which will produce an error message in your mail file every year at [TIME]. This isn't a big deal but if it bothers you just manually delete them from your crontab once a year.


## Install

Just run `pip install .` in the main directory and you should be good to go

## Example Usage

Make a testfile on October 14th at 3PM that contains the current PATH:

```
runat '3PM 14 Oct' 'echo $PATH > ~/testfile'
```

Run script 'train.py' today at 5PM, train.py should live in the current directory

```
runat '5PM' 'python train.py'
```






