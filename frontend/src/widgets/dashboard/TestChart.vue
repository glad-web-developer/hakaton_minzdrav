<template>
  <Bar
      id="my-chart-id"
      :options="chartOptions"
      :chartData="chartData"
  />
</template>

<script>

import {Bar} from 'vue-chartjs/legacy'
import {BarElement, CategoryScale, Chart as ChartJS, Legend, LinearScale, Title, Tooltip} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: "TestChart",
  components: {Bar},
  data() {
    return {
      chartData: {
        labels: ['January', 'February', 'March'],
        datasets: [{data: [40, 20, 12]}]
      },
      chartOptions: {
        responsive: true
      }
    }
  }
}
</script>

<style scoped>

</style>
