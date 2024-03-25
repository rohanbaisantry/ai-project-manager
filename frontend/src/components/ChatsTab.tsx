import React, { useState } from 'react';
import { Box, Grid, List, ListItem, ListItemText, Divider, Card, CardContent, Typography, TextField, Button, ListItemButton } from '@mui/material';
import { useNewChatReceivedMutation } from '../api'; // Import API function
import { CompanyGlobalDataSchema, UserSchema } from '../types';

export const ChatsTab = ({ globalCompanyDetails }: { globalCompanyDetails: CompanyGlobalDataSchema }) => {
  const { team_members: teamMembers } = globalCompanyDetails;
  const [selectedMember, setSelectedMember] = useState<UserSchema | null>(null);
  const [newMessage, setNewMessage] = useState('');

  // Use imported API function for sending chat messages
  const { mutate: sendNewChat } = useNewChatReceivedMutation({
    onSuccess: () => {
      // You might want to refetch the conversation or update it locally here
    },
  });

  const handleSendMessage = async () => {
    if (!selectedMember) return; // Ensure a member is selected

    await sendNewChat({
      userId: selectedMember.id,
      data: { content: newMessage },
    });

    setNewMessage(''); // Reset input field after sending
  };

  return (
    <Grid container spacing={2}>
      <Grid item xs={6}>
        <List component="nav">
          {teamMembers.map((member, index) => (
            <ListItemButton key={index} onClick={() => setSelectedMember(member)} selected={selectedMember?.id === member.id}>
              <ListItemText primary={member.name} />
            </ListItemButton>
          ))}
        </List>
      </Grid>
      <Grid item xs={6}>
        <Box
          sx={{
            maxHeight: '70vh',
            overflow: 'auto',
            marginBottom: '20px',
          }}
        >
          {selectedMember ? (
            selectedMember.chats.map((chat, index) => (
              <Card key={index} sx={{ marginBottom: '10px' }}>
                <CardContent>
                  <Typography color="textSecondary" gutterBottom>
                    {chat.sent_by} - {new Date(chat.sent_at).toLocaleString()}
                  </Typography>
                  <Typography variant="body2">{chat.content}</Typography>
                </CardContent>
              </Card>
            ))
          ) : (
            <Typography variant="body2">Select A Conversation</Typography>
          )}
        </Box>
        <Divider />
        <Box
          component="form"
          sx={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            marginTop: '20px',
          }}
          noValidate
          autoComplete="off"
        >
          <TextField
            id="outlined-basic-email"
            label="Type a message"
            fullWidth
            variant="outlined"
            value={newMessage}
            onChange={(e) => setNewMessage(e.target.value)}
            sx={{ marginRight: '20px' }}
          />
          <Button variant="contained" color="primary" onClick={handleSendMessage}>
            Send
          </Button>
        </Box>
      </Grid>
    </Grid>
  );
};
