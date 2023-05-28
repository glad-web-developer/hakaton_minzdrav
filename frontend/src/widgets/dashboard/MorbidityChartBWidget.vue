<template>
  <v-sheet
      class="root"
      color="cyan"
      elevation="12"
      rounded
  >
    <v-sparkline
        class="px-2"
        :labels="labels"
        :value="value"
        color="white"
        line-width="1"
        label-size="2"
        auto-draw
    ></v-sparkline>
  </v-sheet>
</template>

<script>

export default {
  name: "MorbidityBChartWidget",
  props: ['x', 'y'],
  data() {
    return {
      labels: [
        '2016',
        '2017',
        '2018',
        '2019',
        '2020',
        '2021',
        '2022',
        '2023',
      ],
      value: [
        200,
        675,
        410,
        390,
        310,
        460,
        250,
        240,
      ],
    }
  },
}
</script>

<style scoped>
.root {
  width: 400px;
}
</style>
