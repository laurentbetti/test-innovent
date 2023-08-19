<script>
export default {
  data() {
    return {
      items: []
    }
  },

  async created() {
    const res = await fetch('http://127.0.0.1:8000/alarms/report/', {
      mode: 'cors'
    })
    this.items = await res.json()
  }
}
</script>

<template>
  <main><h1>This is the Alarm Report</h1></main>
  <li v-for="i in items" :key="i.id">
    <pre>{{ JSON.stringify(i) }}</pre>
  </li>
</template>
