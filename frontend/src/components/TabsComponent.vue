<template>
    <div class="mb-4">
      <div class="flex border-b">
        <button
          :class="{ 'bg-black text-white border-black': activeTab === 'list' }"
          class="py-2 px-4 border-b-2 font-semibold"
          @click="$emit('updateTab', 'list')"
        >
          Vegetable List
        </button>
        <button
          :class="{ 'bg-black text-white border-black': activeTab === 'cart' }"
          class="py-2 px-4 border-b-2 font-semibold"
          @click="$emit('updateTab', 'cart')"
        >
          Cart
        </button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps, defineEmits } from 'vue'
  const props = defineProps({ activeTab: String })
  const emit = defineEmits(['updateTab'])
  </script>
  