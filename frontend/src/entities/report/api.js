import Api from "@/share/api";

const TemplateType = [{
    id: 1, title: 'Excel таблица'
}, {
    id: 2, title: 'Список'
},]

const AggregateFunctionType = {
    'SUM': {
        id: 1, title: 'Сумма'
    },
    'AVG': {
        id: 2, title: 'Среднее арифметическое'
    },
}

const templates = [
    {id: 1, title: 'Отчет А', src: './file_abosus.png'},
    {id: 2, title: 'Отчет B', src: './file_abosus.png'},
    {id: 3, title: 'Отчет C', src: './file_abosus.png'},
]

const tables = [{
    id: 1, title: 'Доктора', fields: [{
        id: 1,
        title: 'Идентификатор',
        availableAggregateFunctions: [AggregateFunctionType.SUM, AggregateFunctionType.AVG]
    }, {id: 2, title: 'Имя', availableAggregateFunctions: []}, {
        id: 3,
        title: 'Фамилия',
        availableAggregateFunctions: []
    },]
}, {
    id: 2, title: 'Пациенты', fields: [{
        id: 1,
        title: 'Идентификатор',
        availableAggregateFunctions: [AggregateFunctionType.SUM, AggregateFunctionType.AVG]
    }, {id: 2, title: 'Имя', availableAggregateFunctions: []}, {
        id: 3,
        title: 'Фамилия',
        availableAggregateFunctions: []
    },]
}]

export default class ReportApi extends Api {

    static async getAllTables() {
        return await new Promise((res) => {
            setTimeout(() => {
                res(tables)
            }, 1000)
        })
    }

    static async getAllTemplates() {
        return await new Promise((res) => {
            setTimeout(() => {
                res(templates)
            }, 1000)
        })
    }

    static async getAllTemplateTypes() {
        return await new Promise((res) => {
            setTimeout(() => {
                res(TemplateType)
            }, 1000)
        })
    }

    // eslint-disable-next-line no-unused-vars
    static async createTemplate(data) {
        console.log(data)
    }

    // eslint-disable-next-line no-unused-vars
    static async createReport(templateId) {

    }
}
