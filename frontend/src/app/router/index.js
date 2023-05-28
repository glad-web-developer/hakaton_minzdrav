import Vue from 'vue'
import VueRouter from 'vue-router'
import store from "@/app/store";
import {DashboardConstructorPage, DashboardPage, HomePage, LoginPage, MainLayout, NotFoundPage} from "@/pages";

Vue.use(VueRouter)

const routes = [

    {
        path: '/',
        component: MainLayout,
        children: [
            {
                name: 'home',
                component: HomePage,
                path: '/'
            },
            {
                path: '/dashboard-constructor',
                component: DashboardConstructorPage,
                name: 'dashboard-constructor'
            },
            {
                path: '/dashboard/:id',
                component: DashboardPage,
                name: 'dashboard',
                props: true,
            }
        ]
    },
    {
        path: '/login',
        name: 'login',
        component: LoginPage
    },
    {
        path: '*',
        name: 'page404',
        component: NotFoundPage
    },

]

const router = new VueRouter({
    mode: 'history',
    routes
})

router.beforeResolve((to, from, next) => {
    const isAuthenticated = store.state.auth.isAuthenticated

    if (to.name !== 'login' && !isAuthenticated) next({name: 'login'})
    else next()
})

export default router
