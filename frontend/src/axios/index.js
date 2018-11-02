import axios from 'axios'

// 全局状态控制引入
import store from '../store/index'

// http request interceptor
axios.interceptors.request.use(
  config => {
    console.log(store)
    if (store.state.user.userInfo.token) {
      // 判断是否存在token，如果存在的话，则每个http header都加上token
      config.headers.Authorization = `JWT ${store.state.user.userInfo.token}`
    }
    return config
  },
  err => {
    return Promise.reject(err)
  }
)

// http response interceptor
// axios.interceptors.response.use(undefined, error => {
//   let res = error.response
//   switch (res.status) {
//     case 401:
//       console.log('Not login or token expire.')
//       break
//     case 403:
//       console.log('you have not permission.')
//       break
//     case 500:
//       console.log('Server error.')
//       break
//   }
//   return Promise.reject(error.response.data)
// })
