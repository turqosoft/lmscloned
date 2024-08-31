<template>
    <div>
      <h2 class="text-xl font-semibold mb-4">Products</h2>
      <div v-if="products.length">
        <div v-for="product in products" :key="product.id" class="mb-4 border p-4 rounded">
          <div class="flex justify-between items-center">
            <div>
              <h3 class="text-lg font-semibold">{{ product.name }}</h3>
              <p v-if="product.parent_item_group"><strong>Parent:</strong> {{ product.parent_item_group }}</p>
            </div>
            <button 
              @click="() => $emit('addProduct', product)"
              class="py-2 px-4 bg-green-500 text-white rounded"
            >
              Add to Cart
            </button>
          </div>
        </div>
      </div>
      <div v-else>
        No products available.
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue'
  
  const props = defineProps({
    products: {
      type: Array,
      required: true
    }
  })
  </script>
  