import Api from "@/share/api";

const protocols = [
    {
        id: 4,
        innerNumber: '788/458',
        patientId: 1,
        dateOfAppearance: '11.07.1484',
        doctorId: 2,
        diagnosis: {
            id: 2,
            code: 'MT-799',
            title: 'Заболевание другое'
        },
    },
    {
        id: 5,
        innerNumber: '788/965',
        patientId: 1,
        dateOfAppearance: '12.08.1484',
        doctorId: 3,
        diagnosis: {
            id: 3,
            code: 'MT-127',
            title: 'Заболевание  ваще другое'
        },
    },
    {
        id: 6,
        innerNumber: '788/127',
        patientId: 2,
        dateOfAppearance: '10.09.1484',
        doctorId: 1,
        diagnosis: {
            id: 1,
            code: 'MT-784',
            title: 'Заболевание такое то'
        },
    }
]

export default class ProtocolApi extends Api {

    static async getAllProtocolsByPatientId(patientId) {
        // const response = await fetch(`${AuthApi.basePath}/login/`, {
        //     method: 'POST',
        //     body: {id: doctorId}
        // })

        return await new Promise((res) => {
            setTimeout(() => {
                res(protocols.filter(protocol => protocol.patientId === patientId))
            }, 1000)
        })
    }

    static async getProtocolById(protocolId) {
        return await new Promise((res) => {
            setTimeout(() => {
                res(protocols.find(protocol => protocol.id === protocolId))
            }, 1000)
        })
    }

    static async createProtocol(body) {
        console.log(body)
    }

    static async importProtocol(name, file) {
        const formData = new FormData()
        formData.set('excel', file)
        formData.set('data_set_name', name)

        return await fetch(`${ProtocolApi.basePath}/import_excel/`, {
            method: 'POST',
            body: formData
        })
    }
}
