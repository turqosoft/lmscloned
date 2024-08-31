<template>
    <div>
      <!-- Vegetables List -->
      <div v-if="vegetablesBySection">
        <div v-for="(section, sectionName) in vegetablesBySection" :key="sectionName">
          <h3 class="text-lg font-bold">{{ sectionName }}</h3>
          <ul>
            <li 
              v-for="(vegetable, index) in section" 
              :key="index" 
              class="flex justify-between mb-2 border p-2 rounded-md shadow-md"
            >
              <span>{{ vegetable.name }} - ${{ vegetable.price.toFixed(2) }}</span>
              <button 
                @click="openPopup(vegetable)" 
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
  import { defineProps, defineEmits } from 'vue'
  
  // Define props
  const props = defineProps({
    vegetablesBySection: {
      type: Object,
      required: true
    }
  })
  
  // Define emits
  const emit = defineEmits(['openPopup'])
  
  // Function to emit the openPopup event
  const openPopup = (vegetable) => {
    emit('openPopup', vegetable)
  }
  </script>
  
  <style scoped>
  /* Add any scoped styles here */
  </style>