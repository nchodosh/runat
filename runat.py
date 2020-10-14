import argparse
import os
import uuid
import subprocess
from os.path import expanduser
from dateutil.parser import parse
from crontab import CronTab


parser = argparse.ArgumentParser(description="Tool for running commands at a specific time")
parser.add_argument('time', type = str,
                    help='the time at which to run the command, parsed using dateutil')
parser.add_argument('command', type = str,
                    help = 'the command to run')
parser.add_argument('--dry-run', action='store_true',
                    help = 'just print what will be run and at what time without doing anything')


if __name__ == '__main__':
    args = parser.parse_args()
    envdir = os.path.join(expanduser('~'), '.runat/')
    if not os.path.isdir(envdir):
        os.mkdir(envdir)

    time = parse(args.time)

    if args.dry_run:
        print('DRY RUN: NOTHING WILL BE SET UP TO RUN')
        print('Command will run at {}'.format(str(time)))
        print('The command to run is: {}'.format(args.command))
    else:
        id = str(uuid.uuid4().hex)
        envfile = os.path.join(envdir, id + '.env')
        cmd = 'bash -i -c \'source {} && {}; rm {}\''.format(envfile, args.command, envfile)
        with CronTab(user=True) as cron:
            job = cron.new(command=cmd)
            job.minute.on(time.minute)
            job.hour.on(time.hour)
            job.day.on(time.day)
            job.month.on(time.month)


        subprocess.run('set > {}'.format(envfile), shell=True)
        print('Running the command at {}'.format(str(time)))
        print('Environment saved in {}'.format(envfile))

    
    
