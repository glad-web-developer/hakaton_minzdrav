<template>
  <div id="app">
    <v-app class="w-100">



      <v-main>


        <router-view
            @loadComplete="isLoad = true"
            :user="user"
            @showAlert="showAlert($event)"
        />


        <v-snackbar
            color="white"
            v-model="snackbar"
        >
          <span class="text-dark"><b>{{ snackbarText }}</b></span>

          <template v-slot:action="{ attrs }">
            <v-btn
                color="blue accent-2"
                tile
                v-bind="attrs"
                @click="snackbar = false"
            >
              Ок
            </v-btn>
          </template>
        </v-snackbar>

      </v-main>
    </v-app>

  </div>
</template>

<style lang="scss" src="./assets/style.scss">
</style>

<script>

import LOCAL_CONFIG from "@/store/LOCAL_CONFIG";
import CookieHelper from "@/plugins/cookieHelper";

export default {

  data() {
    return {
      isLogin: false,
      isLoad: false,
      user: {
        isAdmin: false,
        userName: ''
      },

      counter: 0,

      snackbar: false,
      snackbarText: ""
    }
  },

  created: async function () {
    await this.checkUser();
  },

  methods: {

    showAlert(text) {
      this.snackbar = true
      this.snackbarText = text;
    },

    async checkUser() {
      const sessionId = CookieHelper.getCookie('sessionid');
      if (sessionId === undefined) {
        this.isLogin = false;
        if (window.location.href.indexOf("/login") === -1) {
          window.location.href = '/#/login'
        }

      }

      const url = LOCAL_CONFIG.urls.checkUser;
      const response = await fetch(url, {method: 'get'});
      try {
        const user = await response.json();
        if (user.isLogin === true) {
          if (window.location.href.indexOf("/#/login") > -1) {
            window.location.href = '/'
          }
          this.isLogin = true;
          this.user = {
            userName: user['userName'],
            isAdmin: user['isAdmin']
          }
        } else {
          if (window.location.href.indexOf("/login") === -1) {
            window.location.href = '/#/login'
          }
        }
      } catch (e) {
        alert(1)
        this.showAlert('Ошибка при обращение к серверу авториации');
      }

    }
  },


}
</script>