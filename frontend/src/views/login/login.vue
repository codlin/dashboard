<template>
  <v-layout justify-center
            class="login_bg">
    <v-flex xs4>
      <v-container class="text-xs-center">
        <v-card flat>
          <v-card-title primary-title>
            <h4>Login</h4>
          </v-card-title>
          <v-form ref="form"
                  v-model="valid"
                  lazy-validation>
            <v-text-field prepend-icon="person"
                          v-model="username"
                          :rules="nameRules"
                          :counter="16"
                          label="Username"
                          required></v-text-field>
            <v-text-field prepend-icon="lock"
                          v-model="password"
                          :rules="passwordRules"
                          label="Password"
                          type="password"
                          required></v-text-field>
            <v-card-actions>
              <v-btn primary
                     large
                     block
                     :disabled="!valid"
                     @click="login">
                Login
              </v-btn>
            </v-card-actions>
          </v-form>
        </v-card>
      </v-container>
    </v-flex>
  </v-layout>
</template>

<script>
import cookie from '../../static/js/cookie.js'

export default {
  created () {
    // clear cache
    cookie.delCookie('token')
    cookie.delCookie('name')

    // update store data
    this.$store.dispatch('setUserInfo')
  },

  data () {
    return {
      username: '',
      password: '',
      autoLogin: false,
      error: false,
      usernameError: '',
      passwordError: '',

      valid: true,
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must <= 10 characters'
      ],
      passwordRules: [
        v => !!v || 'Password is required',
        v => (v && v.length <= 16) || 'Name must <= 16 characters'
      ]
    }
  },

  methods: {
    login () {
      if (this.$refs.form.validate()) {
        this.$api.post(
          '/login',
          {
            username: this.username,
            password: this.password
          },
          r => {
            console.log(r)
            // store user info in local
            cookie.setCookie('name', this.username, 7)
            cookie.setCookie('token', r.data.token, 7)

            // update store
            this.$store.dispatch('setUserInfo')

            // jump to homepage
            this.$router.push({ name: 'root' })
          },
          r => {
            console.log('Failed: ', r)
            // if ('non_field_errors' in error) {
            //   that.error = error.non_field_errors[0]
            // }
            // if ('username' in error) {
            //   that.usernameError = error.username[0]
            // }
            // if ('password' in error) {
            //   that.parseWordError = error.password[0]
            // }
          }
        )
      }
    },

    clear () {
      this.$refs.form.reset()
    }
    // for testing
  }
}
</script>

<style lang='scss' scoped>
.login_bg {
  background-color: #f5f5f5;
  // background-image: url('http://cdn.wallpapersafari.com/7/86/gqiGH7.jpg');
  background-size: cover;
  overflow: hidden;
}
</style>
