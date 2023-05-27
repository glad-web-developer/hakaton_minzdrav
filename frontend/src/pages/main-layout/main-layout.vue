<template>
  <div class="h-100">
    <app-navigation-widget/>
    <v-main class="h-100">
      <router-view class="h-100"/>
    </v-main>
    <v-overlay
        class="overlay"
        :value="overlay"
    >
      <component
          :is="overlayComponent"
          @click-close-button="onCloseHandler"
      />
    </v-overlay>
  </div>
</template>

<script>
import {AppNavigationWidget, navigationBus} from "@/widgets";
import {CreateProtocolForm, OpenProtocolForm} from "@/features/protocol"
import {CreateRecipe107, CreateRecipe148} from "@/features/recipe";
import {SelectDashboardForm} from "@/features/dashboard";
import {CreateReportTemplate} from '@/features/report'

export default {
  name: 'MainLayout',
  components: {OpenProtocolForm, AppNavigationWidget, CreateRecipe107, CreateRecipe148, CreateReportTemplate},
  data() {
    return {
      overlay: false,
      overlayComponent: null
    };
  },
  methods: {
    onClickOpenFile() {
      this.overlayComponent = OpenProtocolForm
      this.overlay = true
    },
    onClickCreateFile() {
      this.overlayComponent = CreateProtocolForm
      this.overlay = true
    },
    onCloseHandler() {
      this.overlay = false
    },
    onClickCreateRecipe107() {
      this.overlayComponent = CreateRecipe107
      this.overlay = true
    },
    onClickCreateRecipe148() {
      this.overlayComponent = CreateRecipe148
      this.overlay = true
    },
    onClickShowSelectDashboard() {
      this.overlayComponent = SelectDashboardForm
      this.overlay = true
    },
    onClickCreateReportTemplate() {
      this.overlayComponent = CreateReportTemplate
      this.overlay = true
    }
  },
  mounted() {
    navigationBus.$on('click-open-file', this.onClickOpenFile)
    navigationBus.$on('click-create-file', this.onClickCreateFile)
    navigationBus.$on('click-create-recipe-107', this.onClickCreateRecipe107)
    navigationBus.$on('click-create-recipe-148', this.onClickCreateRecipe148)
    navigationBus.$on('click-show-select-dashboard', this.onClickShowSelectDashboard)
    navigationBus.$on('click-create-report-template', this.onClickCreateReportTemplate)
  }
}
</script>

<style lang="scss">

</style>
