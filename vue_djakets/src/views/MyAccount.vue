<template>
  <div class="page-my-account">
    <div class="columns is-multiline">
      <h1 class="title">My account</h1>
    </div>
    <div class="column is-12">
      <button @click="logout()" class="button is-danger">Log Out</button>
    </div>
    <hr>
    <div class="column is-12">
      <h2 class="subtitle">
        My Orders
      </h2>
      <OrderSummary
        v-for="order in orders"
        v-bind:key="order.id"
        v-bind:order="order" 
      />
    </div>
  </div>
</template>
<script>
import axios from 'axios'

import OrderSummary from '@/components/OrderSummary.vue'

export default {
  name: "MyAccount",
  components: {
    OrderSummary
  },
  data() {
    return {
      orders: []
    }
  },
  mounted() {
    document.title = "My account | Djakets"
    this.getMyOrders()
  },
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = ""
      localStorage.removeItem("token")
      localStorage.removeItem("username")
      localStorage.removeItem("userid")
      this.$store.commit("removeToken")
      this.$router.push('/')
    },
    async getMyOrders(){
      this.$store.commit('setIsLoading', true)
      await axios
        .get('/api/v1/orders/')
        .then(response => {
          this.orders = response.data
          this.$store.commit('setIsLoading', false)
        })
        .catch(error => {
          console.error(error)
        })
    }
  }
}
</script>