<script>
export default {
  props: {
    producer: { type: Object }
  }
}
</script>

<template>
  <tr class="table-group-divider">
    <td :row-span="producer.alarms.length">{{ producer.name }}</td>
    <td>
      <span v-if="producer.alarms.length > 0">
        <span class="small">🥇</span>{{ producer.alarms[0].name }} ({{ producer.alarms[0].count }})
      </span>
      <span v-else>No alarm reported</span>
    </td>
  </tr>

  <tr v-if="producer.alarms.length > 1">
    <td></td>
    <td>
      <span class="small">🥈</span>{{ producer.alarms[1].name }} ({{ producer.alarms[1].count }})
    </td>
  </tr>
</template>
