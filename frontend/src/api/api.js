import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/';
const anomalies = 'anomalies/'
const posts = 'posts/'
const summary = 'summary/'

export const fetchAnomalies = async () => {
    const response = await axios.get(BASE_URL + anomalies);
    return response.data;
};

export const fetchPosts = async () => {
    const response = await axios.get(BASE_URL + posts);
    return response.data;
};

export const fetchSummary = async () => {
    const response = await axios.get(BASE_URL + summary);
    return response.data;
};

