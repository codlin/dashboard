<template>
  <div>
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
                        v-model="dateChkbox"
                        label="7 Days"
                        value="theweek"></v-checkbox>
            <v-checkbox hide-details
                        v-model="dateChkbox"
                        label="24-hour"
                        value="24hour"></v-checkbox>
            <v-checkbox hide-details
                        v-model="passrateChkBox"
                        value="Passed"
                        label="Passed"></v-checkbox>
            <v-checkbox hide-details
                        v-model="passrateChkBox"
                        value="Failed"
                        label="Failed"></v-checkbox>

          </v-layout>
        </v-content>
        <v-text-field v-model="load_search"
                      append-icon="search"
                      label="Search"
                      single-line
                      hide-details></v-text-field>
      </v-toolbar>

      <v-data-table :pagination.sync="pagination"
                    :headers="loadTblHeaders"
                    :items="filteredItems"
                    :search="load_search"
                    hide-actions>
        <template slot="items"
                  slot-scope="props">
          <tr>
            <td>{{ props.item.start_time }}</td>
            <td class="text-xs-left">
              <router-link :to="{ name: 'loadtls', params: { loadName: props.item.load_name } }">{{ props.item.load_name }}</router-link>
            </td>
            <td class="text-xs-left">{{ props.item.passed_num }}</td>
            <td class="text-xs-left">{{ props.item.failed_num }}</td>
            <td class="text-xs-left">{{ props.item.norun_num }}</td>
            <td class="text-xs-left">{{ props.item.total_num }}</td>
            <td class="text-xs-left">{{ props.item.first_passrate }}</td>
            <td class="text-xs-left">{{ props.item.passrate }}</td>
            <td class="text-xs-left">
              <router-link :to="{ name: 'loadcases', params: { loadName: props.item.load_name } }">LINK</router-link>
            </td>
          </tr>
        </template>
        <v-alert slot="no-results"
                 :value="true"
                 color="error"
                 icon="warning">
          Your search for "{{ load_search }}" found no results.
        </v-alert>
      </v-data-table>
    </v-card>
  </div>
</template>

<script>
import Vue from 'vue'
import { daysBetween, getCurrentDate } from '../../../static/js/utils.js'

export default {
  props: {
    productId: {
      type: String,
      required: true
    }
  },

  created () {
    // get data from server
    this.getLoadList()

    // create breadcrums
    this.createBreadcrums()
  },

  data () {
    return {
      // json data retrieved from server
      loads: [],
      loadTblHeaders: [
        { text: 'Start Time', align: 'left', value: 'start_time' },
        { text: 'Load', align: 'left', value: 'load_name' },
        { text: 'Passed', align: 'left', value: 'passed_num' },
        { text: 'Failed', align: 'left', value: 'failed_num' },
        { text: 'NA', align: 'left', value: 'norun_num' },
        { text: 'Total', align: 'left', value: 'total_num' },
        { text: 'First PassRate (%)', align: 'left', value: 'first_passrate' },
        { text: 'PassRate (%)', align: 'left', value: 'passrate' },
        { text: 'Cases', align: 'left', value: 'cases' }
      ],

      // vars from json data which will be used in the template

      // table data
      load_search: '',
      // sorting by descending
      pagination: { sortBy: 'start_time', descending: true, rowsPerPage: -1 },

      // UI Components related
      dateChkbox: null,
      passrateChkBox: null
    }
  },

  computed: {
    filteredItems () {
      let filteredData = this.loads[this.productId]

      if (this.dateChkbox !== null || this.passrateChkBox !== null) {
        if (this.dateChkbox !== null) {
          let today = getCurrentDate()
          let days = (this.dateChkbox === 'theweek') ? 7 : 1
          filteredData = filteredData.filter((item, i) => {
            let starTime = item.start_time
            let date = starTime.substring(0, starTime.indexOf(' ')).trim()
            return daysBetween(today, date) <= days
          })
        }

        if (this.passrateChkBox !== null) {
          filteredData = filteredData.filter((item, i) => {
            return (this.passrateChkBox === 'Passed') ? (item.passrate === 100) : (item.passrate <= 40)
          })
        }

        console.log(filteredData)
      }

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
      this.getLoadList()
      this.createBreadcrums()
    }
  },

  methods: {
    createBreadcrums () {
      // create breadcrums
      this.$store.dispatch('setBreadcrumbs', [
        {
          disabled: true,
          text: 'Loads',
          path: '/loads'
        },
        {
          disabled: false,
          text: this.productId.toUpperCase(),
          path: '/loads/index/' + this.productId
        }
      ])

      this.$store.dispatch('setRelatedChips', [])
    },

    // get loads list
    getLoadList () {
      if (this.loads[this.productId] == null) {
        this.$api.get('/api/loads', { productid: this.productId },
          res => {
            /** Due to limitations in JavaScript, Vue cannot detect the following changes to an array:
             * 1. When you directly set an item with the index, e.g. vm.items[indexOfItem] = newValue
             * 2. When you modify the length of the array, e.g. vm.items.length = newLength
             * **/
            console.log(res.data)
            Vue.set(this.loads, this.productId, res.data)
            console.log('getLoadList: data ', this.loads[this.productId])
          },
          er => {
            console.error('getLoadList: ', er)
          })
      } else {
        this.increGetLoadList()
      }
    },

    // incremental get loads
    increGetLoadList () {
      let params = this.loads[this.productId].length === 0 ? { productid: this.productId } : { productid: this.productId, from: this.loads[this.productId][0].start_time }
      this.$api.get('/api/loads', params,
        r => {
          console.log('data:', r.data)
          if (r.data.length > 0) {
            this.loads[this.productId].unshift(r.data)
          }
        },
        r => {
          console.log('getLoadList: mock data')
        })

      console.log('Leave getLoadList')
    },

    // UI releated
    tableRowColor (item) {
      console.log(item)
      if (item.passrate === 100) {
        return '#E8F5E9'
      } else if (item.passrate < 50) {
        return '#FBE9E7'
      }
    },

    refreshData () {
      console.log(this.dateChkbox)
      this.increGetLoadList()
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
