<template>
  <div class="w-100 h-100 bg-fon px-3 pt-2 pb-5  d-flex flex-column  blue  lighten-3 align-self-center justify-center">
    <div class="row ">
      <div class="col-12 col-sm-8 col-md-6 col-lg-5 col-xl-3 m-auto">
        <div class="card shadow-lg p-3 text-center">

          <h2><b>МИС Главного врача</b></h2>


          <form method="post" class="card-body forma-vhoda text-center" action="#">


            <v-btn
                color="light-blue darken-4"
                dark
                class="px-5 mb-5 d-block w-100"
                @click="loginChiefDoctor"
            >Войти как глав. врач
            </v-btn>

            <v-btn
                color="light-blue darken-4"
                dark
                class="px-5 mb-5 d-block w-100"
                @click="loginDoctor"
            >Войти как врач
            </v-btn>

            <v-btn
                color="light-blue darken-4"
                dark
                class="px-5 mb-5 d-block w-100"
                @click="loginPatient"
            >Войти как пациент
            </v-btn>

            <v-btn
                color="light-blue darken-4"
                dark
                class="px-5  d-block w-100"
                @click="loginInsurance"
            >Войти как соц. страх
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

  methods: {
    //для удобства демонстрации и проверки, все логины и пароли зашиты в коде. Авторизация на беке работает. В продакшене будует форма авторизации
    async loginChiefDoctor() {
      this.login('ivanov', 'Serenity321')
    },

     async loginDoctor() {
       await this.login('petrov', 'Serenity321')
    },

     async loginPatient() {
      await this.login('924375053', 'Serenity321')
    },

      async loginInsurance() {
      await this.login('sidorov_soz', 'Serenity321')
    },


    async login(login, pas) {

      const userForm = {
        login: login,
        pas: pas,
      }


      try {
        const url = LOCAL_CONFIG.urls.login;
        const response = await fetch(url, {
          method: 'POST',
          body: JSON.stringify(userForm),
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
        }
         else if (response.status === 400){
            this.$emit('showAlert', await response.text());
        }

        else {
          this.$emit('showAlert', 'Непредвиденная ошибка авторизации');
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