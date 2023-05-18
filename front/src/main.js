import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from '@/plugins/vuetify'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import VueCookie from 'vue-cookie'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  VueCookie,
  vuetify,
  render: h => h(App)
}).$mount('#app')
