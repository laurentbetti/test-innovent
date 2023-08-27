<script>
import ProducerAlarmReport from './ProducerAlarmReport.vue'
export default {
  components: {
    ProducerAlarmReport
  },
  data() {
    return {
      producerAlarms: [],
      page: 1
    }
  },

  async created() {
    this.producerAlarms = await this.fetchData()
  },

  methods: {
    async fetchData() {
      const res = await fetch(`http://127.0.0.1:8000/alarms/report?page=${this.page}`, {
        mode: 'cors'
      })
      return await res.json()
    },

    async loadMore() {
      this.page++
      const newData = await this.fetchData()
      this.producerAlarms = [...this.producerAlarms, ...newData]
    }
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
          <th>Top 2 alarms (# triggers)</th>
        </tr>
      </thead>
      <tbody>
        <ProducerAlarmReport
          v-for="producer in producerAlarms"
          :key="producer.id"
          :producer="producer"
        ></ProducerAlarmReport>
      </tbody>
    </table>
    <button class="btn btn-primary" @click="loadMore">Voir plus</button>
  </main>
</template>

<style>
main {
  max-width: 600px;
}
</style>
