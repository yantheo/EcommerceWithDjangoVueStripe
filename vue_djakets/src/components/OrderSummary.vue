<template>
  <div>
    <h3></h3>
    <h4></h4>
    <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
            </tr>
          </thead>
          <tbody>
            <tr 
                v-for="item in order.items" 
                v-bind:key="item.product.id">
              <td>{{ item.product.name }}</td>
              <td>${{ item.product.price }}</td>
              <td>{{ item.quantity }}</td>
              <td>${{ getItemTotal(item).toFixed(2) }}</td>
            </tr>
          </tbody>
        </table>
  </div>
</template>
<script>
export default {
  name: "OrderSummary",
  props: {
    order: Object
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price
    },
    orderTotalLength(order) {
      return order.items.reduce((acc, curVal) => {
        return acc += curVal.quantity
      }, 0)
    },
  }
}
</script>