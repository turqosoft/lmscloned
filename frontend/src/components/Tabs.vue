<template>
  <div class="mb-4">
    <button 
      @click="$emit('changeTab', 'viewlist')" 
      :class="{'bg-blue-500': currentTab === 'viewlist'}" 
      class="py-2 px-4 mr-2 rounded"
    >
      ViewList
    </button>
    <button 
      @click="$emit('changeTab', 'itemgroup')" 
      :class="{'bg-blue-500': currentTab === 'itemgroup'}" 
      class="py-2 px-4 rounded"
    >
      ItemGroup
    </button>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  currentTab: {
    type: String,
    required: true
  }
})
</script>
