<template>
  <vue-draggable-resizable
      class="border-0"
      :w="500"
      :h="200"
      :grid="[50,50]"
      :parent="true"
      :resizable="false"
      @dragging="onDragging"
  >
    <contollable-card
        class="root"
        title="График гепатит С"
        @click-close-button="$emit('close')"
    >
      <v-sheet
          class="v-sheet--offset mx-auto"
          color="cyan"
          elevation="12"
          max-width="calc(100% - 32px)"
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
    </contollable-card>
  </vue-draggable-resizable>
</template>

<script>
import {ContollableCard} from '@/share/ui'

export default {
  name: "MorbidityCChartWidget",
  components: {ContollableCard},
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
  methods: {
    onDragging(x, y) {
      this.$emit('dragging', x, y)
    }
  }
}
</script>

<style scoped>
.root {
  height: 100%;
  cursor: pointer;
}
</style>
