<template>
  <v-layout id="testlines"
            fill-height>
    <v-content>
      <v-card flat>
        <v-toolbar flat
                   color="white">
          <v-toolbar-title>Details</v-toolbar-title>
          <v-divider class="mx-2"
                     inset
                     vertical></v-divider>
          <v-btn icon
                 @click="refreshData">
            <v-icon>refresh</v-icon>
          </v-btn>

          <v-spacer></v-spacer>
          <v-content>
            <v-layout align-center
                      justify-start>
              <v-checkbox hide-details
                          v-model="productChkbox"
                          v-for="product in products"
                          :key="product.name"
                          :label="product.text"
                          :value="product.name"></v-checkbox>
            </v-layout>
          </v-content>
          <v-text-field v-model="item_search"
                        append-icon="search"
                        label="Search"
                        single-line
                        hide-details></v-text-field>
        </v-toolbar>

        <v-data-table :pagination.sync="pagination"
                      :headers="tblHeaders"
                      :items="filteredItems"
                      :search="item_search"
                      :class="['text-xs-left']"
                      hide-actions>
          <template slot="items"
                    slot-scope="props">
            <tr>
              <td>{{ props.item.mode }}</td>
              <td>{{ props.item.sitetype }}</td>
              <td>{{ props.item.node }}</td>
              <td>{{ props.item.btsid }}</td>
              <td>{{ props.item.ca }}</td>
              <td>{{ props.item.jenkinsjob }}</td>
              <td>{{ props.item.mbtsid }}</td>
              <td>{{ props.item.mnode }}</td>
            </tr>
          </template>
          <v-alert slot="no-results"
                   :value="true"
                   color="error"
                   icon="warning">
            Your search for "{{ item_search }}" found no results.
          </v-alert>
        </v-data-table>
      </v-card>
    </v-content>
  </v-layout>
</template>

<script>
import { getTimestamp } from '../../../static/js/utils.js'

export default {
  created () {
    this.getProducts()
  },

  data () {
    return {
      // json data retrieved from server
      products: [],

      testlines: [],

      tblHeaders: [
        { text: 'Mode', align: 'left', value: 'mode' },
        { text: 'Site Type', align: 'left', value: 'sitetype' },
        { text: 'Jenkins Node', align: 'left', value: 'node' },
        { text: 'BTSID', align: 'left', value: 'btsid' },
        { text: 'CA', align: 'left', value: 'ca' },
        { text: 'Jenkins Job', align: 'left', value: 'jenkinsjob' },
        { text: 'Mobility BTSID', align: 'left', value: 'mbtsid' },
        { text: 'Mobility Node', align: 'left', value: 'mnode' }
      ],

      // vars from json data which will be used in the template

      // table data
      item_search: '',
      // sorting by descending
      pagination: { sortBy: 'mode', descending: true, rowsPerPage: -1 },

      // UI Components related
      productChkbox: null
    }
  },

  computed: {
    filteredItems () {
      let filteredData = this.testlines
      if (this.productChkbox !== null) {
        filteredData = filteredData.filter((item, i) => {
          let mode = item.mode
          return (this.productChkbox.indexOf(mode) !== -1)
        })
      }

      console.log('filter data: ', filteredData)
      return filteredData
    }
  },

  watch: {
    /** Watch route changing, beacuse the current view was bound by many URLs, but the created() function
     * only be executed once when it loaded. In the Vue documnet: "...the same component instance will be
     * reused. Since both routes render the same component, this is more efficient than destroying the old
     * instance and then creating a new one. However, this also means that the lifecycle hooks of the component
     * will not be called."
     * So we should watch $route for reacting URLs' changing
     **/
    $route () {
      this.getTestlines()
    }
  },

  methods: {
    getProducts () {
      console.log(getTimestamp(), 'Enter getProducts:')
      if (this.products.length > 0) {
        console.log('product already exist.')
        return
      }

      this.$api.get('/api/products', null,
        r => {
          this.products = r.data
          console.log(getTimestamp(), 'getProducts: get result', this.products)
        },
        r => {
          console.log('Failed: ', r)
        })

      console.log(getTimestamp(), 'Leave getProducts')
    },

    getTestlines () {
      this.$api.get('/api/testlines', null,
        r => {
          this.testlines = r.data
          console.log(getTimestamp(), 'getTestlines: ', this.testlines)
        },
        r => {
          console.log('Failed: ', r)
        })
    },

    refreshData () {
      console.log(this.productChkbox)
    }

    // for testing
  }
}
</script>

<style lang="scss" scoped>
// .v-tabs__div {
//   text-transform: none;
//   font-size: 12px;
// }
</style>
