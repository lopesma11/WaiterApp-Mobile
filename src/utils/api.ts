import axios from "axios";

const api = axios.create({
    baseURL: process.env.EXPO_PUBLIC_API_URL ?? "http://192.168.0.15:3001",
});

export default api;
