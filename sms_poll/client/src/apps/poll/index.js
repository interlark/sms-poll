import { ChakraProvider, ColorModeScript, createLocalStorageManager, extendTheme } from "@chakra-ui/react"
import ReactDOM from "react-dom/client"
import App from "./App"

import axios from 'axios'
import React from "react"


if (process.env.NODE_ENV === 'development') {
  axios.defaults.baseURL = "http://localhost:5000"

  axios.interceptors.request.use(request => {
      console.log('request =>', request)
      return request
  }, error => {
      console.error('request error =>', error)
      return Promise.reject(error)
  })

  axios.interceptors.response.use(response => {
      console.log('response <=', response)
      return response
  }, error => {
      console.error('response error <=', error)
      return Promise.reject(error)
  })
}

const config = {
  initialColorMode: "dark",
  useSystemColorMode: false,
}

const theme = extendTheme({ config })
const manager = createLocalStorageManager("poll")
const root = ReactDOM.createRoot(document.getElementById("root"))
root.render(
  <ChakraProvider theme={theme} colorModeManager={manager}>
    <ColorModeScript initialColorMode={theme.config.initialColorMode} storageKey="poll-color-mode" />
    <App />
  </ChakraProvider>
)
