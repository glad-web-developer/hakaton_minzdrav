<template>
  <div>
    <v-overlay v-if="isLoading">
      <v-progress-circular indeterminate/>
    </v-overlay>

    <v-container fluid class="mw-100 pt-0">
      <v-row class="h-100">
        <v-col class="h-100" ref="content">
          <vue-draggable-resizable
              class="border-0"
              w="auto"
              h="auto"
              v-for="widget in widgets"
              :key="widget.id"
              :x="widget.x"
              :y="widget.y"
              :grid="[grid,grid]"
              :parent="true"
              :resizable="false"
              :draggable="false"
          >
            <div :style="{width: `${widget.cols * grid}px`}">
              <v-card>
                <v-card-title>{{ widget.title }}</v-card-title>
                <v-card-text>
                  <component
                      :is="widget.component"
                      :x="widget.x"
                      :y="widget.y"
                  />
                </v-card-text>
              </v-card>
            </div>
          </vue-draggable-resizable>
        </v-col>
      </v-row>
    </v-container>


  </div>
</template>

<script>
import DashboardApi from "@/entities/dashboard/api";
import {MorbidityBChartWidget, MorbidityCChartWidget} from '@/widgets'

export default {
  name: "DashboardPage",
  props: {
    id: [String, Number]
  },
  components: {MorbidityBChartWidget, MorbidityCChartWidget},
  data() {
    return {
      isLoading: true,
      widgets: [],
      grid: null
    }
  },
  methods: {
    revalidate() {
      const fetchData = async () => {
        this.isLoading = true
        const {widgets} = await DashboardApi.getDashboardById(this.id)
        this.widgets = widgets
        this.isLoading = false
      }

      fetchData()
    }
  },
  watch: {
    id() {
      this.revalidate()
    }
  },
  mounted() {
    const pl = parseInt(window.getComputedStyle(this.$refs.content, null).paddingLeft.split('px')[0], 10)
    const pr = parseInt(window.getComputedStyle(this.$refs.content, null).paddingRight.split('px')[0], 10)
    const width = this.$refs.content.getBoundingClientRect().width

    const innerWidth = width - pl - pr

    this.grid = innerWidth / 32

    this.revalidate()
  }
}
</script>

<style scoped>

</style>
