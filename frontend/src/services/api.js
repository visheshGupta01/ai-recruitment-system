import axios from "axios";

const api = axios.create({
  baseURL: "https://ai-recruitment-system-1-486q.onrender.com/",
});

export default api;