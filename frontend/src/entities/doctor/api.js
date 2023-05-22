import Api from "@/share/api";

const doctors = [
    {
        id: 1,
        firstName: 'Анна',
        secondName: 'Мухамедова',
        patronymic: 'Алексеевна',
    },
    {
        id: 2,
        firstName: 'Ирина',
        secondName: 'Горбачева',
        patronymic: 'Сергеевна',
    },
    {
        id: 3,
        firstName: 'Николай',
        secondName: 'Бурзедский',
        patronymic: 'Иванович',
    },
]

export default class DoctorApi extends Api {

    static async getDoctorById(doctorId) {
        // const response = await fetch(`${AuthApi.basePath}/login/`, {
        //     method: 'POST',
        //     body: {id: doctorId}
        // })

        return await new Promise((res) => {
            setTimeout(() => {
                res(doctors.find(doctor => doctor.id === doctorId))
            }, 1000)
        })
    }

    static async getAllDoctors() {
        return await new Promise((res) => {
            setTimeout(() => {
                res(doctors)
            }, 1000)
        })
    }
}
