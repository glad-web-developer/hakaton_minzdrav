import Api from "@/share/api";

export default class AuthApi extends Api {
    static async login(login, password) {
        const response = await fetch(`${AuthApi.basePath}/login/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                login: login,
                pas: password
            })
        })

        return response.status === 200
    }

    static async logout() {
        const response = await fetch(`${AuthApi.basePath}/login/`)
        return response.status === 200
    }

    static async relogin() {
        const response = await fetch(`${AuthApi.basePath}/check_user/`)
        return response.status === 200
    }
}
