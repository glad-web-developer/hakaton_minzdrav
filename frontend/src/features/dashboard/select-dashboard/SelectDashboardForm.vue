<template>
  <v-progress-circular v-if="isLoading" indeterminate/>
  <contollable-card
      v-else
      title="Дашборды"
      class="root"
      @click-close-button="$emit('click-close-button')"
      @click-rollup-button="$emit('click-rollup-button')"
  >
    <v-list nav dense>
      <v-list-item-group color="primary">
        <router-link
            class="text-decoration-none"
            v-for="dashboard in dashboards"
            :to="{ name: 'dashboard', params: { id: dashboard.id }}"
            :key="dashboard.id"
        >
          <v-list-item @click="$emit('click-close-button')">
            <v-list-item-icon>
              <v-icon>mdi-table</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ dashboard.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </router-link>

      </v-list-item-group>
    </v-list>
  </contollable-card>
</template>

<script>
import {ContollableCard} from "@/share/ui/";
import DashboardApi from "@/entities/dashboard/api";

export default {
  name: "SelectDashboardForm",
  components: {ContollableCard},
  data() {
    return {
      isLoading: true,
      dashboards: [],
    }
  },
  mounted() {
    const fetchData = async () => {
      this.isLoading = true
      this.dashboards = await DashboardApi.getAllDashboards()
      this.isLoading = false
    }

    fetchData()

  }
}
</script>

<style scoped lang="scss">
.root {
  min-width: 80vw;
  min-height: 80vh;
}
</style>
