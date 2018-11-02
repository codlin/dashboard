import cookie from '../../static/js/cookie'

// mutations type
const SET_USERINFO = 'SET_USERINFO'

// state
const userInfo = {
  name: cookie.getCookie('name') || '',
  token: cookie.getCookie('token') || ''
}
const state = {
  userInfo
}

// getters
const getters = {
  userInfo: state => {
    return state.userInfo
  }
}

// mutations
const mutations = {
  [SET_USERINFO] (state, obj) {
    state.userInfo = {
      name: cookie.getCookie('name'),
      token: cookie.getCookie('token')
    }
    console.log(state.userInfo)
  }
}

// actions
function makeAction (type) {
  return ({ commit }, ...args) => commit(type, ...args)
}
const actions = {
  setUserInfo: makeAction(SET_USERINFO)
}

export default {
  state,
  getters,
  mutations,
  actions
}
