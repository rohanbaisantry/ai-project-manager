import React, { useState, useEffect } from 'react';
import { Button, TextField, Box, Typography, Switch } from '@mui/material';
import { GlobalUserDetails } from '../types';

export const AuthComponent = ({ setGlobalUserData }: {setGlobalUserData: (globalCompanyDetails: GlobalUserDetails) => void}) => {

  const login = useMutation(member => {
    return fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(member),
    });
  }, {
    onSuccess: () => {
      queryClient.invalidateQueries('login')
      handleClose();
    },
  });

  const signup`` = useMutation(member => {
    return fetch('/signup`', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(member),
    });
  }, {
    onSuccess: () => {
      queryClient.invalidateQueries('login')
      handleClose();
    },
  });


  const [isLogin, setIsLogin] = useState(false);
  const [userDetails, setUserDetails] = useState({
    name: '',
    mobile: '',
    companyName: '',
  });

  // Attempt auto-login if mobile number exists in local storage
  useEffect(() => {
    const mobile = localStorage.getItem('mobile');
    if (mobile) {
      login({ mobile });
    }
  }, []);

  const handleChange = (e: any) => {
    const { name, value } = e.target;
    setUserDetails(prevDetails => ({
      ...prevDetails,
      [name]: value,
    }));
  };

  const handleSubmit = async () => {
    if (isLogin) {
      login(userDetails);
    } else {
      signup(userDetails);
    }
  };

  const login = async (details: any) => {
    localStorage.setItem('mobile', details.mobile);
    const globalCompanyDetails = "RESPONSE FROM LOGIN API"
    setGlobalUserData(globalCompanyDetails);
  };
  const signup = async (details: any) => {
    localStorage.setItem('mobile', details.mobile);
    const globalCompanyDetails = "RESPONSE FROM SIGNUP API"
    setGlobalUserData(globalCompanyDetails);
  };

  return (
    <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" height="100vh">
      <Typography variant="h5">{isLogin ? 'Login' : 'Signup'}</Typography>
      {!isLogin && (
        <TextField
        required
          label="Name"
          variant="outlined"
          value={userDetails.name}
          onChange={handleChange}
          name="name"
          margin="normal"
        />
      )}
      <TextField
      required
        label="Mobile Number"
        variant="outlined"
        value={userDetails.mobile}
        onChange={handleChange}
        name="mobile"
        margin="normal"
        type="tel"
      />
      {!isLogin && (
        <TextField
        required
          label="Company Name"
          variant="outlined"
          value={userDetails.companyName}
          onChange={handleChange}
          name="companyName"
          margin="normal"
        />
      )}
      <Button onClick={handleSubmit} variant="contained" style={{ marginTop: '20px' }}>
        {!isLogin ? 'Signup' : 'Login'}
      </Button>
      <Typography variant="body1" style={{ marginTop: '20px' }}>
        Already have an account?
        <Switch checked={isLogin} onChange={() => setIsLogin(!isLogin)} />
      </Typography>
    </Box>
  );
};
