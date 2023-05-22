import Api from "@/share/api";

export default class AuthApi extends Api {
    static async login(login, password) {
        const response = await fetch(`${AuthApi.basePath}/login/`, {
            method: 'POST',
            body: {login, password}
        })

        return response.status === 200
    }

    static async relogin() {
        const response = await fetch(`${AuthApi.basePath}/check_user`, {
            mode: 'no-cors'
        })
        return response.status === 200
    }
}
