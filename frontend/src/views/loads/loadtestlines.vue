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
          </v-layout>
        </v-content>
        <v-text-field v-model="item_search"
                      append-icon="search"
                      label="Search"
                      single-line
                      hide-details></v-text-field>
      </v-toolbar>

      <v-data-table :pagination.sync="pagination"
                    :headers="subHeaders"
                    :items="filteredItems"
                    :search="item_search"
                    :class="['text-xs-left']"
                    hide-actions>
        <template slot="headers"
                  slot-scope="props">
          <tr>
            <th v-for="header in headers"
                :key="header.key"
                :hidden="HiddenHeaderItem(header)"
                :colspan="header.colspan">
              {{ header.text }}
            </th>
          </tr>

          <tr>
            <th v-for="header in subHeaders"
                :key="header.key"
                :hidden="HiddenHeaderItem(header)"
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
              <a :href="testline_url(props.item)"
                 target="_blank">{{ props.item.testline }}</a>
            </td>
            <td class="text-xs-left">{{ props.item.cfgid }}</td>

            <td class="text-xs-left">
              <a :href="props.item.check_site_url"
                 target="_blank">{{ props.item.check_site_result }}</a>
            </td>
            <td class="text-xs-left">{{ props.item.check_site_timestamp }}</td>

            <td class="text-xs-left"
                :hidden="tdHidden">
              <a :href="props.item.health_checkup_url"
                 target="_blank">{{ props.item.health_checkup_result }}</a>
            </td>
            <td class="text-xs-left"
                :hidden="tdHidden">{{ props.item.health_checkup_timestamp }}</td>

            <td class="text-xs-left">
              <a :href="props.item.upgrade_url"
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
    // fix loadname
    if (this.loadName.indexOf('LC') > -1) {
      this.loadName = this.loadName.replace('18A', '00')
    }
    // get data from server
    this.getLoadToTLs()
    this.createBreadcrums()
  },

  data () {
    return {
      // origin loadname
      origLoadName: this.loadName,

      // json data retrieved from server
      testlines: [],

      // header level I
      headers: [
        { key: 'loadsummary', text: 'Load Summary', value: 'loadsummary', align: 'left', colspan: '2' },
        { key: 'checksite', text: 'Check Site Job', value: 'checksite', align: 'left', colspan: '2' },
        { key: 'health_checkup', text: 'Health Checkup Job', value: 'health_checkup', align: 'left', colspan: '2' },
        { key: 'upgrade', text: 'Upgrading Job', value: 'upgrade', align: 'left', colspan: '2' }
      ],

      // header level II
      subHeaders: [
        { key: 'testline', text: 'Testline', align: 'left', value: 'testline' },
        { key: 'cfgid', text: 'BTSID', align: 'left', value: 'cfgid' },
        { key: 'check_site_result', text: 'result', align: 'left', value: 'check_site_result' },
        { key: 'check_site_timestamp', text: 'timestamp', align: 'left', value: 'check_site_timestamp' },
        { key: 'health_checkup_result', text: 'result', align: 'left', value: 'health_checkup_result' },
        { key: 'health_checkup_timestamp', text: 'timestamp', align: 'left', value: 'health_checkup_timestamp' },
        { key: 'upgrade_result', text: 'result', align: 'left', value: 'upgrade_result' },
        { key: 'upgrade_timestamp', text: 'timestamp', align: 'left', value: 'upgrade_timestamp' }
      ],

      // vars from json data which will be used in the template

      // table data
      item_search: '',
      // sorting by descending
      pagination: { sortBy: 'testline', descending: false, rowsPerPage: -1 },

      // UI Components related
      resultChkbox: null,
      tdHidden: (this.loadName.indexOf('LC') > -1)
    }
  },

  computed: {
    filteredItems () {
      let filteredData = this.testlines

      if (this.resultChkbox !== null) {
        filteredData = filteredData.filter((item, i) => {
          if (this.resultChkbox.toUpperCase() === 'FAILED') {
            return (item.check_site_result.toUpperCase() === 'FAILURE') ||
              (item.health_checkup_result.toUpperCase() === 'FAILURE') ||
              (item.upgrade_result.toUpperCase() === 'FAILURE')
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
      this.getLoadToTLs()
    }
  },

  methods: {
    createBreadcrums () {
      // create breadcrums
      this.$store.dispatch('pushBreadcrumbs',
        {
          disabled: false,
          text: this.origLoadName,
          path: '/loads/index/' + this.origLoadName + '/tls'
        }
      )

      // create related chips
      this.$store.dispatch('setRelatedChips', [
        {
          text: 'cases',
          path: '/loads/index/' + this.origLoadName + '/cases'
        }
      ])
    },

    HiddenHeaderItem (item) {
      console.log('HiddenHeaderItem:', this.loadName.indexOf('LC'))
      if (this.loadName.indexOf('LC') > -1) {
        if (item.key.indexOf('health_checkup') > -1) {
          return true
        }
      }
      return false
    },

    HiddenItem () {
      console.log('HiddenItem:', this.loadName.indexOf('LC'))
      if (this.loadName.indexOf('LC') > -1) {
        return true
      }
      return false
    },

    testline_url (item) {
      return item.url + '/computer/' + item.testline
    },

    // get loads testlines
    getLoadToTLs () {
      console.log('Enter getLoadToTLs: ', this.loadName)
      this.$api.get('/api/loadtls', { name: this.loadName },
        res => {
          console.info(res.data)
          this.convertData(res.data)
          this.testlines = res.data
          console.info('load testlines: ', this.testlines)
        },
        er => {
          console.error('getLoadToTLs: ', er)
        })
    },

    convertData (data) {
      // console.log(data)
      data.forEach(testline => {
        // console.log('testline: ', testline)
        testline['check_site_job'] = ''
        testline['check_site_result'] = ''
        testline['check_site_timestamp'] = ''
        testline['check_site_url'] = ''

        testline['health_checkup_job'] = ''
        testline['health_checkup_result'] = ''
        testline['health_checkup_timestamp'] = ''
        testline['health_checkup_url'] = ''

        testline['upgrade_job'] = ''
        testline['upgrade_result'] = ''
        testline['upgrade_timestamp'] = ''
        testline['upgrade_url'] = ''

        let jobs = testline.jobs.split(';')
        // console.log('jobs: ', jobs)
        jobs.forEach(job => {
          // console.log('job: ', job)
          let items = job.split(',')
          // console.log('items: ', items)
          if (items[0].indexOf('check_site') > -1) {
            testline.check_site_job = items[0]
            testline.check_site_result = items[1]
            testline.check_site_timestamp = items[2]
            testline.check_site_url = items[3]
          } else if (items[0].indexOf('healthCheckup') > -1) {
            testline.health_checkup_job = items[0]
            testline.health_checkup_result = items[1]
            testline.health_checkup_timestamp = items[2]
            testline.health_checkup_url = items[3]
          } else if (items[0].indexOf('upgrade') > -1) {
            testline.upgrade_job = items[0]
            testline.upgrade_result = items[1]
            testline.upgrade_timestamp = items[2]
            testline.upgrade_url = items[3]
          }
        })
      })
    },

    // UI releated
    changeSort (header) {
      this.pagination.sortBy = header.value
      this.pagination.descending = !this.pagination.descending
    }
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
