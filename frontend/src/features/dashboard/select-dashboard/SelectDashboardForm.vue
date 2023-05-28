<template>
  <v-overlay v-if="isLoading">
    <v-progress-circular indeterminate/>
  </v-overlay>
  <contollable-card
      v-else
      title="Дашборды"
      class="root"
      @click-close-button="$emit('click-close-button')"
      @click-rollup-button="$emit('click-rollup-button')"
  >
    <div v-if="isEmptyDashboards" class="d-flex flex-column gap-2">
      Вы еще не создали ни одной доски.
      <v-btn text :to="{name: 'dashboard-constructor'}" @click="$emit('click-close-button')">Создать доску</v-btn>
    </div>

    <v-list v-else nav dense>
      <v-list-item-group color="primary">

        <v-list-item
            @click="$emit('click-close-button')"
            v-for="dashboard in dashboards"
            :to="{ name: 'dashboard', params: { id: dashboard.id }}"
            :key="dashboard.id"
        >
          <v-list-item-avatar>
            <v-icon
                class="grey lighten-1"
                dark
            >
              mdi-folder
            </v-icon>
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title>{{ dashboard.title }}</v-list-item-title>
          </v-list-item-content>

          <v-list-item-action @click.stop.prevent="fetchDeleteDashboard(dashboard.id)">
            <v-btn icon>
              <v-icon color="red lighten-1">mdi-delete</v-icon>
            </v-btn>
          </v-list-item-action>
        </v-list-item>

      </v-list-item-group>
    </v-list>
    <v-pagination
        v-if="pages > 1"
        v-model="page"
        :length="pages"
        circle
    ></v-pagination>
    <v-snackbar v-model="isShowSnackbar">
      {{ message }}
    </v-snackbar>
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
      page: 1,
      pages: null,

      message: null,
      isShowSnackbar: false,
      isEmptyDashboards: false,

      dashboards: [],
    }
  },
  methods: {
    showMessage(message) {
      this.isShowSnackbar = true
      this.message = message
      setTimeout(() => this.isShowSnackbar = false, 1500)
    },
    async fetchAllDashboards() {
      const response = await DashboardApi.getAllDashboards(this.page)
      this.dashboards = response.results
      this.pages = Math.ceil(response.count / 9)

      if (this.dashboards.length === 0) {
        this.isEmptyDashboards = true
      }

      this.isLoading = false
    },
    async fetchDeleteDashboard(id) {
      const response = await DashboardApi.deleteDashboard(id)

      if (response.status === 204) {
        this.showMessage("Доска успешно удалена")
        this.dashboards = this.dashboards.filter(dashboard => dashboard.id !== id)
        if (this.dashboards.length === 0 && this.page > 0) {
          this.page--
        }
      } else {
        this.showMessage("Не удалось удалить доску")
      }
    }
  },
  mounted() {
    this.fetchAllDashboards()
  },
  watch: {
    page() {
      this.fetchAllDashboards()
    }
  }
}
</script>

<style scoped lang="scss">
.root {
  min-width: 80vw;
  min-height: 80vh;
}
</style>
