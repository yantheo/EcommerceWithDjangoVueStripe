<template>
  <div class="column is-3">
      <div class="box">
        <figure class="image mb-4">
          <img
            style="width: 100%; height: 300px; object-fit: cover"
            v-bind:src="product.get_thumbnail_image"
            v-bind:alt="product.name"
          />
        </figure>
        <h3 class="is-size-4">{{ product.name }}</h3>
        <p class="is-size-6 has-text-grey">${{ product.price }}</p>
        <router-link
          v-bind:to="product.get_absolute_url"
          class="button is-dark mt-4"
          >Details</router-link
        >
      </div>
  </div>
</template>
<script>
export default {
  name: 'ProductBox',
  props: {
    product: Object
  }
}
</script>