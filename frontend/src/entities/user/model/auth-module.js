import router from "@/app/router";
import {AuthApi} from "@/entities/user/api";

export default {
    state: () => ({
        isAuthenticated: false,
        isAuthError: false,
    }),
    mutations: {
        authorize(state) {
            state.isAuthenticated = true
            state.isAuthError = false
        },

        raiseError(state) {
            state.isAuthenticated = false
            state.isAuthError = true
        },

        resetAuthError(state) {
            state.isAuthError = false
        },

        deauthorize(state) {
            state.isAuthenticated = false
            state.isAuthError = false
        }
    },
    actions: {
        async login({commit}, payload) {
            const isSuccess = await AuthApi.login(payload.login, payload.password)

            if (isSuccess) {
                commit('authorize')
                await router.push({name: 'home'})

            } else {
                commit('raiseError')
            }
        },

        async relogin({commit}) {
            const isSuccess = await AuthApi.relogin()

            if (isSuccess) {
                commit('authorize')
                 await router.push({name: 'home'})
            } else {
                await router.push({name: 'login'})
            }
        },

        async logout({commit}) {
            await AuthApi.logout()
            commit('deauthorize')
            await router.push({name: 'login'})
        }
    },
    getters: {}
}
