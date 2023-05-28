<template>
  <v-app-bar dense class="bg" app>
    <img width="32" height="32" src="/logo.svg"/>
    <v-btn-toggle background-color="transparent" tile group>
      <v-btn v-if="$route.name !== 'home'" @click="$router.push({name: 'home'})" link text class="text-white">Протокол
      </v-btn>

      <v-menu
          v-else
          offset-y
      >
        <template v-slot:activator="{ attrs, on }">
          <v-btn
              class="text-white"
              link
              text
              v-bind="attrs"
              v-on="on"
          >
            Протокол
          </v-btn>
        </template>

        <v-list>
          <v-list-item @click="onClickShowShortProtocol">
            <v-list-item-icon>
              <v-icon>mdi-information-variant</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Показать краткую информацию</v-list-item-title>
          </v-list-item>

          <v-list-item @click="onClickShowDetailProtocol">
            <v-list-item-icon>
              <v-icon>mdi-information-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Показать полную информацию</v-list-item-title>
          </v-list-item>

          <!--          <v-list-item @click="onClickShowOtherSpecialistProtocols">-->
          <!--            <v-list-item-icon>-->
          <!--              <v-icon>mdi-file-table-box-multiple-outline</v-icon>-->
          <!--            </v-list-item-icon>-->
          <!--            <v-list-item-title>Показать другие протоколы других специалистов</v-list-item-title>-->
          <!--          </v-list-item>-->

          <!--          <v-list-item @click="onClickShowErrorsProtocol">-->
          <!--            <v-list-item-icon>-->
          <!--              <v-icon>mdi-alert-remove-outline</v-icon>-->
          <!--            </v-list-item-icon>-->
          <!--            <v-list-item-title>Показать ошибки протокола</v-list-item-title>-->
          <!--          </v-list-item>-->
        </v-list>
      </v-menu>

      <v-menu
          offset-y
          v-model='isShowFileMenu'
          :close-on-content-click="false"
      >

        <template v-slot:activator="{ attrs, on }">
          <v-btn
              class="text-white"
              text
              link
              v-bind="attrs"
              v-on="on"
          >
            Файл
          </v-btn>
        </template>

        <v-list>
          <v-list-item @click="onClickOpenFile">
            <v-list-item-icon>
              <v-icon>mdi-open-in-new</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Открыть</v-list-item-title>
          </v-list-item>

          <v-list-item @click="onClickImportProtocol">
            <v-list-item-icon>
              <v-icon>mdi-import</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Импортировать</v-list-item-title>
          </v-list-item>

          <v-list-group prepend-icon="mdi-export-variant">
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title>Экспортировать как:</v-list-item-title>
              </v-list-item-content>
            </template>

            <v-list-item link>
              <v-list-item-title>
                <a :href="`${backend}${$store.state.protocol.packExcelSrc}`" download>Excel</a>
              </v-list-item-title>
            </v-list-item>
          </v-list-group>
        </v-list>
      </v-menu>

<!--      <v-menu offset-y>-->
<!--        <template v-slot:activator="{ attrs, on }">-->
<!--          <v-btn-->
<!--              class="text-white"-->
<!--              text-->
<!--              link-->
<!--              v-bind="attrs"-->
<!--              v-on="on"-->
<!--          >-->
<!--            Рецепт-->
<!--          </v-btn>-->
<!--        </template>-->

<!--        <v-list>-->

<!--          <v-list-item @click="onClickCreateRecipe107">-->
<!--            <v-list-item-icon>-->
<!--              <v-icon>mdi-card-account-details-outline</v-icon>-->
<!--            </v-list-item-icon>-->
<!--            <v-list-item-title>Форма 107</v-list-item-title>-->
<!--          </v-list-item>-->

<!--          <v-list-item @click="onClickCreateRecipe148">-->
<!--            <v-list-item-icon>-->
<!--              <v-icon>mdi-card-account-details-outline</v-icon>-->
<!--            </v-list-item-icon>-->
<!--            <v-list-item-title>Форма 148</v-list-item-title>-->
<!--          </v-list-item>-->
<!--        </v-list>-->
<!--      </v-menu>-->

      <v-menu offset-y>
        <template v-slot:activator="{ attrs, on }">
          <v-btn
              class="text-white"
              text
              link
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
                <v-icon>mdi-pencil-outline</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Создать доску</v-list-item-title>
            </v-list-item>
          </router-link>

          <v-list-item @click="onClickShowSelectDashboard">
            <v-list-item-icon>
              <v-icon>mdi-open-in-new</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Открыть доску</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

<!--      <v-menu offset-y>-->
<!--        <template v-slot:activator="{ attrs, on }">-->
<!--          <v-btn-->
<!--              class="text-white"-->
<!--              text-->
<!--              link-->
<!--              v-bind="attrs"-->
<!--              v-on="on"-->
<!--          >-->
<!--            Отчетность-->
<!--          </v-btn>-->
<!--        </template>-->
<!--        <v-list>-->

<!--          <v-list-item @click="onClickCreateReportTemplate">-->
<!--            <v-list-item-icon>-->
<!--              <v-icon>mdi-pencil-outline</v-icon>-->
<!--            </v-list-item-icon>-->
<!--            <v-list-item-title>Создать шаблон отчета</v-list-item-title>-->
<!--          </v-list-item>-->

<!--          <v-list-item @click="onClickCreateReport">-->
<!--            <v-list-item-icon>-->
<!--              <v-icon>mdi-open-in-new</v-icon>-->
<!--            </v-list-item-icon>-->
<!--            <v-list-item-title>Сформировать отчет по шаблону</v-list-item-title>-->
<!--          </v-list-item>-->
<!--        </v-list>-->
<!--      </v-menu>-->

    </v-btn-toggle>
    <div class="ml-auto">
      <a :href="`${origin}/admin/`" class="text-decoration-none">
        <v-btn
            class="text-white"
            text
            link
        >
          Админ панель
        </v-btn>
      </a>

      <logout-button class="ml-auto"/>

    </div>
  </v-app-bar>
</template>

<script>
import Vue from "vue";
import {LogoutButton} from "@/features/auth";
import BaseApi from '@/share/api'

export const navigationBus = new Vue()

export default {
  name: "AppNavigationWidget",
  components: {LogoutButton},
  data() {
    return {
      isShowFileMenu: false,
      value: 1,
      backend: BaseApi.basePath,
      origin: BaseApi.origin,
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
    },
    onClickCreateReportTemplate() {
      navigationBus.$emit('click-create-report-template')
    },
    onClickCreateReport() {
      navigationBus.$emit('click-create-report')
    },
    onClickImportProtocol() {
      this.isShowFileMenu = false
      navigationBus.$emit('click-import-protocol')
    }
  }
}
</script>

<style scoped>
.bg {
  background-color: #8BC6EC;
  background-image: linear-gradient(135deg, #8BC6EC 0%, #9599E2 100%);

}
</style>
