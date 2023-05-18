import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from "@/views/HomeView";
import LoginView from "@/views/LoginView";

Vue.use(VueRouter)

const routes = [


     {
        path: '/login',
        name: 'loginView',
        component: LoginView
    },

     {
        path: '/',
        name: 'homeView',
        component: HomeView
    },

     {
        path: '*',
        name: 'page404',
        component: HomeView
    },

]

const router = new VueRouter({
    routes
})

export default router
