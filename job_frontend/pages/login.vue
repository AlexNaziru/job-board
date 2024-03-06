<script setup>
import {useUserStore} from "~/stores/users.js";

const router = useRouter()
const userStore = useUserStore()

let email =  ref("")
let password = ref("")
let errors = ref([])

async function submitForm() {
  console.log("submitForm")
  errors.value = []
  await $fetch("http://127.0.0.1:8000/api/v1/auth/token/login/", {
    method: "POST",
    body: {
      username: email.value,
      password: password.value,
    }
  }).then(data => {
    console.log("response", data.authtoken)

    userStore.setToken(data.authtoken, email.value)

    router.push({path: "/"})
  }).catch(error => {
      if (error.response) {
        for (const property in error.response.data) {
          errors.value.push(`${property}: ${error.response._data[property]}`)
        }
        console.log(JSON.stringify(error.response))
      } else if (error.message) {
        errors.value.push("Something went wrong, try again.")
        console.log(JSON.stringify(error))
      }
  })
}

</script>


<template>
  <div class="py-10 px-6">
    <div class="mx-auto max-w-sm py-10 px-6 bg-gray-100 rounded-xl">
      <h2 class="mb-6 text-2xl">Logare</h2>
      <form v-on:submit.prevent="submitForm">
        <input v-model="email" type="email" placeholder="E-mail" class="w-full mb-4 py-4 px-6 rounded-xl">
        <input v-model="password" type="password" placeholder="Parola" class="w-full mb-4 py-4 px-6 rounded-xl">

        <div v-if="errors.length"
             class="mb-6 py-4 px-6 bg-rose-600 text-white rounded-xl">
          <p v-for="error in errors" v-bind:key="error">{{error}}</p>
        </div>

        <button class="py-4 px-6 bg-green-500 text-white rounded-xl">Logare</button>
      </form>
    </div>
  </div>
</template>
