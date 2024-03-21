import React, { useState, useEffect } from 'react';
import { Box, Container, Tab, Tabs, Typography } from '@mui/material';
import { TasksTab } from './TasksTab';
import { TeamMembersTab } from './components/TeamMembersTab';
import { useQuery } from 'react-query';

export default App = () => {
  const [currentTab, setCurrentTab] = useState(0);
  const [companyData, setCompanyData] = useState(null);

  // Assuming `companyId` is globally available or retrieved from user session
  const companyId = 'someCompanyId';

  const { data, isLoading } = useQuery('companyData', () =>
    fetch(`/data/${companyId}`).then(res => res.json())
  );

  useEffect(() => {
    if (data) setCompanyData(data);
  }, [data]);

  if (isLoading) return <div>Loading...</div>;

  const handleTabChange = (event, newValue) => {
    setCurrentTab(newValue);
  };

  return (
    <Box sx={{ width: '100%' }}>
      <Container maxWidth="xl">
        <Typography gutterBottom variant='h5'>AI Project Manager</Typography>
      </Container>
      <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
        <Tabs value={currentTab} onChange={handleTabChange}>
          <Tab label="Tasks" />
          <Tab label="Team Members" />
        </Tabs>
      </Box>
      {currentTab === 0 && <TasksTab tasks={companyData?.tasks} />}
      {currentTab === 1 && <TeamMembersTab teamMembers={companyData?.team_members} />}
    </Box>
  );
};
