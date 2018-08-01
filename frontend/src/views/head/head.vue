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
               to="/crt">
          <span>Home</span>
        </v-btn>
        <v-btn flat
               to="/loads">
          <span>Loads</span>
        </v-btn>
        <v-btn flat
               to="/testline">
          <span>TLs</span>
        </v-btn>
        <v-btn flat
               to="/cases">
          <span>Cases</span>
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>
  </v-toolbar>
</template>

<script>
export default {}
</script>
