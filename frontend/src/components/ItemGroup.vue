<template>
    <div>
      <div v-if="itemGroups.length === 0">
        Loading item groups...
      </div>
      <div v-else>
        <div v-for="(group, index) in itemGroups" :key="index" class="mb-6">
          <h2 class="text-xl font-semibold mb-2">{{ group.name }}</h2>
          <div v-if="group.items.length === 0" class="text-gray-500">No items available.</div>
          <ul>
            <li 
              v-for="(item, itemIndex) in group.items" 
              :key="itemIndex" 
              class="flex justify-between mb-2 border p-2 rounded-md shadow-md"
            >
              <span>{{ item.name }} - ${{ item.price.toFixed(2) }}</span>
              <button 
                @click="$emit('openPopup', item)" 
                class="py-2 px-4 bg-black text-white rounded"
              >
                Add to Cart
              </button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue'
  
  const props = defineProps({
    itemGroups: {
      type: Array,
      required: true
    }
  })
  </script>
  