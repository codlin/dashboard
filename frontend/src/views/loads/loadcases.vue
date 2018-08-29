<template>
  <div>
    <v-card flat>
      <v-toolbar flat
                 color="white">
        <v-toolbar-title>Details</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-content>
          <v-layout align-center
                    justify-start>
            <v-checkbox hide-details
                        v-model="resultChkbox"
                        value="failed"
                        label="FAILED"></v-checkbox>
            <v-checkbox hide-details
                        v-model="resultChkbox"
                        value="na"
                        label="NA"></v-checkbox>
            <v-checkbox hide-details
                        v-model="resultChkbox"
                        value="exception"
                        label="EXCEPTION"></v-checkbox>

          </v-layout>
        </v-content>
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
                    :class="['text-xs-left']"
                    hide-actions>
        <template slot="items"
                  slot-scope="props">
          <tr>
            <td>
              <a href="http://10.52.200.190/job/FDD_Portswap_Promoted_Load_BTSOM"
                 target="_blank">{{ props.item.casename }}</a>
            </td>
            <td>{{ props.item.btsid }}</td>
            <td>
              <a href="http://10.52.200.190/view/AICT_3_FDD/job/check_site_state_FDD_AICT3/25512/console"
                 target="_blank">{{ props.item.node }}</a>
            </td>
            <td>{{ props.item.result }}</td>
            <td>{{ props.item.suite }}</td>
          </tr>
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
      pagination: { sortBy: 'casename', descending: false, rowsPerPage: -1 },

      // UI Components related
      resultChkbox: null,

      // test data
      test_cases: [
        {
          casename: 'Configuration_File_Same_File_Is_Downloaded',
          btsid: '708',
          node: '135.252.122.156',
          result: 'Failed',
          suite: 'BTSOM'
        },
        {
          casename: 'LTE3397_5_Object_locking_required_param_in_delta_commission',
          btsid: '706',
          node: '135.252.122.154',
          result: 'NA',
          suite: 'BTSOM'
        },
        {
          casename: 'FZM_Testability_SysLog_UDP_IP_Configuration',
          btsid: '11804',
          node: '135.252.122.171',
          result: 'NULL',
          suite: 'Testability'
        }
      ]
    }
  },

  computed: {
    filteredItems () {
      let filteredData = this.cases

      if (this.resultChkbox !== null) {
        filteredData = filteredData.filter((item, i) => {
          if (this.resultChkbox.toUpperCase() === 'FAILED') {
            return item.result.toUpperCase() === 'FAILED'
          } else if (this.resultChkbox.toUpperCase() === 'NA') {
            return item.result.toUpperCase() === 'NA'
          } else {
            return item.result.toUpperCase() !== 'FAILED' && item.result.toUpperCase() !== 'NA'
          }
        })
      }

      return filteredData
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
      this.$api.get('/api/loadcases', this.loadName,
        res => {
          this.cases = res.data
        },
        er => {
          console.error('getLoadCases: ', er)
          this.cases = this.test_cases
        })
    }

    // UI Components related
  }
}
</script>

<style lang="scss" scoped>
</style>
