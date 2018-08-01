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
                   v-for="product in products"
                   :key="product.id"
                   @click="updateNV(product)"
                   :to="{ name: 'index', params: { productId: product.id } }">
              {{ product.name }}
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

export default {
  components: {
    breadcrumbs
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

  },

  created () {
    this.getProducts()
  },

  methods: {
    getProducts () {
      console.log('Enter getProducts')
      this.$api.sync_get('/products', null,
        r => {
          console.log('getProducts: get result')
          this.products = r.data
          this.forwardDefaultPage()
        },
        r => {
          console.log('getProducts: get mock data')
          this.products = [
            {
              id: 'fzmfdd',
              name: 'FZM FDD'
            },
            {
              id: 'fzmtdd',
              name: 'FZM TDD'
            },
            {
              id: 'cfzcfdd',
              name: 'CFZC FDD'
            },
            {
              id: 'cfzctdd',
              name: 'cFZC TDD'
            }
          ]
          this.forwardDefaultPage()
        })

      console.log('Leave getProducts')
    },

    forwardDefaultPage () {
      const product = this.products[0].id
      this.loadsRouteList.push({ text: this.products[0].name, disabled: true })
      // routeItems.forEach(value => { this.loadsRouteList.push(value) })
      this.$router.push({ path: `/loads/index/${product}` })
    },

    // UI Components related
    updateNV (product) {
      console.info(product)
      // this.loadsRouteList.pop()
      this.loadsRouteList.push(product.name)
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
