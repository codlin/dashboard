let axios = require('axios')
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

// configure base URL

/*
  axios wrapper
*/
function apiAxios (method, url, params, success, failure) {
  axios({
    method: method,
    url: url,
    data: method === 'POST' || method === 'PUT' ? params : null,
    params: method === 'GET' || method === 'DELETE' ? params : null
  })
    .then(function (res) {
      console.log(res)
      if (res.status === 200 || res.status === 201) {
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
  }
}
