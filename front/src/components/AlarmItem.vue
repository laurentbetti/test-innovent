<script>
export default {
  data() {
    return {
      producerStats: [
        {
          name: 'Eolienne de Marseille',
          alarms: [
            {
              name: 'Fire in the hole',
              count: 54
            },
            {
              name: 'Chaud, cacao',
              count: 31
            }
          ]
        },
        {
          name: 'Eolienne de Montélimar',
          alarms: [
            {
              name: 'And bang bang',
              count: 167
            },
            {
              name: 'Tourne tourne, joli moulin',
              count: 89
            }
          ]
        }
      ]
    }
  },

  computed: {
    statsRows() {
      const rows = []
      for (const ps of this.producerStats) {
        // TODO: what if there is 1 or 0 alarms ?
        rows.push({
          producerName: ps.name,
          alarm: ps.alarms[0],
          key: `${ps.name - ps.alarms[0].name}`
        })
        rows.push({ alarm: ps.alarms[1], key: `${ps.name - ps.alarms[1].name}` })
      }
      return rows
    }
  }
}
</script>

<template>
  <tr v-for="row in statsRows" :key="row.key" class="table-group-divider">
    <td v-if="row.producerName" row-span="2">{{ row.producerName }}</td>
    <td v-else></td>
    <td>
      <span v-if="row.producerName" class="small">🥇</span><span v-else class="small">🥈</span
      >{{ row.alarm.name }} ({{ row.alarm.count }})
    </td>
  </tr>
</template>
