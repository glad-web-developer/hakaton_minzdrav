<template>
  <div class="w-100 h-100 bg-fon px-3 pt-2 pb-5  d-flex flex-column  blue  lighten-3 align-self-center justify-center">
    <div class="row ">
      <div class="col-12 col-sm-8 col-md-6 col-lg-5 col-xl-3 m-auto">
        <div class="card shadow-lg p-3 text-center">

          <h2><b>МИС Главного врача</b></h2>


          <form method="post" class="card-body forma-vhoda text-center" action="#">


            <div class="mb-3">
              <v-text-field name="login" label="Логин" @keydown.enter="login"
                            v-model="userForm.login"></v-text-field>
            </div>

            <div class="mb-3">
              <v-text-field name="pas" type="password" label="Пароль" @keydown.enter="login"
                            v-model="userForm.pas"></v-text-field>
            </div>

            <v-btn
                color="blue lighten-1"
                dark
                class="px-5"
                @click="login"
            >Войти
            </v-btn>

          </form>

        </div>
      </div>
    </div>

  </div>

</template>

<script>


import LOCAL_CONFIG from "@/store/LOCAL_CONFIG";
import CookieHelper from "@/plugins/cookieHelper";

export default {
  name: "LoginView",
  components: {},
  data() {
    return {
      userForm: {
        login: "",
        pas: ""
      },
    }
  },

  methods: {
    async login() {

      //костыль
      CookieHelper.setCookie('sessionid', "111", {'max-age': 31536000});
      CookieHelper.setCookie('csrftoken', "111", {'max-age': 31536000});
      window.location.href = "/";


      try {
        const url = LOCAL_CONFIG.urls.login;
        const response = await fetch(url, {
          method: 'POST',
          body: JSON.stringify(this.userForm),
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': CookieHelper.getCookie('csrftoken')
          },
        });
        if (response.status === 200) {
          const responseJson = await response.json();
          CookieHelper.setCookie('sessionid', responseJson.sessionid, {'max-age': 31536000});
          CookieHelper.setCookie('csrftoken', responseJson.csrf, {'max-age': 31536000});
          window.location.href = "/";
        } else {
          this.$emit('showAlert', 'Ошибка авторизации');
        }
      } catch (e) {
        this.$emit('showAlert', "Ошибка при обращение к серверу");
      }

    }
  },

  async created() {
    this.$emit('loadComplete',);
  },


}
</script>

<style scoped lang="scss">

.tab-content {
  border: #dee2e6 1px solid;
}


.bg-fon {
  background-image: url("../assets/fon.jpg");
  background-size: cover;
}

.logo {
  width: 100px;
}

.logo-as {
  height: 70px;

}
</style>