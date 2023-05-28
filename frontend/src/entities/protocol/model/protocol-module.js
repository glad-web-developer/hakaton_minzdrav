import ProtocolApi from "@/entities/protocol/api";

export default {
    state: () => ({
        currentProtocolId: 1,
        isLoading: false,
        protocols: [
            {
                id: 1,
                innerNumber: '788/566',
                patientId: 1,
                dateOfAppearance: '10.07.1484',
                doctorId: 1,
                diagnosis: {
                    id: 1,
                    code: 'MT-784',
                    title: 'Заболевание такое то'
                },
            },
            {
                id: 2,
                innerNumber: '788/586',
                patientId: 1,
                dateOfAppearance: '10.08.1484',
                doctorId: 1,
                diagnosis: {
                    id: 1,
                    code: 'MT-784',
                    title: 'Заболевание такое то'
                },
            },
            {
                id: 3,
                innerNumber: '788/466',
                patientId: 1,
                dateOfAppearance: '10.09.1484',
                doctorId: 1,
                diagnosis: {
                    id: 1,
                    code: 'MT-784',
                    title: 'Заболевание такое то'
                },
            }
        ]
    }),
    mutations: {
        changeCurrentProtocol(state, payload) {
            state.currentProtocolId = payload.id
        },
        addProtocol(state, payload) {
            state.protocols.push(payload.protocol)
        },
        removeProtocol(state, payload) {
            state.protocols = state.protocols.filter(protocol => protocol.id !== payload.protocolId)
        }
    },
    actions: {
        async addProtocol({commit, state}, payload) {
            let protocol = state.protocols.find(protocol => protocol.id === payload.protocolId)

            if (!protocol) {
                state.isLoading = true
                protocol = await ProtocolApi.getProtocolById(payload.protocolId)
                commit('addProtocol', {protocol})
                commit('changeCurrentProtocol', {id: protocol.id})
                state.isLoading = false
            } else {
                commit('changeCurrentProtocol', {id: protocol.id})
            }
        },
        async changePackProtocol({commit, state}, payload) {
            const response = await ProtocolApi.getPackProtocol(payload.id)

        }
    },
    getters: {
        getCurrentProtocol(state) {
            return state.protocols.find(protocol => protocol.id === state.currentProtocolId)
        },
    }
}

