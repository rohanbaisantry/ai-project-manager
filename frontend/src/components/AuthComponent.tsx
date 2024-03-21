import React, { useState, useEffect } from 'react';
import { Button, TextField, Box, Typography, Switch } from '@mui/material';
import { GlobalUserDetails } from '../types';

export const AuthComponent = ({ setGlobalUserData }: {setGlobalUserData: (globalCompanyDetails: GlobalUserDetails) => void}) => {
  const [isSignup, setIsSignup] = useState(false);
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

  const toggleForm = () => {
    setIsSignup(!isSignup);
  };

  const handleSubmit = async () => {
    if (isSignup) {
      // Handle signup
      // Ideally, you'd send 'name', 'mobile', 'companyName' to your signup endpoint
      console.log('Signup details:', userDetails);
    } else {
      // Handle login
      login(userDetails);
    }
  };

  const login = async (details: any) => {
    console.log('Logging in with:', details);
    localStorage.setItem('mobile', details.mobile);
    const globalCompanyDetails = {
      "user": {
        "id": "5eb7cf5a86d9755df3a6c593",
        "name": "string",
        "role": "string",
        "mobile": "string",
        "chats": [
          {
            "content": "string",
            "sent_by": "USER",
            "sent_at": "2024-03-21T13:14:09.238Z"
          }
        ],
        "company": {
          "id": "5eb7cf5a86d9755df3a6c593",
          "name": "string"
        },
        "company_id": "5eb7cf5a86d9755df3a6c593"
      },
      "company": {
        "id": "5eb7cf5a86d9755df3a6c593",
        "name": "string"
      },
      "team_members": [
        {
          "id": "5eb7cf5a86d9755df3a6c593",
          "name": "string",
          "role": "string",
          "mobile": "string",
          "chats": [
            {
              "content": "string",
              "sent_by": "USER",
              "sent_at": "2024-03-21T13:14:09.239Z"
            }
          ],
          "company": {
            "id": "5eb7cf5a86d9755df3a6c593",
            "name": "string"
          },
          "company_id": "5eb7cf5a86d9755df3a6c593"
        }
      ],
      "tasks": [
        {
          "id": "5eb7cf5a86d9755df3a6c593",
          "name": "string",
          "description": "string",
          "start_datetime": "2024-03-21T13:14:09.239Z",
          "due_datetime": "2024-03-21T13:14:09.239Z",
          "next_follow_up_datetime": "2024-03-21T13:14:09.239Z",
          "comments": [
            "string"
          ],
          "assignee": {
            "id": "5eb7cf5a86d9755df3a6c593",
            "name": "string",
            "role": "string",
            "mobile": "string",
            "chats": [
              {
                "content": "string",
                "sent_by": "USER",
                "sent_at": "2024-03-21T13:14:09.239Z"
              }
            ],
            "company": {
              "id": "5eb7cf5a86d9755df3a6c593",
              "name": "string"
            },
            "company_id": "5eb7cf5a86d9755df3a6c593"
          },
          "assignee_id": "5eb7cf5a86d9755df3a6c593",
          "company": {
            "id": "5eb7cf5a86d9755df3a6c593",
            "name": "string"
          },
          "company_id": "5eb7cf5a86d9755df3a6c593",
          "is_completed": true
        }
      ]
    };
    setGlobalUserData(globalCompanyDetails);
  };

  return (
    <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" height="100vh">
      <Typography variant="h5">{isSignup ? 'Signup' : 'Login'}</Typography>
      {isSignup && (
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
      {isSignup && (
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
        {isSignup ? 'Signup' : 'Login'}
      </Button>
      <Typography variant="body1" style={{ marginTop: '20px' }}>
        {isSignup ? 'Already have an account?' : "Don't have an account?"}
        <Switch checked={isSignup} onChange={toggleForm} />
      </Typography>
    </Box>
  );
};
