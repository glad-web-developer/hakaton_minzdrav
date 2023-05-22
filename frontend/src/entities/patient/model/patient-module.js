export default {
    state: () => ({
        id: 1,
        firstName: 'Иван',
        secondName: 'Иванов',
        patronymic: 'Иванович'
    }),
    mutations: {},
    actions: {},
    getters: {
        getPatientFullName(state) {
            return `${state.secondName} ${state.firstName} ${state.patronymic}`
        },
        getPatientShortFullName(state) {
            return `${state.secondName} ${state.firstName.at(0)}. ${state.patronymic.at(0)}.`
        }
    }
}

