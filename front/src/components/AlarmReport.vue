<script>
import AlarmItem from './AlarmItem.vue'
export default {
  components: {
    AlarmItem
  },
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
  <main>
    <h1 class="">Alarm report</h1>
    <table class="table table-bordered align-middle caption-top">
      <caption>
        Top 2 alarm events by publisher
      </caption>
      <thead class="table-light">
        <tr>
          <th>Publisher</th>
          <th>Top 2 alarms (# occurences)</th>
        </tr>
      </thead>
      <tbody>
        <AlarmItem />
      </tbody>
    </table>
  </main>
</template>

<style>
main {
  max-width: 600px;
}
</style>
