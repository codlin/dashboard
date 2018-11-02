<template>
  <v-toolbar dark
             dense
             flat
             color="primary">
    <v-icon>apps</v-icon>
    <v-toolbar-title>CRT Dashboard</v-toolbar-title>
    <v-divider class="mx-2"
               inset
               vertical></v-divider>
    <v-toolbar-items>
      <v-btn flat
             v-for="item in sysMenuItems"
             :key="item.name"
             @click="toPage(item)">
        {{ item.text }}
      </v-btn>
    </v-toolbar-items>
    <v-spacer></v-spacer>
    <v-btn flat
           v-if="userInfo.name"
           @click="loginOut">Logout</v-btn>
    <v-btn flat
           v-else
           to="/login">Login</v-btn>
  </v-toolbar>
</template>

<script>
import { mapGetters } from 'vuex'
import cookie from '../../static/js/cookie.js'
export default {
  created () {
    this.getSysMenus()
  },

  data () {
    return {
      // json data retrieved from server
      sysMenus: []
    }
  },

  computed: {
    sysMenuItems () {
      return this.sysMenus
    },
    ...mapGetters({
      userInfo: 'userInfo'
    })
  },

  methods: {
    getSysMenus () {
      if (this.sysMenus.length > 0) {
        console.log('sysMenus already exist.')
        return
      }

      this.$api.get('/api/menu', { group: 'CRT' },
        r => {
          this.sysMenus = r.data
          console.log('getSysMenus result:', this.sysMenus)
        },
        r => {
          console.log('Failed: ', r)
        }
      )

      console.log('Leave getSysMenus')
    },

    loginOut () {
      cookie.delCookie('token')
      cookie.delCookie('name')
      this.$store.dispatch('setUserInfo')

      // 跳转到登录
      this.$router.push({ name: 'login' })
    },

    toPage (item) {
      this.$router.push({ name: item.name })
    }
  }
}
</script>
