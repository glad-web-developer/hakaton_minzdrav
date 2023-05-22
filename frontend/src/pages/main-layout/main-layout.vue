<template>
  <div class="d-flex flex-column h-100">
    <app-navigation-widget class="flex-grow-0"/>
    <router-view class="flex-grow-1"/>
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

export default {
  name: 'MainLayout',
  components: {OpenProtocolForm, AppNavigationWidget, CreateRecipe107, CreateRecipe148},
  data() {
    return {
      overlay: false,
      overlayComponent: undefined
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
    }
  },
  mounted() {
    navigationBus.$on('click-open-file', this.onClickOpenFile)
    navigationBus.$on('click-create-file', this.onClickCreateFile)
    navigationBus.$on('click-create-recipe-107', this.onClickCreateRecipe107)
    navigationBus.$on('click-create-recipe-148', this.onClickCreateRecipe148)
    navigationBus.$on('click-show-select-dashboard', this.onClickShowSelectDashboard)
  }
}
</script>

<style scoped lang="scss">

</style>
