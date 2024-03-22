import React, { useState } from 'react';
import { AuthComponent } from './components/AuthComponent';
import { MainPageComponent } from './components/MainPage';
import { GlobalUserDetails } from './types';
import { Box, CircularProgress } from '@mui/material';
import { useQuery } from 'react-query';

function App() {
  const [globalUserData, setGlobalUserData] = useState<GlobalUserDetails | null>(null)
  const mobile = localStorage.get("mobile")

  // const {data, isFetching} = UseQuery function to the authenticate endpoint.

  return (
    <div>
      {isFetching ? <Box my={5} textAlign="center"><CircularProgress /></Box>: !data ? (
        <AuthComponent setGlobalUserData={setGlobalUserData} />
      ) : (
        <MainPageComponent companyData={data}/>
      )}
    </div>
  );
}

export default App;
