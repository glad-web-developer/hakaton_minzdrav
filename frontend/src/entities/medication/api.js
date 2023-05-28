import BaseApi from '@/share/api'

const medications = [
    {id: 1, title: 'Таблетка 1'},
    {id: 2, title: 'Таблетка 2'},
    {id: 3, title: 'Таблетка 3'},
    {id: 4, title: 'Таблетка 4'},
]

export class MedicationApi extends BaseApi {
    static async getAllMedication() {
        return new Promise(res => {
            setTimeout(() => {
                res(medications)
            }, 1000)
        })
    }
}
