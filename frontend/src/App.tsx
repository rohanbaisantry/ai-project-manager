import React, { useState } from 'react';
import { AuthComponent } from './components/AuthComponent';
import { MainPageComponent } from './components/MainPage';
import { CompanyGlobalDataSchema } from './types';
import { Box, CircularProgress } from '@mui/material';
import { useAuthenticateQuery } from './api'; // Import API function

function App() {
  const [globalUserData, setGlobalUserData] = useState<CompanyGlobalDataSchema | null>(null);
  const mobile = localStorage.getItem("mobile");

  // Use the imported API function for authentication
  const { data, isFetching } = useAuthenticateQuery(mobile ?? "", {
    enabled: !!mobile, // Only fetch if mobile number exists
    onSuccess: (data) => setGlobalUserData(data), // Update state on success
  });

  return (
    <div>
      {isFetching ? (
        <Box my={5} textAlign="center">
          <CircularProgress />
        </Box>
      ) : !data || !globalUserData ? (
        <AuthComponent setGlobalUserData={setGlobalUserData} />
      ) : (
        <MainPageComponent companyData={globalUserData} />
      )}
    </div>
  );
}

export default App;
