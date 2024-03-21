import React, { useState } from 'react';
import { Button, TextField, Box } from '@mui/material';
import { useMutation } from 'react-query';

export const LoginComponent = ({ onLoginSuccess }) => {
  const [mobile, setMobile] = useState('');

  const mutation = useMutation(mobile => {
    return fetch('/auth', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ mobile }),
    });
  });

  const handleLogin = async () => {
    try {
      const data = await mutation.mutateAsync(mobile);
      if (data.ok) onLoginSuccess();
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  return (
    <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" height="100vh">
      <TextField
        label="Mobile Number"
        variant="outlined"
        value={mobile}
        onChange={(e) => setMobile(e.target.value)}
        type="tel"
      />
      <Button onClick={handleLogin} variant="contained" style={{ marginTop: '20px' }}>
        Login
      </Button>
    </Box>
  );
};
