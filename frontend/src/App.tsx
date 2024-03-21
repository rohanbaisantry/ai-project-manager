import React, { useState } from 'react';
import { AuthComponent } from './components/AuthComponent';
import { MainPageComponent } from './components/MainPage';
import { GlobalUserDetails } from './types';

function App() {
  const [globalUserData, setGlobalUserData] = useState<GlobalUserDetails | null>(null);

  return (
    <div>
      {!globalUserData ? (
        <AuthComponent setGlobalUserData={setGlobalUserData} />
      ) : (
        <MainPageComponent companyData={globalUserData}/>
      )}
    </div>
  );
}

export default App;
