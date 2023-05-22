<template>
  <v-progress-circular class="mx-auto" v-if="isLoading" indeterminate/>
  <div v-else class="mt-4">
    <component
        v-for="widget in widgets"
        :key="widget.id"
        :is="widget.component"
        :x="widget.x"
        :y="widget.y"
    />
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
    this.revalidate()
  }
}
</script>

<style scoped>

</style>
