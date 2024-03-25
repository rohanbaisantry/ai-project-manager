import React, { useState, useEffect } from 'react';
import { Button, TextField, Box, Typography, Switch } from '@mui/material';
import { CompanyGlobalDataSchema, SignupEntity } from '../types'; // Import types
import { useSignupMutation, useLoginMutation } from '../api'; // Import API functions

export const AuthComponent = ({ setGlobalUserData }: { setGlobalUserData: (globalUserDetails: CompanyGlobalDataSchema) => void }) => {
  const [isLogin, setIsLogin] = useState(false);
  const [userDetails, setUserDetails] = useState<SignupEntity>({
    user_name: '',  // Updated field name from 'name' to 'user_name'
    user_mobile: '', // Updated field name from 'mobile' to 'user_mobile'
    company_name: '',
  }); // Use SignupEntity type

  const signupMutation = useSignupMutation({
    onSuccess: (data) => {
      // Handle successful signup
      localStorage.setItem('mobile', data.user.mobile); // Updated to use 'user_mobile'
      setGlobalUserData(data); // Assuming API response matches GlobalUserDetails
    },
  });

  const loginMutation = useLoginMutation({
    onSuccess: (data) => {
      // Handle successful login
      localStorage.setItem('mobile', data.user.mobile); // Updated to use 'user_mobile'
      setGlobalUserData(data); // Assuming API response matches GlobalUserDetails
    },
  });

  // Attempt auto-login if mobile number exists in local storage
  useEffect(() => {
    const mobile = localStorage.getItem('mobile');
    if (mobile) {
      loginMutation.mutate(mobile);
    }
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setUserDetails((prevDetails) => ({
      ...prevDetails,
      [name]: value,
    }));
  };

  const handleSubmit = async () => {
    if (isLogin) {
      loginMutation.mutate(userDetails.user_mobile); // Pass only mobile for login
    } else {
      signupMutation.mutate(userDetails);
    }
  };

  return (
    <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" height="100vh">
      <Typography variant="h5">{isLogin ? 'Login' : 'Signup'}</Typography>
      {!isLogin && (
        <TextField
          required
          label="Name"
          variant="outlined"
          value={userDetails.user_name} // Updated field name from 'name' to 'user_name'
          onChange={handleChange}
          name="user_name" // Updated field name from 'name' to 'user_name'
          margin="normal"
        />
      )}
      <TextField
        required
        label="Mobile Number"
        variant="outlined"
        value={userDetails.user_mobile} // Updated field name from 'mobile' to 'user_mobile'
        onChange={handleChange}
        name="user_mobile" // Updated field name from 'mobile' to 'user_mobile'
        margin="normal"
        type="tel"
      />
      {!isLogin && (
        <TextField
          required
          label="Company Name"
          variant="outlined"
          value={userDetails.company_name}
          onChange={handleChange}
          name="company_name"
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
