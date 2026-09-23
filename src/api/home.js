import axios from 'axios';

const base_url = 'http://localhost:8000/api/v1';

export default {

    getCards: (params) => {
        return axios.get(`${base_url}/cards`, {
            params: params
        })
    },
}