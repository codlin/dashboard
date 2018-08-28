<template>
  <v-layout id="loads"
            fill-height>
    <v-content>
      <v-flex d-flex
              md12>
        <v-toolbar dense
                   flat>
          <v-toolbar-items>
            <v-btn flat
                   v-for="product in productItems"
                   :key="product.name"
                   @click="forwardDefaultPage(product)">
              {{ product.text }}
            </v-btn>
          </v-toolbar-items>
        </v-toolbar>
      </v-flex>
      <v-flex d-flex
              md12>
        <v-card flat>
          <breadcrumbs>
          </breadcrumbs>
        </v-card>
      </v-flex>
      <v-flex d-flex
              md12>
        <router-view></router-view>
      </v-flex>
    </v-content>
  </v-layout>
</template>

<script>
import breadcrumbs from '../../components/breadcrums/breadcrums'
import { getTimestamp } from '../../../static/js/utils.js'

export default {
  components: {
    breadcrumbs
  },

  created () {
    this.getProducts()
  },

  data () {
    return {
      // json data retrieved from server
      products: [],

      // vars from json data which will be used in the template
      // UI Components related
      // breadcrumbs navigation
      loadsRouteList: [
        {
          text: 'Loads',
          disabled: true
        }
      ]
    }
  },

  computed: {
    productItems () {
      return this.products
    }
  },

  watch: {

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

          this.forwardDefaultPage(this.products[0])
        },
        r => {
          console.log('Failed: ', r)
        })

      console.log(getTimestamp(), 'Leave getProducts')
    },

    forwardDefaultPage (product) {
      console.log(product)
      this.$router.push({ name: 'index', params: { productId: product.name } })
    },

    // UI Components related
    createBreadcrums () {
      // create breadcrums
      this.$store.dispatch('setBreadcrumbs', [])
      this.$store.dispatch('setRelatedChips', [])
    }
  }

}
</script>

<style lang="scss" scoped>
// .v-tabs__div {
//   text-transform: none;
//   font-size: 12px;
// }
</style>
