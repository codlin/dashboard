import Vue from 'vue'
import Router from 'vue-router'

import app from '../views/app/app'
import Head from '../views/head/head'
import footer from '../views/footer/footer'

import login from '../views/login/login'

import index from '../views/loads/index'
import loadsByProduct from '../views/loads/loads'
import loadTLs from '../views/loads/loadtestlines'
import loadCases from '../views/loads/loadcases'

import testline from '../views/testline/testlines'

// const index = () => import('../views/loads/index')
// const loadsByProduct = () => import('../views/loads/loads')
// const loadTLs = () => import('../views/loads/loadtestlines')
// const loadCases = () => import('../views/loads/loadcases')

Vue.use(Router)

// UI Components related
// breadcrumbs navigation
// var routeList = []

var router = new Router({
  routes: [
    {
      path: '/',
      name: 'root',
      component: app,
      meta: {
        title: 'CRT Dashboard'
      },
      children: [
        {
          path: 'login',
          name: 'login',
          components: {
            head: Head,
            content: login,
            footer: footer
          },
          meta: {
            title: 'CRT Dashboard | Login'
          }
        },
        {
          path: 'crt',
          name: 'crt',
          components: {
            head: Head,
            footer: footer
          },
          meta: {
            title: 'CRT Dashboard'
          }
        },
        {
          path: 'loads',
          name: 'loads',
          components: {
            head: Head,
            content: index,
            footer: footer
          },
          meta: {
            title: 'CRT Dashboard'
          },
          children: [
            {
              path: 'index/:productId',
              name: 'index',
              component: loadsByProduct,
              props: true,
              meta: {
                title: 'CRT Dashboard'
              }
            },
            {
              path: 'index/:loadName/tls',
              name: 'loadtls',
              component: loadTLs,
              props: true,
              meta: {
                title: 'CRT Dashboard'
              }
            },
            {
              path: 'index/:loadName/cases',
              name: 'loadcases',
              component: loadCases,
              props: true,
              meta: {
                title: 'CRT Dashboard'
              }
            }
          ]
        },
        {
          path: 'testline',
          name: 'testline',
          components: {
            head: Head,
            content: testline,
            footer: footer
          },
          meta: {
            title: 'CRT Dashboard'
          }
        },
        {
          path: 'case',
          name: 'case',
          components: {
            head: Head,
            content: testline,
            footer: footer
          },
          meta: {
            title: 'CRT Dashboard'
          }
        }
      ]
    }
  ]
})

router.beforeEach((to, from, next) => {
  console.log('route from', from)
  console.log('route to', to)
  if (to.path === '/' || to.path === '/crt') {
    next({ path: '/loads' })
  } else if (to.matched.length === 0) {
    // if no route was mathec
    from.name ? next({ name: from.name }) : next('/')
  } else {
    next()
  }
})

router.afterEach((to, from, next) => {
  document.title = to.matched[to.matched.length - 1].meta.title
})

export default router
