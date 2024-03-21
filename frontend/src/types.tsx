export type UserChat = {
  sent_by: "SYSTEM" | "USER",
  sent_at: Date,
  content: string,
}

export type Company = {
  id: string,
  name: string
}

export type Task = {
  id: string,
  name: string,
  description:string,
  due_datetime: Date,
  start_datetime: Date,
  next_follow_up_datetime: Date,
  assignee_id: string,
  company_id: string,
  company?: Company,
  assignee?: User,
}

export type User = {
  id: string,
  name: string,
  role: string,
  mobile: string,
  user_chats: UserChat[]
}


export type GlobalUserDetails = {
  user: User,
  company: Company,
  tasks: Task[],
  team_members: User[]
}
