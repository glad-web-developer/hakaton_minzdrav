<template>
  <div>
    <div v-if="isLoad">
      <div class="py-3 light-blue top-navbar">
        <div class="container-fluid ">
          <div class="d-flex">
            <div class="">

              <v-btn
                  color="white"
                  elevation="6"
                  class="mr-3 searchButton"
                  small
              >
                <v-icon class="mr-1" dense>mdi mdi-account-search</v-icon>
                Поиск
              </v-btn>
              <v-btn
                  color="white"
                  elevation="6"
                  class="mr-3"
                  small
              >
                <v-icon class="mr-1"> mdi mdi-menu</v-icon>
                Столбцы
              </v-btn>
              <v-btn

                  color="white"
                  elevation="6"
                  class="mr-3 ml-3"
                  small>
                <v-icon class="mr-1"> mdi mdi-account-multiple-plus-outline</v-icon>
                Новая беременная
              </v-btn>
              <v-btn
                  color="white"
                  elevation="6"
                  class="mr-3"
                  small>
                <v-icon class="mr-1">mdi mdi-refresh</v-icon>
                Обновить
              </v-btn>
              <v-btn

                  color="white"
                  elevation="6"
                  class="mr-3 ml-3"
                  small
              >
                <v-icon class="mr-1" dense> mdi mdi-send</v-icon>
                Переводы
              </v-btn>
              <v-btn

                  color="white"
                  elevation="6"
                  small>
                <v-icon class="mr-1" dense> mdi mdi-file-document</v-icon>
                Отчеты
              </v-btn>
            </div>
            <div class="ml-auto text-right">
              <v-btn
                  color="white"
                  elevation="6"
                  class=""
                  small
                  @click="logout()"
              >
                <v-icon class="mr-1">mdi mdi-logout</v-icon>
                {{ user.userName }}
              </v-btn>
            </div>
          </div>
        </div>
      </div>

      <v-alert
          type="success"
      >
        <a href="https://v2.vuetifyjs.com/en/components/alerts/">https://v2.vuetifyjs.com/en/components/alerts/</a>
      </v-alert>

    </div>

    <div v-else>
      <app-loader-page/>
    </div>

  </div>
</template>

<script>
import CookieHelper from "@/plugins/cookieHelper";

import AppLoaderPage from "@/components/AppLoaderPage";

export default {
  name: "HomeView",
  components: {
    AppLoaderPage,
  },

  props: {
    user: {
      type: Object,
    }
  },

  data() {
    return {
      isLoad: false,
    }
  },


  methods: {
    logout() {
      CookieHelper.setCookie('sessionid', "", {
        'max-age': -1
      })
      location.reload();
    },

  },

  created: async function () {
    this.isLoad = true;
  }
}
</script>

<style scoped>

</style>