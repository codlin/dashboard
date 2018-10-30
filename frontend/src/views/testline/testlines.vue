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
          <v-dialog v-model="dialog"
                    lazy-validation>
            <v-btn slot="activator"
                   color="primary"
                   dark
                   class="mb-2">New Testline</v-btn>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>
              <v-alert :value="alert"
                       :type="alert_type"
                       transition="scale-transition">
                {{ alert_text }}
              </v-alert>
              <v-card-text>
                <v-container grid-list-md>
                  <v-layout wrap>
                    <v-flex xs12
                            sm6
                            md4>
                      <v-autocomplete ref="product"
                                      :rules="[() => !!editedItem.product || 'This field is required']"
                                      :items="products"
                                      v-model="editedItem.product"
                                      label="Product"
                                      placeholder="Select..."
                                      required></v-autocomplete>
                    </v-flex>
                    <v-flex xs12
                            sm6
                            md4>
                      <v-text-field v-model="editedItem.mode"
                                    required
                                    data-vv-name="mode"
                                    label="Mode"
                                    v-validate="'required|max:8'"
                                    :counter="8"
                                    :error-messages="errors.collect('mode')"></v-text-field>
                    </v-flex>
                    <v-flex xs12
                            sm6
                            md4>
                      <v-text-field v-model="editedItem.sitetype"
                                    required
                                    data-vv-name="sitetype"
                                    label="Site Type"
                                    v-validate="'required|max:16'"
                                    :counter="16"
                                    :error-messages="errors.collect('sitetype')"></v-text-field>
                    </v-flex>
                    <v-flex xs12
                            sm6
                            md4>
                      <v-text-field v-model="editedItem.node"
                                    required
                                    data-vv-name="node"
                                    label="Node"
                                    v-validate="'required|max:64'"
                                    :counter="64"
                                    :error-messages="errors.collect('node')"></v-text-field>
                    </v-flex>
                    <v-flex xs12
                            sm6
                            md4>
                      <v-text-field v-model="editedItem.cfgid"
                                    required
                                    data-vv-name="cfgid"
                                    label="ID"
                                    v-validate="'required|max_value:12345678'"
                                    :counter="8"
                                    :error-messages="errors.collect('cfgid')"></v-text-field>
                    </v-flex>
                    <v-flex xs12
                            sm6
                            md4>
                      <v-text-field v-model="editedItem.ca"
                                    required
                                    data-vv-name="ca"
                                    label="CA"
                                    v-validate="'required|max:16'"
                                    :counter="16"
                                    :error-messages="errors.collect('ca')"></v-text-field>
                    </v-flex>
                    <v-flex xs12
                            sm6
                            md4>
                      <v-text-field v-model="editedItem.jenkinsjob"
                                    required
                                    data-vv-name="jenkinsjob"
                                    label="Jenkins Job"
                                    v-validate="'required|max:255'"
                                    :counter="255"
                                    :error-messages="errors.collect('jenkinsjob')"></v-text-field>
                    </v-flex>
                    <v-flex xs12
                            sm6
                            md4>
                      <v-text-field v-model="editedItem.mbtsid"
                                    required
                                    data-vv-name="mbtsid"
                                    label="Mobility BTSID"
                                    v-validate="'max_value:12345678'"
                                    :counter="8"
                                    :error-messages="errors.collect('mbtsid')"></v-text-field>
                    </v-flex>
                    <v-flex xs12
                            sm6
                            md4>
                      <v-text-field v-model="editedItem.mnode"
                                    required
                                    data-vv-name="mnode"
                                    label="Mobility Node"
                                    v-validate="'max:64'"
                                    :counter="64"
                                    :error-messages="errors.collect('mnode')"></v-text-field>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1"
                       flat
                       @click.native="close">Cancel</v-btn>
                <v-btn color="blue darken-1"
                       flat
                       @click.native="save">Save</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
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
              <td>{{ getProductText(props.item.product) }}</td>
              <!-- <td>{{ props.item.mode }}</td> -->
              <td>{{ props.item.sitetype }}</td>
              <td>{{ props.item.node }}</td>
              <td>{{ props.item.cfgid }}</td>
              <td>{{ props.item.ca }}</td>
              <td>{{ props.item.jenkinsjob }}</td>
              <td>{{ props.item.mbtsid }}</td>
              <td>{{ props.item.mnode }}</td>
              <td>
                <v-icon small
                        class="mr-2"
                        @click="editItem(props.item)">
                  edit
                </v-icon>
                <v-icon small
                        @click="deleteItem(props.item)">
                  delete
                </v-icon>
              </td>
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
import { isObjectValueEqual } from '../../../static/js/utils.js'
export default {
  created () {
    this.getProducts()
    this.getTestlines()
  },

  data () {
    return {
      /* json data retrieved from server */
      products: [],
      testlines: [],

      /* UI Components related */
      // table data
      tblHeaders: [
        { text: 'Product', align: 'left', value: 'product' },
        // { text: 'Mode', align: 'left', value: 'mode' },
        { text: 'Site Type', align: 'left', value: 'sitetype' },
        { text: 'Jenkins Node', align: 'left', value: 'node' },
        { text: 'ID', align: 'left', value: 'cfgid' },
        { text: 'CA', align: 'left', value: 'ca' },
        { text: 'Jenkins Job', align: 'left', value: 'jenkinsjob' },
        { text: 'Mobility BTSID', align: 'left', value: 'mbtsid' },
        { text: 'Mobility Node', align: 'left', value: 'mnode' },

        // keep this colum at last
        { text: 'Actions', align: 'left', value: 'actions', sortable: false }
      ],

      item_search: '',
      productChkbox: null,

      // sorting by descending
      pagination: { sortBy: 'sitetype', descending: false, rowsPerPage: -1 },

      // New testline template
      dialog: false,
      valid: false,
      editedIndex: -1,
      // edited item
      editedItem: {
        product: '',
        mode: '',
        sitetype: '',
        node: '',
        cfgid: '',
        ca: '',
        jenkinsjob: '',
        mbtsid: '',
        mnode: ''
      },
      // alert
      alert: false,
      alert_type: 'success',
      alert_text: 'This is a success alert.'
    }
  },

  computed: {
    filteredItems () {
      let filteredData = this.testlines
      if (this.productChkbox !== null) {
        filteredData = filteredData.filter((item, i) => {
          return this.getProductName(item.product).toUpperCase() === this.productChkbox.toUpperCase()
        })
      }

      // console.log('filter data: ', filteredData)
      return filteredData
    },

    formTitle () {
      return this.editedIndex === -1 ? 'New Testline' : 'Edit Testline'
    }
  },

  watch: {
    /** Watch route changing, beacuse the current view was bound by many URLs, but the created() function
     * only be executed once when it loaded. In the Vue documnet: '...the same component instance will be
     * reused. Since both routes render the same component, this is more efficient than destroying the old
     * instance and then creating a new one. However, this also means that the lifecycle hooks of the component
     * will not be called.'
     * So we should watch $route for reacting URLs' changing
     **/
    $route () {
      this.getTestlines()
    },

    dialog (val) {
      val || this.close()
    }
  },

  methods: {
    getProducts () {
      console.log('Enter getProducts:')
      if (this.products.length > 0) {
        console.log('product already exist.')
        return
      }

      this.$api.get(
        '/api/products',
        null,
        r => {
          this.products = r.data
          console.log('getProducts: get result', this.products)
        },
        r => {
          console.log('Failed: ', r)
        }
      )

      console.log('Leave getProducts')
    },

    getTestlines () {
      this.$api.get(
        '/api/testlines',
        null,
        r => {
          this.testlines = r.data
          // console.log('getTestlines: ', this.testlines)
        },
        r => {
          console.log('Failed: ', r)
        }
      )
    },

    getProductText (productID) {
      for (let i = 0, len = this.products.length; i < len; i++) {
        let item = this.products[i]
        if (item.id === productID) {
          console.log('item.text: ', item.text)
          return item.text
        }
      }
      return '-'
    },

    getProductName (productID) {
      for (let i = 0, len = this.products.length; i < len; i++) {
        let item = this.products[i]
        if (item.id === productID) {
          console.log('item.name: ', item.name)
          return item.name
        }
      }
      return '-'
    },

    getProductID (productName) {
      for (let i = 0, len = this.products.length; i < len; i++) {
        let item = this.products[i]
        if (item.name === productName) {
          console.log('item.id: ', item.id)
          return item.id
        }
      }
      return '-'
    },

    refreshData () {
      this.getTestlines()
    },

    editItem (item) {
      console.log('editItem: ' + item.product)

      this.editedIndex = this.testlines.indexOf(item)
      console.log('index:', this.editedIndex)

      let itemTemp = item
      itemTemp.product = this.getProductText(item.product)
      this.editedItem = Object.assign({}, itemTemp)
      // console.log('editedItem:', this.editedItem)
      this.dialog = true
    },

    deleteItem (item) {
      const index = this.testlines.indexOf(item)

      if (confirm('Are you sure you want to delete this item?')) {
        // delete an exist testline
        this.$api.delete(
          '/api/testlines/',
          { id: this.editedItem.id },
          r => {
            console.log('Delete data successfully.')
            this.testlines.splice(index, 1)
          },
          r => {
            console.log('Error: ', r)
          }
        )
      }
    },

    close () {
      this.dialog = false
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
        this.$validator.reset()
        this.clear_alert()
      }, 300)
    },

    save () {
      this.$validator.validate().then(result => {
        if (result) {
          console.log('editedIndex:', this.editedIndex)
          // testline exist
          if (this.editedIndex > -1) {
            console.log('old data:', this.testlines[this.editedIndex])
            console.log('new data:', this.editedItem)
            // if testline is no change, close it.
            if (
              isObjectValueEqual(
                this.testlines[this.editedIndex],
                this.editedItem
              )
            ) {
              this.close()
            } else {
              // update an exist testline
              this.$api.put(
                '/api/testlines/',
                this.editedItem,
                r => {
                  console.log('Update data successfully.')
                  Object.assign(
                    this.testlines[this.editedIndex],
                    this.editedItem
                  )
                  this.success_alert()
                  setTimeout(() => {
                    this.close()
                  }, 1000)
                },
                r => {
                  console.log('Error: ', r)
                  this.fail_alert(r)
                }
              )
            }
          } else {
            // create a new testline
            this.$api.post(
              '/api/testlines/',
              this.editedItem,
              r => {
                console.log('Push data successfully.')
                this.testlines.push(this.editedItem)
                this.success_alert()
                setTimeout(() => {
                  this.close()
                }, 1000)
              },
              r => {
                console.log('Error: ', r)
                this.fail_alert(r)
              }
            )
          }
        }
      })
    },

    getCookie (name) {
      let value = ' ' + document.cookie
      let parts = value.split(' ' + name + '=')
      if (parts.length === 2) {
        return parts
          .pop()
          .split('')
          .shift()
      }
    },

    clear_alert () {
      this.alert = false
    },
    fail_alert (r) {
      this.alert = true
      this.alert_type = 'error'
      this.alert_text = 'Push data to server failed. ' + r
    },
    success_alert () {
      this.alert = true
      this.alert_type = 'success'
      this.alert_text = 'Push data successfully.'
    }
    // for testing
  }
}
</script>

<style lang='scss' scoped>
// .v-tabs__div {
//   text-transform: none
//   font-size: 12px
// }
</style>
