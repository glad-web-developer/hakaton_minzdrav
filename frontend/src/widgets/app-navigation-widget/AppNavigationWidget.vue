<template>
  <v-app-bar
      dense
  >
    <div class="d-flex gap-2">
      <router-link v-if="$route.name !== 'home'" :to="{name: 'home'}" class="text-decoration-none">
        <v-btn>Перейти к протоколу</v-btn>
      </router-link>

      <v-menu
          v-else
          offset-y
      >
        <template v-slot:activator="{ attrs, on }">
          <v-btn
              v-bind="attrs"
              v-on="on"
          >
            Протокол
          </v-btn>
        </template>

        <v-list>
          <v-list-item @click="onClickShowShortProtocol">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Показать краткую информацию</v-list-item-title>
          </v-list-item>

          <v-list-item @click="onClickShowDetailProtocol">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Показать полную информацию</v-list-item-title>
          </v-list-item>

          <v-list-item @click="onClickShowOtherSpecialistProtocols">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Показать другие протоколы других специалистов</v-list-item-title>
          </v-list-item>

          <v-list-item @click="onClickShowErrorsProtocol">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Показать ошибки протокола</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-menu
          offset-y
          :close-on-content-click="false"
          :value='isShowFileMenu'
      >

        <template v-slot:activator="{ attrs, on }">
          <v-btn
              v-bind="attrs"
              v-on="on"
              @click.prevent="isShowFileMenu = true"
          >
            Файл
          </v-btn>
        </template>

        <v-list>

          <v-list-item @click="onClickCreateFile">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Создать</v-list-item-title>
          </v-list-item>

          <v-list-item @click="onClickOpenFile">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Открыть</v-list-item-title>
          </v-list-item>

          <v-list-group prepend-icon="mdi-account-circle">
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title>Экспортировать как:</v-list-item-title>
              </v-list-item-content>
            </template>

            <v-list-item link>
              <v-list-item-title>PDF</v-list-item-title>
            </v-list-item>

            <v-list-item link>
              <v-list-item-title>Word</v-list-item-title>
            </v-list-item>

            <v-list-item link>
              <v-list-item-title>Excel</v-list-item-title>
            </v-list-item>
          </v-list-group>
        </v-list>
      </v-menu>

      <v-menu offset-y>
        <template v-slot:activator="{ attrs, on }">
          <v-btn
              v-bind="attrs"
              v-on="on"
          >
            Рецепт
          </v-btn>
        </template>

        <v-list>

          <v-list-item @click="onClickCreateRecipe107">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Форма 107</v-list-item-title>
          </v-list-item>

          <v-list-item @click="onClickCreateRecipe148">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Форма 148</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-menu offset-y>
        <template v-slot:activator="{ attrs, on }">
          <v-btn
              v-bind="attrs"
              v-on="on"
          >
            Статистика
          </v-btn>
        </template>

        <v-list>

          <router-link :to="{name: 'dashboard-constructor'}" class="text-decoration-none">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-home</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Создать</v-list-item-title>
            </v-list-item>
          </router-link>

          <v-list-item @click="onClickShowSelectDashboard">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Открыть</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

    </div>

  </v-app-bar>
</template>

<script>
import Vue from "vue";

export const navigationBus = new Vue()

export default {
  name: "AppNavigationWidget",
  data() {
    return {
      isShowFileMenu: false
    }
  },
  methods: {
    onClickOpenFile(event) {
      this.isShowFileMenu = false
      navigationBus.$emit('click-open-file', event)
    },
    onClickCreateFile(event) {
      this.isShowFileMenu = false
      navigationBus.$emit('click-create-file', event)
    },
    onClickShowShortProtocol() {
      navigationBus.$emit('click-show-short-protocol-info')
    },
    onClickShowDetailProtocol() {
      navigationBus.$emit('click-show-detail-protocol-info')
    },
    onClickShowOtherSpecialistProtocols() {
      navigationBus.$emit('click-show-other-specialist-protocols')
    },
    onClickShowErrorsProtocol() {
      navigationBus.$emit('click-show-errors-protocol')
    },
    onClickCreateRecipe148() {
      navigationBus.$emit('click-create-recipe-148')
    },
    onClickCreateRecipe107() {
      navigationBus.$emit('click-create-recipe-107')
    },
    onClickShowSelectDashboard() {
      navigationBus.$emit('click-show-select-dashboard')
    }
  }
}
</script>

<style scoped>

</style>
