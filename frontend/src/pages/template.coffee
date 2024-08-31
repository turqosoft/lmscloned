<template>
<div class="">
		<header
			class="sticky top-0 z-10 flex items-center justify-between border-b bg-white px-3 py-2.5 sm:px-5"
		>
			<Breadcrumbs
				class="h-7"
				:items="[{ label: __('Requirements'), route: { name: 'Requirements' } }]"
			/>
			<div class="flex space-x-2">
				<div class="w-40">
					<Select
						v-if="categories.data?.length"
						v-model="currentCategory"
						:options="categories.data"
						:placeholder="__('Filter')"
					/>
				</div>
				<router-link
					v-if="user.data?.is_moderator"
					:to="{
						name: 'CreateRequirement',
						params: { materialrequirementName: 'new' },
					}"
				>
                <Button variant="solid">
						<template #prefix>
							<Plus class="h-4 w-4 stroke-1.5" />
						</template>
						{{ __('New') }}
					</Button>
				</router-link>
			</div>