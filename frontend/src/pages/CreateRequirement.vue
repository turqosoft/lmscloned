<template>
  <div>
    <header class="sticky top-0 z-10 flex items-center justify-between border-b bg-white px-3 py-2.5 sm:px-5">
      <Breadcrumbs class="h-7" :items="breadcrumbs" />
      <Button variant="solid" @click="saveRequirement">
        {{ __('Save') }}
      </Button>
    </header>
    <div class="w-full max-w-4xl mx-auto py-5">
      <!-- Form Controls -->
      <div>
        <div class="text-lg font-semibold mb-4">
          {{ __('Create Requirement') }}
        </div>
        <div class="grid grid-cols-2 gap-10 mb-4">
          <div>
            <FormControl
              v-model="requirementData.username"
              :label="__('Username')"
              class="mb-4"
              readonly
            />
            <FormControl
              v-model="requirementData.user_types"
              :label="__('User Types')" 
              class="mb-4"
            />
            <FormControl
              v-model="requirementData.customer_info"
              :label="__('Customer Info')"
              class="mb-4"
            />
            <FormControl
              v-model="requirementData.branchs"
              :label="__('Branch')"
              class="mb-4"
            />
            <FormControl
              v-model="requirementData.schedule_date"
              :label="__('Required By')"
              type="date"
              class="mb-4"
            />
          </div>
        </div>

        <!-- Item Groups List with Box Styling -->
        <div class="grid gap-4 mb-4">
          <div v-for="(group, index) in itemGroups" :key="index" class="border rounded-lg p-4 bg-gray-50 cursor-pointer" @click="showPopup(group)">
            <h2 class="text-lg font-semibold mb-2">{{ group.name }}</h2>
          </div>
        </div>

        <!-- Child Table for Material Requirement Item -->
        <div class="border rounded-lg overflow-hidden">
          <table class="w-full border-collapse">
            <thead>
              <tr class="bg-gray-200">
                <th class="border px-4 py-2">Item Group</th>
                <th class="border px-4 py-2">Qty</th>
                <th class="border px-4 py-2">UOM</th>
                <th class="border px-4 py-2">Notes</th>
                <th class="border px-4 py-2">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(entry, index) in requirementData.items" :key="index">
                <td class="border px-4 py-2">
                  {{ entry.item_group }}
                </td>
                <td class="border px-4 py-2">
                  <input v-model.number="entry.qty" type="number" class="w-full" />
                </td>
                <td class="border px-4 py-2">
                  <input v-model="entry.uom" class="w-full" />
                </td>
                <td class="border px-4 py-2">
                  <input v-model="entry.notes" class="w-full" />
                </td>
                <td class="border px-4 py-2">
                  <Button variant="outline" @click="removeItem(index)">
                    {{ __('Remove') }}
                  </Button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Popup for Item Group Details -->
        <div v-if="selectedGroup" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
          <div class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full">
            <h3 class="text-xl font-semibold mb-4">{{ selectedGroup.name }}</h3>
            <FormControl
              v-model="popupData.quantity"
              :label="__('Quantity')"
              class="mb-4"
              type="number"
            />
            <FormControl
              v-model="popupData.uom"
              :label="__('UOM')"
              class="mb-4"
            />
            <FormControl
              v-model="popupData.notes"
              :label="__('Notes')"
              class="mb-4"
            />
            <div class="flex justify-end">
              <Button variant="solid" @click="addToCart">
                {{ __('Add to Cart') }}
              </Button>
              <Button variant="outline" @click="closePopup" class="ml-2">
                {{ __('Close') }}
              </Button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="successMessage" class="fixed bottom-5 right-5 p-4 bg-green-500 text-white rounded-lg">
      {{ successMessage }}
    </div>
  </div>
</template>


<script setup>
import { reactive, ref, onMounted } from 'vue'
import {
  Breadcrumbs,
  FormControl,
  Button,
  createResource,
} from 'frappe-ui'
import { showToast } from '../utils'

