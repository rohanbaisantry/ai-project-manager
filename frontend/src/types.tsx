export type CompanyGlobalDataSchema = {
  user: UserSchema;
  company: CompanySchema;
  team_members: UserSchema[];
  tasks: TaskSchema[];
};

export type CompanySchema = {
  id: string;
  name: string;
};

export type CreateTaskEntity = {
  name: string;
  description: string;
  start_datetime: string;
  due_datetime: string;
  next_follow_up_datetime?: string | null;
  company_id: string;
  assignee_user_id: string;
};

export type CreateTeamMemberEntity = {
  name: string;
  mobile: string;
};

export type HTTPValidationError = {
  detail: ValidationError[];
};

export type SaveNewChatEntity = {
  message: string;
};

export type SignupEntity = {
  user_name: string;
  user_mobile: string;
  company_name: string;
};

export type TaskSchema = {
  id: string;
  name: string;
  description: string;
  start_datetime: string;
  due_datetime: string;
  next_follow_up_datetime?: string | null;
  comments: string[];
  assignee?: UserSchema | null;
  assignee_id: string;
  company?: CompanySchema | null;
  company_id: string;
  is_completed: boolean;
};

export type UpdateTaskEntity = {
  new_comment?: string | null;
  due_datetime?: string | null;
  start_datetime?: string | null;
  is_completed?: boolean | null;
  next_follow_up_datetime?: string | null;
};

export type UserChat = {
  content: string;
  sent_by: UserChatSentBy;
  sent_at: string;
};

export type UserChatSentBy = "USER" | "SYSTEM";

export type UserSchema = {
  id: string;
  name: string;
  role: string;
  mobile: string;
  chats: UserChat[];
  company?: CompanySchema | null;
  company_id: string;
};

export type ValidationError = {
  loc: (string | number)[];
  msg: string;
  type: string;
};
