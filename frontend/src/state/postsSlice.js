import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    posts: [],
    anomalies: [],
    summary: {}
};
const postsSlice = createSlice({
  name: 'posts',
  initialState,
  reducers: {
    setPosts(state, action) {
    state.posts = action.payload;
    },
    setAnomalies(state, action) {
      state.anomalies = action.payload;
    },
    setSummary(state, action) {
      state.summary = action.payload;
    }
  }
});

export const { setPosts, setAnomalies, setSummary } = postsSlice.actions;
export default postsSlice.reducer;