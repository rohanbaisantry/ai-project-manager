import React, { useState } from 'react';
import { Box, Button, Dialog, DialogActions, DialogContent, DialogTitle, TextField, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import { useMutation, useQueryClient } from 'react-query';
import { GlobalUserDetails } from '../types';

export const TeamMembersTab = ({ globalCompanyDetails }: {globalCompanyDetails: GlobalUserDetails}) => {
  const {team_members: teamMembers} = globalCompanyDetails
  const [open, setOpen] = useState(false);
  const [currentMember, setCurrentMember] = useState({});
  const queryClient = useQueryClient();

  const mutation = useMutation(member => {
    return fetch('/team-member', {
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

  const handleOpen = (member = {}) => {
    setCurrentMember(member);
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
    setCurrentMember({});
  };

  const handleSave = () => {
    if (currentMember) {
      mutation.mutate(currentMember);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCurrentMember({ ...currentMember, [name]: value });
  };

  return (
    <Box>
      <Button fullWidth onClick={() => handleOpen()} variant="contained" style={{ marginBottom: '20px' }}>
        Add A New Team Member
      </Button>
      <TableContainer component={Paper}>
        <Table aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell align="right">Role</TableCell>
              <TableCell align="right">Mobile</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {teamMembers.map((row) => (
              <TableRow key={row.name} hover onClick={() => handleOpen(row)}>
                <TableCell component="th" scope="row">
                  {row.name}
                </TableCell>
                <TableCell align="right">{row.role}</TableCell>
                <TableCell align="right">{row.mobile}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>{currentMember.name ? 'Edit Team Member' : 'Add Team Member'}</DialogTitle>
        <DialogContent>
          <TextField autoFocus margin="dense" name="name" label="Name" type="text" fullWidth variant="outlined" value={currentMember.name || ''} onChange={handleChange} />
          <TextField margin="dense" name="mobile" label="Mobile" type="tel" fullWidth variant="outlined" value={currentMember.mobile || ''} onChange={handleChange} />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleSave}>Save</Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
};
