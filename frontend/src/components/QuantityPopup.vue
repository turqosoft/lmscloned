<template>
    <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-gray-500 bg-opacity-75">
      <div class="bg-white p-6 rounded-md shadow-md">
        <h3 class="text-lg font-semibold mb-4">Enter Quantity for {{ product.name }}</h3>
        <input 
          type="number" 
          v-model="quantity" 
          :min="1"
          class="border p-2 rounded w-full mb-4"
        />
        <div class="flex justify-end gap-4">
          <button 
            @click="addToCart"
            class="py-2 px-4 bg-green-500 text-white rounded"
          >
            Add to Cart
          </button>
          <button 
            @click="$emit('close')"
            class="py-2 px-4 bg-red-500 text-white rounded"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps, defineEmits, ref } from 'vue'
  
  const props = defineProps({
    product: {
      type: Object,
      required: true
    },
    visible: {
      type: Boolean,
      required: true
    },
    initialQuantity: {
      type: Number,
      default: 1
    }
  })
  
  const emit = defineEmits(['add-to-cart', 'close'])
  
  const quantity = ref(props.initialQuantity)
  
  const addToCart = () => {
    emit('add-to-cart', { product: props.product, quantity: quantity.value })
  }
  </script>
  