// Reactive state for requirement data
const requirementData = reactive({
  username: '',
  user_types: '',
  customer_info: '',
  branchs: '',
  schedule_date: '',
  items: [], // Child table for items
})

// Reactive state for popup
const selectedGroup = ref(null)
const popupData = reactive({
  quantity: '',
  uom: '',
  notes: ''
})

// Item Groups Data (Will be fetched from API)
const itemGroups = ref([])

// Resource for fetching item groups
const itemGroupsResource = createResource({
  url: 'lmscloned.lmscloned.utils.get_item_groups', 
  cache: ['itemGroups'],
  auto: true, // Auto fetch when component mounts
})

// Resource for fetching user details
const userDetails = createResource({
  url: 'lmscloned.lmscloned.utils.get_user_details', 
  cache: ['userDetails'],
  auto: true, // Auto fetch when component mounts
})

// Resource for saving the requirements
const saveResource = createResource({
  url: 'frappe.client.insert',
  method: 'POST',
  makeParams() {
    return {
      doc: {
        doctype: 'Material Requirement',
        ...requirementData,
        items: requirementData.items.map(item => ({
          qty: item.qty,
          uom: item.uom,
          notes: item.notes,
          item_group: item.item_group, // Ensure item_group is included
        })),
      },
    }
  },
  cache: false, // Do not cache POST requests
})

// Success message ref
const successMessage = ref('')

// Fetch item groups
const fetchItemGroups = () => {
  itemGroupsResource.fetch().then(response => {
    itemGroups.value = response || [] // Default to empty array if response is undefined
  }).catch(error => {
    console.error('Error fetching item groups:', error.message || 'Unknown error')
    showToast('Error', 'Error fetching item groups', 'x')
  })
}

// Fetch user details
const fetchUserDetails = () => {
  userDetails.fetch().then(response => {
    requirementData.username = response.username
    requirementData.user_types = response.user_types
    requirementData.customer_info = response.customer_info
    requirementData.branchs = response.branchs
  }).catch(error => {
    console.error('Error fetching user details:', error.message || 'Unknown error')
    showToast('Error', 'Error fetching user details', 'x')
  })
}

// Save the requirement data
const saveRequirement = async () => {
  try {
    console.log('Requirement Data:', requirementData) // Log the data
    await saveResource.submit(
      {},
      {
        onSuccess(data) {
          successMessage.value = 'Material Requirement saved successfully!'
          console.log('Save response data:', data)
          // Clear form data
          requirementData.username = ''
          requirementData.user_types = ''
          requirementData.customer_info = ''
          requirementData.branchs = ''
          requirementData.schedule_date = ''
          requirementData.items = [] // Clear items
        },
        onError(err) {
          console.error('Error saving requirement:', err.messages?.[0] || err)
          showToast('Error', err.messages?.[0] || err, 'x')
        },
      }
    )
  } catch (err) {
    console.error('Error saving requirement:', err.message || 'Unknown error')
    showToast('Error', err.message || 'Error saving requirement', 'x')
  }
}

// Add the item to the cart and close popup
const addToCart = () => {
  if (popupData.quantity && popupData.uom) {
    requirementData.items.push({
      item_group: selectedGroup.value.name, // Use item_group instead of group_name
      qty: popupData.quantity,
      uom: popupData.uom,
      notes: popupData.notes,
    })
    closePopup()
  } else {
    showToast('Error', 'Quantity and UOM are required', 'x')
  }
}

// Show popup with group details
const showPopup = (group) => {
  selectedGroup.value = group
}

// Close popup and reset popup data
const closePopup = () => {
  selectedGroup.value = null
  popupData.quantity = ''
  popupData.uom = ''
  popupData.notes = ''
}

// Remove item from items list
const removeItem = (index) => {
  requirementData.items.splice(index, 1)
}

// On component mount, fetch item groups and user details
onMounted(() => {
  fetchItemGroups()
  fetchUserDetails()
})

</script>
