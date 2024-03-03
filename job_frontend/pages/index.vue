<script setup>
  const {data: jobs} = await useFetch("http://127.0.0.1:8000/api/v1/jobs/newest/")
</script>

<template>
<!-- Front page -->
  <div class="relative px-6 py-5 lg:py-15">
    <img src="/static/job.jpg" alt="Your Image Description" class="w-full h-96 object-cover">
    <div class="absolute top-0 left-0 right-0 bottom-0 bg-opacity-50 flex items-center justify-center">
      <div class="text-center">
        <p class="mb-2 text-3xl lg:text-5xl text-white">Cauti un job?</p>
        <p class="mb-10 text-white font-semibold">Cauta un job bazat pe aptitudinile tale</p>
        <NuxtLink to="/browse" class="inline-block px-8 py-4 rounded-xl bg-white text-emerald-500 hover:bg-gray-200">Cauta</NuxtLink>
      </div>
    </div>
  </div>

  <div class="py-5 px-6">
    <h2 class="mb-8 text-2xl text-center">Cele mai recente</h2>

    <div class="space-y-4">
      <Job v-for="job in jobs" v-bind:key="job.id" v-bind:job="job" />
    </div>



  </div>


</template>
