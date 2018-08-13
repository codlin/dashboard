const SET_BREADCRUMS = 'SET_BREADCRUMS'
const SET_CHIPS = 'SET_CHIPS'

/** breadcrums item struct
 * {
 *   disabled: true/false
 *   text: ''
 *   path: ''
 * }
 * related chip struct
 * {
 *   text: ''
 *   path: ''
 * }
 **/
// state
const state = {
  breadcrums: [],
  relatedChips: []
}

// getters
const getters = {
  breadCrums: state => {
    return state.breadcrums
  },

  relatedChips: state => {
    return state.relatedChips
  }
}

// mutations
const mutations = {
  [SET_BREADCRUMS] (state, obj) {
    state.breadcrums = obj
  },
  [SET_CHIPS] (state, obj) {
    state.relatedChips = obj
  }
}

// actions
function makeAction (type) {
  return ({ commit }, ...args) => commit(type, ...args)
}
const actions = {
  setBreadcrumbs: makeAction(SET_BREADCRUMS),
  setrelatedChips: makeAction(SET_CHIPS)
}

export default {
  state,
  getters,
  mutations,
  actions
}