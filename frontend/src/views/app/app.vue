<template>
  <v-content id="app">
    <v-container fluid pa-0>
      <router-view name="head"></router-view>
    </v-container>
    <v-container fluid align-space-between pa-0
            row
            fill-height>
      <router-view name="content"></router-view>
    </v-container>
    <v-container fluid>
      <router-view name='footer'></router-view>
    </v-container>
  </v-content>
</template>

<script>
</script>

<style  lang='scss'>
</style>
