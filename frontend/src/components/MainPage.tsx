import React, { useState } from 'react';
import { Box, Container, Tab, Tabs, Typography } from '@mui/material';
import { TasksTab } from './TasksTab';
import { TeamMembersTab } from './TeamMembersTab';
import { GlobalUserDetails } from '../types';
import { ChatsTab } from './ChatsTab';

export const MainPageComponent = ({companyData}: {companyData: GlobalUserDetails}) => {
  const [currentTab, setCurrentTab] = useState(0);

  const handleTabChange = (event: any, newValue: React.SetStateAction<number>) => {
    setCurrentTab(newValue);
  };

  return (
    <Container maxWidth="xl">
      <Box my={3} textAlign="center"><Typography variant="h5" color="primary"> AI Project Manager</Typography></Box>
      <Box borderBottom={1} borderColor="divider" my={3}>
        <Tabs value={currentTab} onChange={handleTabChange} variant='fullWidth'>
          <Tab label="Tasks" />
          <Tab label="Team Members" />
          <Tab label="Conversations" />
        </Tabs>
      </Box>
      {currentTab === 0 && <TasksTab globalCompanyDetails={companyData} />}
      {currentTab === 1 && <TeamMembersTab globalCompanyDetails={companyData} />}
      {currentTab === 2 && <ChatsTab globalCompanyDetails={companyData} />}
    </Container>
  );
};
