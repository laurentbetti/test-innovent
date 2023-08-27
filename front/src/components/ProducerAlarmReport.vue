<script>
export default {
  props: {
    producer: { type: Object }
  }
}
</script>

<template>
  <tr class="first-alarm-row">
    <td :rowspan="producer.alarms.length || 1">
      {{ producer.name }}
    </td>
    <td>
      <span v-if="producer.alarms.length > 0">
        🥇&nbsp;{{ producer.alarms[0].name }}&nbsp;&nbsp;
        <span class="badge bg-primary">{{ producer.alarms[0].count }}</span>
      </span>
      <span v-else class="badge bg-secondary">No alarm reported</span>
    </td>
  </tr>

  <tr v-if="producer.alarms.length > 1" class="second-alarm-row">
    <td>
      🥈&nbsp;{{ producer.alarms[1].name }}&nbsp;&nbsp;<span class="badge bg-primary">{{
        producer.alarms[1].count
      }}</span>
    </td>
  </tr>
</template>

<style>
.first-alarm-row:not(:last-of-type),
.first-alarm-row:not(:last-of-type) td {
  border-bottom: none;
}

.second-alarm-row,
.seconde-alarm-row td {
  border-top: 1px dashed var(--bs-border-color);
}
</style>
