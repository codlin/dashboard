<template>
  <v-layout align-center style="height: 40px">
    <v-breadcrumbs id="breadcrums" style="height: 40px">
      <v-breadcrumbs-item v-for="item in breadcrums"
                          :disabled="item.disabled"
                          :key="item.text"
                          :to="item.path">
        {{ item.text }}
      </v-breadcrumbs-item>
    </v-breadcrumbs>
    <v-chip small
            disabled
            v-for="item in relatedChips"
            :key="item.text">
      <router-link :to="item.path">{{ item.text }}</router-link>
    </v-chip>
  </v-layout>
</template>

<script>
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

export default {
  computed: {
    breadcrums () {
      return this.$store.getters.breadCrums
    },

    relatedChips () {
      return this.$store.getters.relatedChips
    }

  }
}
</script>
