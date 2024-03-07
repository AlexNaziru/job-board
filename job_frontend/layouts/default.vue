<script setup>
  import {useUserStore} from "~/stores/users.js";
  const userStore = useUserStore()

  function logout() {
    userStore.removeToken()
  }
</script>

<template>
  <div>
    <nav class="p-6 flex items-center justify-between bg-gray-700">
      <NuxtLink to="/" class="text-xl text-white hover:text-gray-300"> Job Market </NuxtLink>
      <div class="flex items-center space-x-4">
        <NuxtLink to="/" class="text-white hover:text-gray-300">Acasa</NuxtLink>
        <NuxtLink to="/browse" class="text-white hover:text-gray-300">Cauta</NuxtLink>
      </div>
    </nav>
<!--  when we use this component, will be rendered into slot, and will come from this default file into other components  -->
    <slot />

  <footer class="p-3 flex flex-wrap items-center justify-between bg-gray-700 inset-x-0 bottom-0">
      <p class="text-gray-300">Copyright 2024 - Job Market</p>
    <div class="flex mt-6 md:mt-0 items-center space-x-4">
      <template v-if="userStore.user.isAuthenticated">
        <NuxtLink to="/myjobs" class="py-4 px-6 bg-green-500 hover:bg-green-600 text-white rounded-xl">Job-urile mele</NuxtLink>
        <NuxtLink to="/create-job" class="py-4 px-6 bg-green-500 hover:bg-green-600 text-white rounded-xl">Creeaza</NuxtLink>
        <a v-on:click="logout" class="py-4 px-6 bg-rose-500 hover:bg-rose-600 text-white rounded-xl">Deconectare</a>
      </template>

      <template v-else>
        <NuxtLink to="/login" class="py-4 px-6 bg-green-500 hover:bg-green-600 text-white rounded-xl">Logare</NuxtLink>
        <NuxtLink to="/signup" class="py-4 px-6 bg-green-500 hover:bg-green-600 text-white rounded-xl">Sign up</NuxtLink>
      </template>
    </div>
  </footer>
  </div>
</template>
