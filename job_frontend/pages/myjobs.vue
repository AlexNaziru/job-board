<script setup>
  import {onMounted} from "vue";
  import {useUserStore} from "~/stores/users.js";

  const userStore = useUserStore()
  const router = useRouter()
  let jobs = ref()

  onMounted(() => {
    if (!userStore.user.isAuthenticated) {
      router.push("/login")
    } else {
      getJobs()
    }
  })

  async function getJobs() {
    await $fetch("http://127.0.0.1:8000/api/v1/jobs/my", {
      headers: {
        "Authorization": "Token " + userStore.user.token,
        "Content-Type": "application/json"
      }
    })
        .then(response => {
          jobs.value = response
        })
        .catch(error => {
          console.log("error", error)
        })
    // Token is undefined, fix it
    console.log("Using token: ", userStore.user.token);
  }
</script>

<template>
  <div class="py-10 px-6">
    <h1 class="mb-6 text-2xl">Locuri de munca</h1>

    <div class="space-y-4">
      <Job
          v-for="job in jobs"
          :key="job.id"
          :job="job"
          :my="true"/>
    </div>
  </div>
</template>

