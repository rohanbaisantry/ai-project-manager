from backend.app.companies.schemas import CompanySchema
from backend.app.tasks.models import Task
from backend.app.tasks.schemas import TaskSchema
from backend.app.users.schemas import UserSchema


async def serialize_task(
    task: Task, asignee: UserSchema | None = None, company: CompanySchema | None = None
) -> TaskSchema:
    task_schema = TaskSchema(
        id=task.id,
        name=task.name,
        comments=task.comments,
        start_datetime=task.start_datetime,
        due_datetime=task.due_datetime,
        next_follow_up_datetime=task.next_follow_up_datetime,
        is_completed=task.is_completed,
        company=company,
        company_id=company.id if company else task.company,
        asignee=asignee,
        asignee_id=asignee.id if asignee else task.asignee,
    )
    return task_schema
