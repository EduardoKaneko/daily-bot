from crontab import CronTab

cron = CronTab(user=True)  
job = cron.new(command='/Users/felipe/projects/daily-bot/script/daily.py')
job.setall('* * * * *')
job.enable()

cron.write()    