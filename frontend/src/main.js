import Vue from 'vue'
import App from './app/App.vue'
import router from './app/router'
import store from './app/store'
import vuetify from '@/app/plugins/vuetify'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

import VueDraggableResizable from 'vue-draggable-resizable'
import 'vue-draggable-resizable/dist/VueDraggableResizable.css'

Vue.component('vue-draggable-resizable', VueDraggableResizable)

Vue.config.productionTip = false


new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount('#app')
