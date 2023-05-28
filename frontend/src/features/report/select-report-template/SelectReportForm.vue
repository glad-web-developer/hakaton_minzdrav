<template>
  <v-progress-circular v-if="isLoading" indeterminate/>
  <contollable-card
      v-else
      title="Шаблоны отчетов"
      class="root"
      @click-close-button="$emit('click-close-button')"
      @click-rollup-button="$emit('click-rollup-button')"
  >
    <v-list nav dense>
      <v-list-item-group color="primary">
        <a
            v-for="template in templates"
            class="text-decoration-none"
            :href="template.src"
            :key="template.id"
        >
          <v-list-item @click="$emit('click-close-button')">
            <v-list-item-icon>
              <v-icon>mdi-table</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ template.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </a>

      </v-list-item-group>
    </v-list>
  </contollable-card>
</template>

<script>
import {ContollableCard} from "@/share/ui/";
import ReportApi from "@/entities/report/api";

export default {
  name: "SelectReportForm",
  components: {ContollableCard},
  data() {
    return {
      isLoading: true,
      templates: [],
    }
  },
  mounted() {
    const fetchData = async () => {
      this.isLoading = true
      this.templates = await ReportApi.getAllTemplates()
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
