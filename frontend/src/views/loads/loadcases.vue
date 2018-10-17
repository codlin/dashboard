<template>
  <div>
    <v-card flat>
      <v-toolbar flat
                 color="white">
        <v-toolbar-title>Details</v-toolbar-title>
        <v-divider class="mx-2"
                   inset
                   vertical></v-divider>

        <v-spacer></v-spacer>
        <v-content>
          <v-layout align-center
                    justify-center>
            <v-checkbox hide-details
                        v-model="resultChkbox"
                        value="passed"
                        label="PASSED"></v-checkbox>
            <v-checkbox hide-details
                        v-model="resultChkbox"
                        value="failed"
                        label="FAILED"></v-checkbox>
            <v-checkbox hide-details
                        v-model="resultChkbox"
                        value="norun"
                        label="NORUN"></v-checkbox>
            <h4 align-center
                justify-center>Case Count: {{ filteredCaseNum }}</h4>
          </v-layout>
        </v-content>
        <v-spacer></v-spacer>
        <v-text-field v-model="items_search"
                      append-icon="search"
                      label="Search"
                      single-line
                      hide-details></v-text-field>
      </v-toolbar>

      <v-data-table :pagination.sync="pagination"
                    :headers="tblHeaders"
                    :items="filteredItems"
                    :search="items_search"
                    hide-actions>
        <template slot="items"
                  slot-scope="props">
          <td>
            <a :href="getFailedCaseUrl(props.item)"
               target="_blank">{{ props.item.casename }}</a>
          </td>
          <td>{{ props.item.btsid }}</td>
          <td>
            <a :href="getFailedCaseUrl(props.item)"
               target="_blank">{{ props.item.node }}</a>
          </td>
          <td>{{ props.item.result }}</td>
          <td>{{ props.item.suite }}</td>
        </template>

        <v-alert slot="no-results"
                 :value="true"
                 color="error"
                 icon="warning">
          Your search for "{{ items_search }}" found no results.
        </v-alert>
      </v-data-table>
    </v-card>
  </div>
</template>

<script>
export default {
  props: {
    loadName: {
      type: String,
      required: true
    }
  },

  created () {
    // get data from server
    this.getLoadCases()
    this.createBreadcrums()
  },

  data () {
    return {
      // json data retrieved from server
      cases: [],

      // header
      tblHeaders: [
        { key: 'casename', text: 'Case Name', align: 'left', value: 'casename' },
        { key: 'btsid', text: 'BTSID', align: 'left', value: 'btsid' },
        { key: 'node', text: 'Jenkins Node', align: 'left', value: 'node' },
        { key: 'result', text: 'RESULT', align: 'left', value: 'result' },
        { key: 'suite', text: 'SUITE', align: 'left', value: 'suite' }
      ],

      // table data
      items_search: '',
      // sorting by descending
      pagination: { sortBy: 'result', descending: false, rowsPerPage: -1 },

      // UI Components related
      resultChkbox: null
    }
  },

  computed: {
    filteredItems () {
      return this.filterItems()
    },

    filteredCaseNum: function () {
      return this.filterItems().length
    }
  },

  watch: {
    /** Watch route changing, beacuse the current view was bound by many URLs, but the created() function
     * only be executed once when loaded.The same component instance will be reused. Since both routes
     * render the same component, this is more efficient than destroying the old instance and then creating
     * a new one. However, this also means that the lifecycle hooks of the component will not be called.
     * So we should watch $route for reacting URLs' changing
     **/
    '$route' (to, from) {
      this.getLoadCases()
    }
  },

  methods: {
    createBreadcrums () {
      // create breadcrums
      this.$store.dispatch('pushBreadcrumbs',
        {
          disabled: false,
          text: this.loadName,
          path: '/loads/index/' + this.loadName + '/tls'
        }
      )

      // create related chips
      this.$store.dispatch('setRelatedChips', [
        {
          text: 'test lines',
          path: '/loads/index/' + this.loadName + '/tls'
        }
      ])
    },

    // get loads list
    getLoadCases () {
      console.log('Enter getLoadCases: ', this.loadName)
      this.$api.get('/api/loadcases', { name: this.loadName },
        res => {
          this.cases = res.data
        },
        er => {
          console.error('getLoadCases: ', er)
        })
    },

    getFailedCaseUrl (item) {
      var release = this.loadName
      release = release.substring(0, 3)
      var jenkins = ''
      var ip = item.node
      var falg = ip.indexOf('10.52') !== -1
      // console.log(ip.indexOf('10.52') !== -1)
      switch (release) {
        case 'FLF':
          if (falg === true) {
            jenkins = 'http://10.52.200.190'
          } else {
            jenkins = 'http://10.66.11.20:8085'
          }
          break
        case 'TLF':
          if (falg === true) {
            jenkins = 'http://10.52.200.190'
          } else {
            jenkins = 'http://10.66.11.20:8086'
          }
          break
        case 'FLC':
          jenkins = 'http://10.66.11.20:8087'
          break
        case 'TLC':
          jenkins = 'http://10.66.11.20:8088'
          break
      }
      var url = jenkins + '/computer/' + item.node
      return url
    },

    // UI Components related
    filterItems () {
      let filteredData = this.cases

      if (this.resultChkbox !== null) {
        filteredData = filteredData.filter((item, i) => {
          if (this.resultChkbox.toUpperCase() === 'FAILED') {
            return item.result.toUpperCase() === 'FAILED' || item.result.toUpperCase() === 'NOT ANALYZED'
          } else if (this.resultChkbox.toUpperCase() === 'PASSED') {
            return item.result.toUpperCase() === 'PASSED'
          } else if (this.resultChkbox.toUpperCase() === 'NORUN') {
            return item.result.toUpperCase() === 'NULL'
          }
        })
      }

      return filteredData
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
