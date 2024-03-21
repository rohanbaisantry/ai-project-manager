import { GlobalUserDetails } from "./types";

export const getTeamMemberNameFromId = (userId: string, globalData: GlobalUserDetails): string =>  {
  return globalData.team_members.filter((item) => item.id == userId)[0].name
}
