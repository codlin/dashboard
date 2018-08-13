<template>
  <div>
    <v-card flat>
      <v-card-title>
        <strong>Details</strong>
        <v-spacer></v-spacer>
        <v-text-field v-model="load_search"
                      append-icon="search"
                      label="Search"
                      single-line
                      hide-details></v-text-field>
      </v-card-title>
      <v-data-table :pagination.sync="pagination"
                    :headers="loadTblHeaders"
                    :items="loads[productId]"
                    :search="load_search"
                    hide-actions>
        <template slot="items"
                  slot-scope="props">
          <tr :bgcolor=tableRowColor(props.item)>
            <td>{{ props.item.starttime }}</td>
            <td class="text-xs-left">{{ props.item.load }}</td>
            <td class="text-xs-left">{{ props.item.passed }}</td>
            <td class="text-xs-left">{{ props.item.failed }}</td>
            <td class="text-xs-left">{{ props.item.norun }}</td>
            <td class="text-xs-left">{{ props.item.total }}</td>
            <td class="text-xs-left">{{ props.item.firstpassrate }}</td>
            <td class="text-xs-left">{{ props.item.passrate }}</td>
            <td class="text-xs-left">{{ props.item.cases }}</td>
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

export default {
  props: {
    productId: {
      type: String,
      required: true
    },
    loadName: {
      type: String,
      required: true
    },
    startTime: {
      type: String,
      required: true
    }
  },

  data () {
    return {
      // json data retrieved from server
      loads: [],
      loadTblHeaders: [],

      // vars from json data which will be used in the template

      // table data
      load_search: '',
      // sorting by descending
      pagination: { sortBy: 'starttime', descending: true, rowsPerPage: -1 },

      // UI Components related

      // test data
      test_loads: {
        'fzmfdd':
          [
            {
              starttime: '2018-07-25 09:20:57',
              load: 'FLF18_ENB_0000_010120_000000',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-25 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000000',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 35,
              passrate: 40,
              cases: 'Link'
            },
            {
              starttime: '2018-07-25 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000000',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-25 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000000',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 100,
              cases: 'Link'
            },
            {
              starttime: '2018-07-26 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000001',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-27 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000002',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-28 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000003',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-25 09:20:57',
              load: 'FLF18_ENB_0000_010120_000000',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-25 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000000',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 35,
              passrate: 40,
              cases: 'Link'
            },
            {
              starttime: '2018-07-25 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000000',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-25 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000000',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 100,
              cases: 'Link'
            },
            {
              starttime: '2018-07-26 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000001',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-27 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000002',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-28 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000003',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            }, {
              starttime: '2018-07-25 09:20:57',
              load: 'FLF18_ENB_0000_010120_000000',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-25 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000000',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 35,
              passrate: 40,
              cases: 'Link'
            },
            {
              starttime: '2018-07-25 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000000',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-25 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000000',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 100,
              cases: 'Link'
            },
            {
              starttime: '2018-07-26 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000001',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-27 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000002',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-28 15:06:32',
              load: 'FLF18SP_ENB_0000_000375_000003',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            }
          ],
        'fzmtdd':
          [
            {
              starttime: '2018-07-27 09:20:57',
              load: 'TLF18_ENB_0000_010120_000000',
              passed: 317,
              failed: 15,
              norun: 28,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-25 15:06:32',
              load: 'TLF18SP_ENB_0000_000375_000000',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 35,
              passrate: 40,
              cases: 'Link'
            }
          ],
        'cfzcfdd':
          [
            {
              starttime: '2018-07-27 09:20:57',
              load: 'FLC18_ENB_0000_010120_000000',
              passed: 317,
              failed: 15,
              norun: 28,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-25 15:06:32',
              load: 'FLC18SP_ENB_0000_000375_000000',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 35,
              passrate: 40,
              cases: 'Link'
            }
          ],
        'cfzctdd':
          [
            {
              starttime: '2018-07-27 09:20:57',
              load: 'TLC18_ENB_0000_010120_000000',
              passed: 317,
              failed: 15,
              norun: 28,
              total: 335,
              firstpassrate: 89.6,
              passrate: 91.6,
              cases: 'Link'
            },
            {
              starttime: '2018-07-25 15:06:32',
              load: 'TLF18SP_ENB_0000_000375_000000',
              passed: 307,
              failed: 15,
              norun: 18,
              total: 335,
              firstpassrate: 35,
              passrate: 40,
              cases: 'Link'
            }
          ]
      },
      test_loadTblHeaders: [
        { text: 'Start Time', align: 'left', value: 'starttime' },
        { text: 'Load', align: 'left', value: 'load' },
        { text: 'Passed', align: 'left', value: 'passed' },
        { text: 'Failed', align: 'left', value: 'failed' },
        { text: 'NA', align: 'left', value: 'norun' },
        { text: 'Total', align: 'left', value: 'total' },
        { text: 'First PassRate (%)', align: 'left', value: 'firstpassrate' },
        { text: 'PassRate (%)', align: 'left', value: 'passRate' },
        { text: 'Cases', align: 'left', value: 'cases' }
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
      this.getLoadList()
    }
  },

  methods: {
    // get loads list
    getLoadList () {
      console.log('Enter getLoadList: ', this.loadName)
      if (this.loads[this.productId] == null) {
        this.$api.get('/api/loads', this.productId,
          res => {
            this.loads = res.data
          },
          er => {
            console.error('getLoadList: ', er)
            /** Due to limitations in JavaScript, Vue cannot detect the following changes to an array:
             * 1. When you directly set an item with the index, e.g. vm.items[indexOfItem] = newValue
             * 2. When you modify the length of the array, e.g. vm.items.length = newLength
             * **/
            Vue.set(this.loads, this.productId, this.test_loads[this.productId])
            console.log('getLoadList: mock data ', this.loads[this.productId])
          })
      } else {
        this.increGetLoadList()
      }

      console.log('Leave getLoadList')
    },

    // incremental get loads
    increGetLoadList () {
      console.log('Enter increGetLoadList: product', this.productId)
      let latestLoad = this.loads[this.productId][0]
      this.$api.get('/api/loads', { productid: this.productId, from: { timestart: latestLoad.startTime, load: latestLoad.loadName } },
        r => {
          this.loads[this.productId].unshift(r.data)
        },
        r => {
          console.log('getLoadList: mock data')
          Vue.set(this.loads, this.productId, this.test_loads[this.productId].concat(this.loads[this.productId]))
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

    // for testing
    // init page data
    test_initPageData () {
      this.loadTblHeaders = this.test_loadTblHeaders
    }
  },

  created () {
    // for testing
    this.test_initPageData()

    // get data from server
    this.getLoadList()
  },

  beforeRouteEnter (to, from, next) {
    console.info('beforeRouteEnter:', to.path)
    next()
  }
}
</script>

<style lang="scss" scoped>
// .v-tabs__div {
//   text-transform: none;
//   font-size: 12px;
// }
</style>
