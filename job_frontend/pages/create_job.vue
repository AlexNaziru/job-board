

<template>
  <div class="py-10 px-6">
    <h1 class="mb-6 text-2xl">Creaza un loc de munca</h1>

    <form class="space-y-4">
      <div>
        <label>Categorie</label>

        <select class="w-full mt-2 p-4 rounded-xl bg-gray-100">
          <option value="">Selecteaza categoria</option>
          <option value="cat1">Categoria 1</option>
          <option value="cat2">Categoria 2</option>
        </select>
      </div>

      <div>
        <label>Ttilu</label>
        <input type="text" class="w-full mt-2 p-4 rounded-xl bg-gray-100">
      </div>

      <div>
        <label>Descrierea postului</label>
        <textarea type="text" class="w-full mt-2 p-4 rounded-xl bg-gray-100"></textarea>
      </div>

      <div>
        <label>Salariu</label>
        <input type="text" class="w-full mt-2 p-4 rounded-xl bg-gray-100"/>
      </div>

      <div>
        <label>Locatia</label>
        <input type="text" class="w-full mt-2 p-4 rounded-xl bg-gray-100"/>
      </div>

      <div>
        <label>Numele Companiei</label>
        <input type="text" class="w-full mt-2 p-4 rounded-xl bg-gray-100"/>
      </div>

      <div>
        <label>Locatia Companiei</label>
        <input type="text" class="w-full mt-2 p-4 rounded-xl bg-gray-100"/>
      </div>

      <div>
        <label>Date de contact</label>
        <input type="text" class="w-full mt-2 p-4 rounded-xl bg-gray-100"/>
      </div>

      <button class="py-4 px-6 bg-green-500 text-white rounded-xl">Aplica</button>

    </form>
  </div>
</template>

<script setup lang="ts">
</script>