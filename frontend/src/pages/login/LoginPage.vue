<template>
  <div class="w-100 h-100 bg-fon px-3 pt-2 pb-5  d-flex flex-column  blue  lighten-3 align-self-center justify-center">
    <div class="row ">
      <div class="col-12 col-sm-8 col-md-6 col-lg-5 col-xl-3 m-auto">
        <div class="card shadow-lg p-3 text-center">

          <h2><b>МИС Главного врача</b></h2>

          <form method="post" class="card-body forma-vhoda text-center" action="#">

            <div class="mb-3">
              <v-text-field
                  clearable
                  name="login"
                  label="Логин"
                  @keydown.enter="login"
                  v-model="userForm.login"
              />

            </div>

            <div class="mb-3">
              <v-text-field
                  clearable
                  name="pas"
                  type="password"
                  label="Пароль"
                  @keydown.enter="login"
                  v-model="userForm.password"
              />
            </div>

            <v-btn
                color="blue lighten-1"
                dark
                class="px-5"
                @click="login"
            >
              Войти
            </v-btn>

          </form>
        </div>
      </div>
    </div>

    <v-snackbar
        v-model="$store.state.auth.isAuthError"
        multi-line
    >
      <span class="red--text">Неправильно введен логин или пароль</span>

      <template v-slot:action="{ attrs }">
        <v-btn
            text
            v-bind="attrs"
            @click="$store.commit('resetAuthError')"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>

</template>

<script>

export default {
  name: "LoginView",
  components: {},
  data() {
    return {
      userForm: {
        login: "",
        password: "",
      },
    }
  },

  methods: {
    async login() {
      await this.$store.dispatch('login', {
        login: this.userForm.login,
        password: this.userForm.password,
      })
    }
  },

}
</script>

<style scoped lang="scss">

.tab-content {
  border: #dee2e6 1px solid;
}


.bg-fon {
  background-image: url("./assets/login-page-background.jpg");
  background-size: cover;
}

.logo {
  width: 100px;
}

.logo-as {
  height: 70px;

}
</style>
