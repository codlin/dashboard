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
          <v-layout>
            <v-checkbox hide-details
                        v-model="dateChkbox"
                        label="1 Week"
                        value="oneweek"></v-checkbox>
            <v-checkbox hide-details
                        v-model="dateChkbox"
                        label="2 Weeks"
                        value="twoweek"></v-checkbox>
            <v-checkbox hide-details
                        v-model="passrateChkBox"
                        value="Passed"
                        label="Passed"></v-checkbox>
            <v-checkbox hide-details
                        v-model="passrateChkBox"
                        value="Failed"
                        label="Failed"></v-checkbox>
            <v-checkbox hide-details
                        v-model="isDebugged"
                        value="debugged"
                        label="Debugged"></v-checkbox>
          </v-layout>
        </v-content>
        <v-content>
          <v-layout>
            <v-select flat
                      v-model="selectedRelease"
                      :items="Releases"
                      attach
                      small-chips
                      placeholder="Release"
                      multiple></v-select>

            <v-text-field v-model="load_search"
                          append-icon="search"
                          label="Search"
                          single-line
                          hide-details></v-text-field>
          </v-layout>
        </v-content>
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
            <td>{{ props.item.duration }}</td>
            <td class="text-xs-left">
              <router-link :to="{ name: 'loadcases', params: { loadName: props.item.loadname } }">{{ props.item.loadname }}</router-link>
            </td>
            <td class="text-xs-left">
              <router-link :to="{ name: 'loadtls', params: { loadName: props.item.loadname } }">LINK</router-link>
            </td>
            <td class="text-xs-left">{{ props.item.passed_num }}</td>
            <td class="text-xs-left">{{ props.item.failed_num }}</td>
            <td class="text-xs-left">{{ props.item.norun_num }}</td>
            <td class="text-xs-left">{{ props.item.total_num }}</td>
            <td class="text-xs-left">{{ props.item.first_passrate }}</td>
            <td class="text-xs-left"
                :bgcolor="tableCellColor(props.item)">{{ props.item.passrate }}</td>
            <td class="text-xs-left">{{ props.item.debug }}</td>
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
import { daysBetween, getCurrentDate, getDuration } from '../../../static/js/utils.js'

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
      releases: new Set(),

      loadTblHeaders: [
        { text: 'Start Time', align: 'left', value: 'start_time' },
        { text: 'Duration (HH:MM:SS)', align: 'left', value: 'duration' },
        { text: 'Load', align: 'left', value: 'loadname' },
        { text: 'Testline', align: 'left', value: 'testline' },
        { text: 'Passed', align: 'left', value: 'passed_num' },
        { text: 'Failed', align: 'left', value: 'failed_num' },
        { text: 'NA', align: 'left', value: 'norun_num' },
        { text: 'Total', align: 'left', value: 'total_num' },
        { text: 'First PassRate (%)', align: 'left', value: 'first_passrate' },
        { text: 'PassRate (%)', align: 'left', value: 'passrate' },
        { text: 'Debug', align: 'left', value: 'debug' }
      ],

      // table data
      load_search: '',
      // sorting by descending
      pagination: { sortBy: 'start_time', descending: true, rowsPerPage: -1 },

      // UI Components related
      dateChkbox: null,
      passrateChkBox: null,
      isDebugged: null,
      selectedRelease: []
    }
  },

  computed: {
    filteredItems () {
      let filteredData = this.loads[this.productId]
      if (filteredData == null) {
        return
      }

      if (this.dateChkbox !== null || this.passrateChkBox !== null) {
        if (this.dateChkbox !== null) {
          let today = getCurrentDate()
          let days = (this.dateChkbox === 'oneweek') ? 7 : 14
          filteredData = filteredData.filter((item, i) => {
            let starTime = item.start_time
            let date = starTime.substring(0, starTime.indexOf(' ')).trim()
            return daysBetween(today, date) <= days
          })
        }

        if (this.passrateChkBox !== null) {
          filteredData = filteredData.filter((item, i) => {
            return (this.passrateChkBox === 'Passed') ? (parseFloat(item.passrate) >= 100) : (parseFloat(item.passrate) < 50)
          })
        }
        // console.log(filteredData)
      }

      console.log('this.isDebugged: ', this.isDebugged)
      if (this.isDebugged !== null) {
        filteredData = filteredData.filter((item, i) => {
          // console.log('item.debug: ', item.debug)
          return item.debug.toUpperCase() === 'YES'
        })
      }

      // for releases
      console.log('selected release: ' + this.selectedRelease)
      if (this.selectedRelease != null && this.selectedRelease.length > 0) {
        filteredData = filteredData.filter((item, i) => {
          let rel = item.loadname.split('_')[0]
          return this.selectedRelease.indexOf(rel) >= 0
        })
      }

      return filteredData
    },

    Releases () {
      console.log('Releases set:', this.releases)
      console.log('Releases:', [...this.releases])
      return [...this.releases]
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
      this.reInitVars()
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
      this.$api.get('/api/loads', { productid: this.productId },
        res => {
          /** Due to limitations in JavaScript, Vue cannot detect the following changes to an array:
           * 1. When you directly set an item with the index, e.g. vm.items[indexOfItem] = newValue
           * 2. When you modify the length of the array, e.g. vm.items.length = newLength
           * **/
          // console.log(res.data)
          this.convertData(res.data)
          // console.log(res.data)
          Vue.set(this.loads, this.productId, res.data)
          // console.log('getLoadList: data ', this.loads[this.productId])
          this.groupRelease(res.data)
        },
        er => {
          console.error('getLoadList: ', er)
        })
    },

    refreshData () {
      console.log(this.dateChkbox)
      this.getLoadList()
    },

    convertData (data) {
      let len = data.length
      data.forEach((item, i) => {
        let j = i + 1
        if (j < len) {
          item.duration = getDuration(data[j].start_time, item.start_time)
        } else {
          item.duration = 'NA'
        }
      })
    },

    groupRelease (data) {
      let releaseSet = new Set()
      data.forEach(item => {
        let rel = item.loadname.split('_')[0]
        releaseSet.add(rel)
      })
      this.releases = releaseSet
      console.log(this.releases)
    },

    reInitVars () {
      this.dateChkbox = null
      this.passrateChkBox = null
      this.isDebugged = null
      this.selectedRelease = []
    },

    // UI releated
    tableCellColor (item) {
      // console.log(item)
      if (item.passrate >= 100) {
        return '#E8F5E9'
      } else if (item.passrate < 50) {
        return '#FBE9E7'
      }
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
