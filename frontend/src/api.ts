import { useQuery, useMutation, UseMutationOptions, UseQueryOptions } from "react-query";

import { AppConstants } from "./constants";
import { CompanyGlobalDataSchema, CreateTaskEntity, CreateTeamMemberEntity, SaveNewChatEntity, SignupEntity, TaskSchema, UpdateTaskEntity, UserChat, UserSchema } from "./types";

export const useSignupMutation = (options?: UseMutationOptions<CompanyGlobalDataSchema, Error, SignupEntity>) => {
  return useMutation(async (data: SignupEntity) => {
    const response = await fetch(`${AppConstants.API_BASE_URL}/auth/signup`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    return response.json();
  }, options);
};

export const useLoginMutation = (options?: UseMutationOptions<CompanyGlobalDataSchema, Error, string>) => {
  return useMutation(async (mobile: string) => {
    const response = await fetch(`${AppConstants.API_BASE_URL}/auth/login/${mobile}`, {
      method: "POST",
    });
    return response.json();
  }, options);
};

export const useAuthenticateQuery = (mobile: string, options?: UseQueryOptions<CompanyGlobalDataSchema, Error>) => {
  return useQuery(["authenticate", mobile], async () => {
    const response = await fetch(`${AppConstants.API_BASE_URL}/auth/authenticate?mobile=${mobile}`);
    return response.json();
  }, options);
};

export const useCreateTeamMemberMutation = (options?: UseMutationOptions<UserSchema, Error, { companyId: string; data: CreateTeamMemberEntity }>) => {
  return useMutation(
    async ({ companyId, data }: { companyId: string; data: CreateTeamMemberEntity }) => {
      const response = await fetch(`${AppConstants.API_BASE_URL}/company/team-members/${companyId}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      return response.json();
    },
    options
  );
};

export const useCreateTaskMutation = (options?: UseMutationOptions<TaskSchema, Error, CreateTaskEntity>) => {
  return useMutation(async (data: CreateTaskEntity) => {
    const response = await fetch(`${AppConstants.API_BASE_URL}/tasks`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    return response.json();
  }, options);
};

export const useEditTaskMutation = (options?: UseMutationOptions<TaskSchema, Error, { taskId: string; data: UpdateTaskEntity }>) => {
  return useMutation(
    async ({ taskId, data }: { taskId: string; data: UpdateTaskEntity }) => {
      const response = await fetch(`${AppConstants.API_BASE_URL}/tasks/${taskId}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      return response.json();
    },
    options
  );
};

export const useNewChatReceivedMutation = (options?: UseMutationOptions<UserChat, Error, { userId: string; data: SaveNewChatEntity }>) => {
  return useMutation(
    async ({ userId, data }: { userId: string; data: SaveNewChatEntity }) => {
      const response = await fetch(`${AppConstants.API_BASE_URL}/chats/${userId}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      return response.json();
    },
    options
  );
};
