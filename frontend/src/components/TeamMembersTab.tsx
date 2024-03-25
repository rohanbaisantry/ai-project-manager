import React, { useState } from 'react';
import { Box, Button, Dialog, DialogActions, DialogContent, DialogTitle, TextField, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import { useCreateTeamMemberMutation } from '../api'; // Import API function
import { CompanyGlobalDataSchema, CreateTeamMemberEntity } from '../types';

export const TeamMembersTab = ({ globalCompanyDetails }: { globalCompanyDetails: CompanyGlobalDataSchema }) => {
  const { team_members: teamMembers, company: company } = globalCompanyDetails;
  const [open, setOpen] = useState(false);
  const [currentMember, setCurrentMember] = useState<CreateTeamMemberEntity>({name: "", mobile: ""});

  // Use imported API function for creating team members
  const { mutate: createTeamMember } = useCreateTeamMemberMutation({
    onSuccess: () => {
      // You might want to refetch the team members list or update it locally here
      handleClose(); // Close the dialog after successful creation
    },
  });

  const handleOpen = (member: CreateTeamMemberEntity = {name: "", mobile: ""}) => {
    setCurrentMember(member);
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
    setCurrentMember({name: "", mobile: ""});
  };

  const handleSave = () => {
    createTeamMember({ companyId: company.id, data: currentMember });
  };

  const handleChange = (e: { target: { name: any; value: any; }; }) => {
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
              <TableRow key={row.name} hover onClick={() => handleOpen(row)} sx={{ cursor: 'pointer' }}>
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
