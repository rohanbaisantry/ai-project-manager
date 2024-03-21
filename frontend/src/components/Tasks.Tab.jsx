import React, { useState } from 'react';
import { Box, Button, Card, CardContent, Typography, Dialog, DialogActions, DialogContent, DialogTitle, TextField } from '@mui/material';
import { useMutation, useQueryClient } from 'react-query';

export const TasksTab = ({ tasks }) => {
  const [open, setOpen] = useState(false);
  const [currentTask, setCurrentTask] = useState(null);
  const [isAdding, setIsAdding] = useState(false);
  const queryClient = useQueryClient();

  const taskMutation = useMutation(task => {
    const url = task.id ? `/tasks/${task.id}` : `/tasks`; // Adjust API endpoint for create/update
    return fetch(url, {
      method: task.id ? 'PUT' : 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(task),
    });
  }, {
    onSuccess: () => {
      queryClient.invalidateQueries('tasks');
      handleClose();
    },
  });

  const handleOpen = (task = null) => {
    setIsAdding(!task);
    setCurrentTask(task);
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
    setCurrentTask(null);
  };

  const handleSave = () => {
    if (currentTask) {
      taskMutation.mutate(currentTask);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCurrentTask({ ...currentTask, [name]: value });
  };

  return (
    <Box>
      <Button onClick={() => handleOpen()} variant="contained" style={{ marginBottom: '20px' }}>
        Add Task
      </Button>
      {tasks.map((task, index) => (
        <Card key={index} sx={{ marginBottom: '20px' }} onClick={() => handleOpen(task)}>
          <CardContent>
            <Typography variant="h5">{task.name}</Typography>
            <Typography color="text.secondary">Start: {task.start_datetime}</Typography>
            <Typography color="text.secondary">Due: {task.due_datetime}</Typography>
            <Typography color="text.secondary">Assignee: {task.assignee_name}</Typography>
          </CardContent>
        </Card>
      ))}
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>{isAdding ? 'Add New Task' : 'Edit Task'}</DialogTitle>
        <DialogContent>
          <TextField autoFocus margin="dense" name="name" label="Name" type="text" fullWidth variant="outlined" value={currentTask?.name || ''} onChange={handleChange} />
          <TextField margin="dense" name="description" label="Description" type="text" fullWidth multiline rows={4} variant="outlined" value={currentTask?.description || ''} onChange={handleChange} />
          <TextField margin="dense" name="assignee_name" label="Assignee" type="text" fullWidth variant="outlined" value={currentTask?.assignee_name || ''} onChange={handleChange} />
          <TextField margin="dense" name="start_datetime" label="Start Date and Time" type="datetime-local" fullWidth variant="outlined" InputLabelProps={{ shrink: true }} value={currentTask?.start_datetime || ''} onChange={handleChange} />
          <TextField margin="dense" name="due_datetime" label="Due Date and Time" type="datetime-local" fullWidth variant="outlined" InputLabelProps={{ shrink: true }} value={currentTask?.due_datetime || ''} onChange={handleChange} />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleSave}>Save</Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
};
