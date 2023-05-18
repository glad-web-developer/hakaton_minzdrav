let baseUrl = 'http://127.0.0.1:8000';
// let baseUrl = '';
export default {
    baseUrl: baseUrl,

     urls: {
        // пользователи
        login: `${baseUrl}/api/login/`,
        checkUser: `${baseUrl}/api/check_user/`,
        logout: `${baseUrl}/api/logout/`,

    },

    yesNoList: [
        {'label': 'Да', id: true},
        {'label': 'Нет', id: false},
    ],

    yesNoNullList: [
        {'label': '-', id: ''},
        {'label': 'Да', id: true},
        {'label': 'Нет', id: false},
    ],

    sexList: [
        {'label': 'Неизвестен', id: 0},
        {'label': 'Мужской', id: 1},
        {'label': 'Женский', id: 2},
        {'label': 'Интерсекс', id: 3},
    ],


}