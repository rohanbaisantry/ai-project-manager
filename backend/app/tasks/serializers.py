from app.companies.schemas import CompanySchema
from app.tasks.models import Task
from app.tasks.schemas import TaskSchema
from app.users.schemas import UserSchema


def serialize_task(
    task: Task, asignee: UserSchema | None = None, company: CompanySchema | None = None
) -> TaskSchema:
    task_schema = TaskSchema(
        id=task.id,
        name=task.name,
        description=task.description,
        comments=task.comments,
        start_datetime=task.start_datetime,
        due_datetime=task.due_datetime,
        next_follow_up_datetime=task.next_follow_up_datetime,
        is_completed=task.is_completed,
        company=company,
        company_id=company.id if company else task.company.to_ref().id,
        asignee=asignee,
        asignee_id=asignee.id if asignee else task.asignee.to_ref().id,
    )
    return task_schema
