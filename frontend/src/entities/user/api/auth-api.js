import Api from "@/share/api";
import CookieHelper from "@/app/plugins/cookieHelper";

export default class AuthApi extends Api {
    static async login(login, password) {
        const response = await fetch(`${AuthApi.basePath}/login/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': CookieHelper.getCookie('csrftoken'),
            },
            body: JSON.stringify({
                login: login,
                pas: password
            })
        })
        const data = await response.json();
        CookieHelper.setCookie('sessionid', data.sessionid, {'max-age': 31536000});
        CookieHelper.setCookie('csrftoken', data.csrf, {'max-age': 31536000});
        return response.status === 200
    }

    static async logout() {
        const response = await fetch(`${AuthApi.basePath}/login/`)
        return response.status === 200
    }

    static async relogin() {
        const session_key =  CookieHelper.getCookie('sessionid');
        const response = await fetch(
            `${AuthApi.basePath}/check_user/${session_key}/`,
            {
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': CookieHelper.getCookie('sessionid'),
                },
            }
        )
        return response.status === 200
    }
}
