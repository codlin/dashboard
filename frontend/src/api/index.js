// configure base URL
let host = 'https://135.252.122.189:8000/api'

let axios = require('axios')

/*
  axios wrapper
*/
function apiAxios (method, url, params, success, failure) {
  axios({
    method: method,
    url: url,
    data: method === 'POST' || method === 'PUT' ? params : null,
    params: method === 'GET' || method === 'DELETE' ? params : null,
    baseURL: host,
    withCredentials: false
  })
    .then(function (res) {
      if (res.data.success === true) {
        if (success) {
          success(res)
        }
      } else {
        if (failure) {
          failure(res)
        } else {
          console.error('error: ' + JSON.stringify(res.data))
        }
      }
    })
    .catch(function (err) {
      if (failure) {
        failure(err)
      } else {
        if (err) {
          console.error('api error: ' + err.response)
        }
      }
    })
}

// axios synchronous method
async function apiAxiosPromise (relativeURL, params) {
  try {
    let url = host + relativeURL
    if (params) {
      url += params
    }

    const response = await axios.get(url)
    console.log(response)
  } catch (error) {
    console.error(error)
  }
}

// return api function
export default {
  get: function (url, params, success, failure) {
    return apiAxios('GET', url, params, success, failure)
  },
  post: function (url, params, success, failure) {
    return apiAxios('POST', url, params, success, failure)
  },
  put: function (url, params, success, failure) {
    return apiAxios('PUT', url, params, success, failure)
  },
  delete: function (url, params, success, failure) {
    return apiAxios('DELETE', url, params, success, failure)
  },
  sync_get: (url, params, success, failure) => {
    apiAxiosPromise(url, params)
      .then(function (res) {
        if (res.data.success === true) {
          if (success) {
            success(res)
          }
        } else {
          if (failure) {
            failure(res)
          } else {
            console.error('error: ' + JSON.stringify(res.data))
          }
        }
      })
      .catch(function (err) {
        if (failure) {
          failure(err)
        } else {
          if (err) {
            console.error('api error: ' + err.response)
          }
        }
      })
  }
}
