import React, { useState } from 'react';
import {
  Box,
  Button,
  Card,
  CardContent,
  Typography,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  TextField,
  Select,
  MenuItem,
  InputLabel,
  FormControl,
} from '@mui/material';
import { useMutation, useQueryClient } from 'react-query';
import { getTeamMemberNameFromId } from '../utils';
import { CompanyGlobalDataSchema, CreateTaskEntity, TaskSchema, UpdateTaskEntity } from '../types'; // Import types
import { useCreateTaskMutation, useEditTaskMutation } from '../api'; // Import API functions

export const TasksTab = ({ globalCompanyDetails }: { globalCompanyDetails: CompanyGlobalDataSchema }) => {
  const { tasks, team_members: teamMembers } = globalCompanyDetails;
  const [open, setOpen] = useState(false);
  const [currentTask, setCurrentTask] = useState<TaskSchema | null>(null);
  const [isAdding, setIsAdding] = useState(false);
  const queryClient = useQueryClient();

  const createTaskMutation = useCreateTaskMutation({
    onSuccess: () => {
      queryClient.invalidateQueries('login');
      handleClose();
    },
  });

  const editTaskMutation = useEditTaskMutation({
    onSuccess: () => {
      queryClient.invalidateQueries('login');
      handleClose();
    },
  });

  const handleOpen = (task: TaskSchema | null = null) => {
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
      if (isAdding) {
        createTaskMutation.mutate(currentTask as CreateTaskEntity); // Assert currentTask as CreateTaskEntity
      } else {
        editTaskMutation.mutate({ taskId: currentTask.id, data: currentTask as UpdateTaskEntity }); // Assert currentTask as UpdateTaskEntity
      }
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | { name?: string; value: unknown }>) => {
    const { name, value } = e.target;
    setCurrentTask({ ...currentTask!, [name as string]: value }); // Asserting name as string
  };

  return (
    <Box>
      <Button fullWidth onClick={() => handleOpen()} variant="contained" style={{ marginBottom: '20px' }}>
        Add A New Task
      </Button>
      {tasks.map((task, index) => (
        <Card
          key={index}
          sx={{ marginBottom: '20px', cursor: 'pointer' }}
          onClick={() => handleOpen(task)}
          elevation={2}
        >
          <CardContent>
            <Typography variant="h5">{task.name}</Typography>
            <Typography color="text.secondary">Start: {task.start_datetime}</Typography>
            <Typography color="text.secondary">
              Next Follow Up: {task.next_follow_up_datetime}
            </Typography>
            <Typography color="text.secondary">Due: {task.due_datetime}</Typography>
            <Typography color="text.secondary">
              Assignee: {getTeamMemberNameFromId(task.assignee_id, globalCompanyDetails)}
            </Typography>
          </CardContent>
        </Card>
      ))}
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>{isAdding ? 'Add New Task' : 'Edit Task'}</DialogTitle>
        <DialogContent>
          <TextField
            autoFocus
            margin="dense"
            name="name"
            label="Name"
            type="text"
            fullWidth
            variant="outlined"
            value={currentTask?.name || ''}
            onChange={handleChange}
          />
          <TextField
            margin="dense"
            name="description"
            label="Description"
            type="text"
            fullWidth
            multiline
            rows={4}
            variant="outlined"
            value={currentTask?.description || ''}
            onChange={handleChange}
          />
          {/* Start Datetime */}
          <TextField
            margin="dense"
            name="start_datetime"
            label="Start Datetime"
            type="datetime-local"
            fullWidth
            variant="outlined"
            value={currentTask?.start_datetime || ''}
            onChange={handleChange}
          />
          {/* Due Datetime */}
          <TextField
            margin="dense"
            name="due_datetime"
            label="Due Datetime"
            type="datetime-local"
            fullWidth
            variant="outlined"
            value={currentTask?.due_datetime || ''}
            onChange={handleChange}
          />
          {/* Next Follow Up Datetime */}
          <TextField
            margin="dense"
            name="next_follow_up_datetime"
            label="Next Follow Up Datetime"
            type="datetime-local"
            fullWidth
            variant="outlined"
            value={currentTask?.next_follow_up_datetime || ''}
            onChange={handleChange}
          />
          {/* Assignee Dropdown */}
          <FormControl fullWidth margin="dense">
            <InputLabel id="assignee-select-label">Assignee</InputLabel>
            <Select
              labelId="assignee-select-label"
              id="assignee-select"
              name="assignee_id"
              value={currentTask?.assignee_id || ''}
              onChange={handleChange}
              label="Assignee"
            >
              {teamMembers.map((member) => (
                <MenuItem key={member.id} value={member.id}>
                  {member.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
          {/* ... other fields ... */}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleSave}>Save</Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
};
