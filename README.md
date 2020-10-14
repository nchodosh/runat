# RUNAT

This is a hacky way of running commands at a specified time with the current environment. It's useful when working on a system that does not contain the "at" command or when it's important to recreate the current enviorment for a scheduled job.

## Overview

The basic usage of this command is
```runat [TIME] [COMMAND]```
which will run COMMAND at TIME where TIME is in standard cron format.

When run file will be created at ~/.at/<JOBID>.env containing the current enviornment and an entry will be added to your crontab file to run the command.
