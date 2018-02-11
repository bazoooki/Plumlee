import { cloneDeep } from 'lodash'
import axios from 'axios'

const { BASE_URL } = process.env.api

const api = axios.create({
  baseURL: `${BASE_URL}`,
  headers: cloneDeep(axios.defaults.headers),
  withCredentials: true
})

const pullPlayers = () => {
  return api.get('players/get')
}
const login = (data) => {
  return api.post('login', data)
}
const register = (data) => {
  return api.post('register', data)
}
const whoami = () => {
  return api.get('whoami')
}

export default {
  pullPlayers,
  login,
  register,
  whoami
}
