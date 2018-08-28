<template>
  <div>
    <v-card flat>
      <v-card-title>
        <strong>{{ loadName }}</strong>
        <v-spacer></v-spacer>
        <v-text-field v-model="item_search"
                      append-icon="search"
                      label="Search"
                      single-line
                      hide-details></v-text-field>
      </v-card-title>

      <v-data-table :pagination.sync="pagination"
                    :headers="subHeaders"
                    :items="testlines"
                    :search="item_search"
                    :class="['text-xs-left']"
                    hide-actions>
        <template slot="headers"
                  slot-scope="props">
          <tr>
            <th v-for="header in headers"
                :key="header.key"
                :colspan="header.colspan">
              {{ header.text }}
            </th>
          </tr>

          <tr>
            <th v-for="header in subHeaders"
                :key="header.key"
                :class="['column sortable', pagination.descending ? 'desc' : 'asc', header.value === pagination.sortBy ? 'active' : '']"
                @click="changeSort(header)">
              {{ header.text }}
              <v-icon small>arrow_upward</v-icon>
            </th>
          </tr>
        </template>

        <template slot="items"
                  slot-scope="props">
          <tr>
            <td class="text-xs-left">
              <a href="http://10.52.200.190/job/FDD_Portswap_Promoted_Load_BTSOM"
                 target="_blank">{{ props.item.testline }}</a>
            </td>
            <td class="text-xs-left">{{ props.item.btsid }}</td>
            <td class="text-xs-left">{{ props.item.ca }}</td>
            <td class="text-xs-left">
              <a href="http://10.52.200.190/view/AICT_3_FDD/job/check_site_state_FDD_AICT3/25512/console"
                 target="_blank">{{ props.item.check_site_result }}</a>
            </td>
            <td class="text-xs-left">{{ props.item.check_site_timestamp }}</td>
            <td class="text-xs-left">
              <a href="http://10.52.200.190/view/AICT_3_FDD/job/healthCheckup_AICT3_FDD/24854/console"
                 target="_blank">{{ props.item.healthCheckup_result }}</a>
            </td>
            <td class="text-xs-left">{{ props.item.healthCheckup_timestamp }}</td>
            <td class="text-xs-left">
              <a href="http://10.52.200.190/view/AICT_3_FDD/job/upgrade_FDD_AICT3/24065/console"
                 target="_blank">{{ props.item.upgrade_result }}</a>
            </td>
            <td class="text-xs-left">{{ props.item.upgrade_timestamp }}</td>
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
    this.getLoadToTLs()
    this.createBreadcrums()
  },

  data () {
    return {
      // json data retrieved from server
      testlines: [],

      // header leverl I
      headers: [
        { key: 'loadsummary', text: 'Load Summary', value: 'loadsummary', align: 'left', colspan: '3' },
        { key: 'checksite', text: 'Check Site Job', value: 'checksite', align: 'left', colspan: '2' },
        { key: 'healthcheckup', text: 'Health Checkup Job', value: 'healthcheckup', align: 'left', colspan: '2' },
        { key: 'upgrade', text: 'Upgrading Job', value: 'upgrade', align: 'left', colspan: '2' }
      ],

      // header leverl II
      subHeaders: [
        { key: 'testline', text: 'Testline', align: 'left', value: 'testline' },
        { key: 'btsid', text: 'BTSID', align: 'left', value: 'btsid' },
        { key: 'ca', text: 'CA', align: 'left', value: 'ca' },
        { key: 'check_site_result', text: 'result', align: 'left', value: 'check_site_result' },
        { key: 'check_site_timestamp', text: 'timestamp', align: 'left', value: 'check_site_timestamp' },
        { key: 'healthCheckup_result', text: 'result', align: 'left', value: 'healthCheckup_result' },
        { key: 'healthCheckup_timestamp', text: 'timestamp', align: 'left', value: 'healthCheckup_timestamp' },
        { key: 'upgrade_result', text: 'result', align: 'left', value: 'upgrade_result' },
        { key: 'upgrade_timestamp', text: 'timestamp', align: 'left', value: 'upgrade_timestamp' }
      ],

      // vars from json data which will be used in the template

      // table data
      item_search: '',
      // sorting by descending
      pagination: { sortBy: 'testline', descending: false, rowsPerPage: -1 },

      // UI Components related

      // test data
      test_testlines: [
        {
          testline: '135.252.122.155',
          btsid: '707',
          ca: 'LTE3296',
          check_site_result: 'SUCCESS',
          check_site_timestamp: '2018-08-27 10:03:01',
          healthCheckup_result: 'SUCCESS',
          healthCheckup_timestamp: '2018-08-27 10:05:19',
          upgrade_result: 'Failed',
          upgrade_timestamp: '2018-08-27 10:14:55'
        },
        {
          testline: '135.252.122.157',
          btsid: '709',
          ca: 'Uplane',
          check_site_result: 'SUCCESS',
          check_site_timestamp: '2018-08-27 10:03:01',
          healthCheckup_result: 'Failed',
          healthCheckup_timestamp: '2018-08-27 10:05:20',
          upgrade_result: 'SUCCESS',
          upgrade_timestamp: '2018-08-27 10:14:55'
        },

        {
          testline: '135.252.122.159',
          btsid: '720',
          ca: 'Uplane',
          check_site_result: 'SUCCESS',
          check_site_timestamp: '2018-08-27 10:03:01',
          healthCheckup_result: 'SUCCESS',
          healthCheckup_timestamp: '2018-08-27 10:05:21',
          upgrade_result: 'SUCCESS',
          upgrade_timestamp: '2018-08-27 10:14:55'
        }
      ]
    }
  },

  computed: {
  },

  watch: {
    /** Watch route changing, beacuse the current view was bound by many URLs, but the created() function
     * only be executed once when loaded.The same component instance will be reused. Since both routes
     * render the same component, this is more efficient than destroying the old instance and then creating
     * a new one. However, this also means that the lifecycle hooks of the component will not be called.
     * So we should watch $route for reacting URLs' changing
     **/
    '$route' (to, from) {
      this.getLoadToTLs()
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
          text: 'cases',
          path: '/loads/index/fzmtdd/' + this.loadName + '/cases'
        }
      ])
    },

    // get loads list
    getLoadToTLs () {
      console.log('Enter getLoadToTLs: ', this.loadName)
      this.$api.get('/api/loadtls', this.loadName,
        res => {
          this.testlines = res.data
        },
        er => {
          console.error('getLoadToTLs: ', er)
          this.testlines = this.test_testlines
        })
    },

    // UI releated
    changeSort (header) {
      this.pagination.sortBy = header.value
      this.pagination.descending = !this.pagination.descending
    }
  },

  beforeRouteEnter (to, from, next) {
    console.info('beforeRouteEnter:', to.path)
    next()
  }
}
</script>

<style lang="scss" scoped>
tr {
  border: #cccccc solid 1px;
}

th {
  height: 0%;
}

tr.border_top {
  border-top: #cccccc solid 1px;
  border-bottom: #cccccc solid 0px;
}
tr.border_bottom {
  border-top: #cccccc solid 0px;
  border-bottom: #cccccc solid 1px;
}
</style>
