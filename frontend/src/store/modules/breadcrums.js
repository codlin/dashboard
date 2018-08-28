import Vue from 'vue'
const SET_BREADCRUMS = 'SET_BREADCRUMS'
const PUSH_BREADCRUMS = 'PUSH_BREADCRUMS'
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

function findFirstIndex (el, obj) {
  return (
    el.disabled === obj.disabled && el.text === obj.text && el.path === obj.path
  )
}

// mutations
const mutations = {
  [SET_BREADCRUMS] (state, obj) {
    state.breadcrums = obj
  },
  [PUSH_BREADCRUMS] (state, obj) {
    let idx = state.breadcrums.findIndex(findFirstIndex, obj)
    if (idx === -1) {
      state.breadcrums.push(obj)
    } else {
      Vue.set(state.breadcrums, idx, obj)
    }
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
  pushBreadcrumbs: makeAction(PUSH_BREADCRUMS),
  setRelatedChips: makeAction(SET_CHIPS)
}

export default {
  state,
  getters,
  mutations,
  actions
}
