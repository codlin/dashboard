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
                    :headers="tableHeaders"
                    :items="testlines"
                    :search="item_search"
                    :class="['text-xs-left', 'border 1px solid black']"
                    hide-actions>
        <template slot="headers"
                  slot-scope="props">
          <tr>
            <th colspan="3"> Load Summary </th>
            <th colspan="2"> check_site </th>
            <th colspan="2"> healthCheckup </th>
            <th colspan="2"> upgrade </th>
          </tr>
          <tr>
            <th v-for="header in tableHeaders"
                :key="header.key"
                :class="['column sortable']"
                @click="changeSort(header.value)">
              {{ header.text }}
            </th>
          </tr>
        </template>

        <template slot="items"
                  slot-scope="props">
          <tr>
            <td>{{ props.item.testline }}</td>
            <td class="text-xs-left">{{ props.item.btsid }}</td>
            <td class="text-xs-left">{{ props.item.ca }}</td>
            <td class="text-xs-left">{{ props.item.check_site_result }}</td>
            <td class="text-xs-left">{{ props.item.check_site_timestamp }}</td>
            <td class="text-xs-left">{{ props.item.healthCheckup_result }}</td>
            <td class="text-xs-left">{{ props.item.healthCheckup_timestamp }}</td>
            <td class="text-xs-left">{{ props.item.upgrade_result }}</td>
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
  },

  data () {
    return {
      // json data retrieved from server
      testlines: [],
      tableHeaders: [
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
          testline: '135.252.122.157',
          btsid: '709',
          ca: 'Uplane',
          check_site_result: 'SUCCESS',
          check_site_timestamp: '2018-08-27 10:03:01',
          healthCheckup_result: 'SUCCESS',
          healthCheckup_timestamp: '2018-08-27 10:05:19',
          upgrade_result: 'SUCCESS',
          upgrade_timestamp: '2018-08-27 10:14:55'
        },
        {
          testline: '135.252.122.155',
          btsid: '707',
          ca: 'LTE3296',
          check_site_result: 'SUCCESS',
          check_site_timestamp: '2018-08-27 10:03:01',
          healthCheckup_result: 'SUCCESS',
          healthCheckup_timestamp: '2018-08-27 10:05:19',
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
    }

    // UI releated
  },

  beforeRouteEnter (to, from, next) {
    console.info('beforeRouteEnter:', to.path)
    next()
  }
}
</script>

<style lang="scss" scoped>
</style>
