import Api from "@/share/api";

const TemplateType = [{
    id: 1, title: 'Excel таблица'
}, {
    id: 2, title: 'Список'
},]

const AggregateFunctionType = {
    'SUM': {
        id: 1, title: 'Сумма'
    }, 'AVG': {
        id: 2, title: 'Среднее арифметическое'
    },
}

const templates = [{
    id: 1,
    type: TemplateType.TableExcel,
    title: 'Отчет по больничным работников',
    fields: [{field: 'id', aggregateFunction: null}, {
        field: 'first_name',
        aggregateFunction: null
    }, {field: 'last_name', aggregateFunction: null}, {
        field: 'count_ill_day',
        aggregateFunction: AggregateFunctionType.SUM
    },]
}, {
    id: 2,
    type: TemplateType.TableExcel,
    title: 'Отчет еще какой то',
    table_id: 1,
    fields: [{field: 'id', aggregateFunction: null}, {
        field: 'first_name',
        aggregateFunction: null
    }, {field: 'last_name', aggregateFunction: null}, {
        field: 'count_ill_day',
        aggregateFunction: AggregateFunctionType.SUM
    },],
},]

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
    // const response = await fetch(`${AuthApi.basePath}/login/`, {
    //     method: 'POST',
    //     body: {id: doctorId}
    // })


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
