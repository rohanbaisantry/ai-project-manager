import aiocron

from app.common.use_cases import CommonUseCases


# Follow-Up Task runs every 5 minutes
@aiocron.crontab("* * * * *")
async def check_and_follow_up_for_tasks():
    print("starting Task")
    use_cases = CommonUseCases()
    await use_cases.check_and_follow_up_for_tasks()
