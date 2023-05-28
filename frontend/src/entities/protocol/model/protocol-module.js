import ProtocolApi from "@/entities/protocol/api";

export default {
    state: () => ({
        currentProtocolId: 1,
        isLoading: false,
        protocols: [],
        packExcelSrc: null,
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
        },
        setProtocolPacks(state, payload) {
            state.protocols = payload
        },
        setPackExcelSrc(state, payload) {
            state.packExcelSrc = payload
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
        async changePackProtocol({commit}, payload) {
            const response = await ProtocolApi.getPackProtocol(payload)
            commit('setProtocolPacks', response.data.items)
            commit('changeCurrentProtocol', {id: response.data.items.at(0)?.id ?? -1})
            commit('setPackExcelSrc', response.data.excelIn)
        }
    },
    getters: {
        getCurrentProtocol(state) {
            return state.protocols.find(protocol => protocol.id === state.currentProtocolId)
        },
        isEmptyProtocols(state) {
            return state.protocols.length === 0
        }
    }
}

