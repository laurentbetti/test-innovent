<script>
export default {
  data() {
    return {
      items: [
        { id: 1, name: 'Pouet' },
        { id: 2, name: 'Plouf' }
      ]
    }
  }
}
</script>

<template>
  <main><h1>This is the Alarm Report</h1></main>
  <li v-for="i in items" :key="i.id">
    <a>Name: {{ i.name }}</a>
  </li>
</template>
