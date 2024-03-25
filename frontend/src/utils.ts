import { CompanyGlobalDataSchema } from "./types";

export const getTeamMemberNameFromId = (userId: string, globalData: CompanyGlobalDataSchema): string =>  {
  return globalData.team_members.filter((item) => item.id == userId)[0].name
}
