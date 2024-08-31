<template>
    <div>
      <h2 class="text-xl font-semibold mb-4">Your Cart</h2>
      <div v-if="cartItems.length">
        <div v-for="item in cartItems" :key="item.id" class="mb-4 border p-4 rounded">
          <div class="flex justify-between items-center">
            <div>
              <h3 class="text-lg font-semibold">{{ item.name }}</h3>
              <p><strong>Quantity:</strong> {{ item.quantity }}</p>
            </div>
          </div>
        </div>
        <button 
          @click="$emit('submitCart')"
          class="mt-4 py-2 px-4 bg-blue-500 text-white rounded"
        >
          Submit Cart
        </button>
      </div>
      <div v-else>
        Your cart is empty.
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue'
  
  const props = defineProps({
    cartItems: {
      type: Array,
      required: true
    }
  })
  </script>
  