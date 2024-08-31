<template>
    <div class="mt-4">
      <div class="text-lg font-semibold mb-2">{{ __('Items') }}</div>
      <table class="w-full border-collapse border border-gray-300 mb-4">
        <thead>
          <tr class="bg-gray-200">
            <th class="border border-gray-300 px-4 py-2">{{ __('Item Group') }}</th>
            <th class="border border-gray-300 px-4 py-2">{{ __('Quantity') }}</th>
            <th class="border border-gray-300 px-4 py-2">{{ __('Action') }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in materialItems" :key="index">
            <td class="border border-gray-300 px-4 py-2">
              <select v-model="item.item_group" class="w-full px-2 py-1 border rounded">
                <option v-for="group in itemGroups" :key="group.name" :value="group.name">
                  {{ group.name }}
                </option>
              </select>
            </td>
            <td class="border border-gray-300 px-4 py-2">
              <input v-model="item.quantity" type="number" class="w-full px-2 py-1 border rounded" />
            </td>
            <td class="border border-gray-300 px-4 py-2">
              <Button variant="danger" @click="removeItem(index)">{{ __('Remove') }}</Button>
            </td>
          </tr>
        </tbody>
      </table>
      <Button variant="outline" @click="addItem">{{ __('Add Item') }}</Button>
    </div>
  </template>
  
  <script setup>
  import { reactive, ref, onMounted } from 'vue'
  import { Button, createResource } from 'frappe-ui'
  
  const materialItems = reactive([
    { item_group: '', quantity: 0 },
  ])
  
  const itemGroups = ref([])
  
  const fetchItemGroups = async () => {
    try {
      const response = await createResource({
        url: 'lmscloned.lmscloned.utils.get_item_groups',
        method: 'GET',
      })
      itemGroups.value = response.data || []
    } catch (error) {
      console.error('Error fetching item groups:', error)
    }
  }
  
  onMounted(fetchItemGroups)
  
  const addItem = () => {
    materialItems.push({ item_group: '', quantity: 0 })
  }
  
  const removeItem = (index) => {
    materialItems.splice(index, 1)
  }
  
  defineExpose({ materialItems })
  </script>
  