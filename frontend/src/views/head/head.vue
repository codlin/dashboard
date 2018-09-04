<template>
  <v-toolbar dark
             dense
             flat
             color="primary"
             extended>
    <v-toolbar-side-icon></v-toolbar-side-icon>
    <v-toolbar-title>CRT Dashboard</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-btn flat>Login</v-btn>
    </v-toolbar-items>
    <v-toolbar dark
               dense
               flat
               color="primary"
               slot="extension">
      <v-toolbar-items>
        <v-btn flat
               v-for="item in sysMenuItems"
               :key="item.name"
               @click="toPage(item)">
          {{ item.text }}
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>
  </v-toolbar>
</template>

<script>
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
    }
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

    toPage (item) {
      this.$router.push({ name: item.name })
    }
  }
}
</script>
