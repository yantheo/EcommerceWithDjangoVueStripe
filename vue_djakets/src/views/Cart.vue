<template>
  <div class="page-cart">
    <div class="columns is-multiline">
      <h1 class="title">
        Cart
      </h1>
      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="cartTotalLenght">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
          <CartItemVue 
            v-for="item in cart.items"
            v-bind:key="item.product.id"
            v-bind:initialItem="item"
            v-on:removeFromCart="removeFromCart"
          />
          </tbody>
        </table>
        <p v-else>You don't have any products in your cart</p>
        <div class="column is-12 box">
          <h2 class="subtitle">Summary</h2>
          <strong>${{ cartTotalPrice.toFixed(2)}}, {{cartTotalLenght}} items</strong>
          <hr>
          <router-link to='/cart/checkout' class="button is-dark">Proceed to checkout</router-link>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import CartItemVue from '../components/CartItem.vue'

export default {
  name: 'Cart',
  components: {
    CartItemVue
  },
  data() {
    return {
      cart: {
        items: []
      }
    }
  },
  mounted(){
    this.cart = this.$store.state.cart
  },
  methods: {
    removeFromCart(item){
      console.log('click')
      this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
    }
  },
  computed: {
    cartTotalLenght(){
      return this.cart.items.reduce((acc, curVal) => {
        return acc += curVal.quantity
      }, 0)
    },
    cartTotalPrice(){
      return this.cart.items.reduce((acc, curVal) => {
        return acc += curVal.product.price * curVal.quantity
      }, 0)
    }
  }
}

</script>