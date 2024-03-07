<script setup>
import {onMounted} from "vue";
import {useUserStore} from "~/stores/users.js";

const userStore = useUserStore()
onMounted(() => {
  userStore.initStore()
})
</script>

<template>
  <div>
<!-- default layout loads -->
   <NuxtLayout>
<!-- loads everything -->
     <NuxtPage />
   </NuxtLayout>
  </div>
</template>
