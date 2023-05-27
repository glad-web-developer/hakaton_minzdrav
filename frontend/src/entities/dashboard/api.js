import Api from "@/share/api";

const dashboards = [
    {
        id: 1,
        title: 'Гепатит вариант 1',
        widgets: [
            {
                id: 1,
                component: 'MorbidityCChartWidget',
                title: 'График гепатит C',
                cols: 10,
                x: 150,
                y: 150,
            },
            {
                id: 2,
                component: 'MorbidityBChartWidget',
                title: 'График гепатит B',
                cols: 10,
                x: 0,
                y: 300,
            }
        ]
    },
    {
        id: 2,
        title: 'Гепатит вариант 2',
        widgets: [
            {
                id: 1,
                component: 'MorbidityCChartWidget',
                title: 'График гепатит C',
                cols: 10,
                x: 0,
                y: 0,
            },
            {
                id: 2,
                component: 'MorbidityBChartWidget',
                title: 'График гепатит B',
                cols: 10,
                x: 400,
                y: 400,
            }
        ]
    }
]

export default class DashboardApi extends Api {

    // eslint-disable-next-line no-unused-vars
    static async createDashboard(dashboard) {
        // const response = await fetch(`${AuthApi.basePath}/login/`, {
        //     method: 'POST',
        //     body: {id: doctorId}
        // })
    }

    static async getAllDashboards() {
        return new Promise(res => {
            setTimeout(() => {
                res(dashboards)
            }, 1500)
        })
    }

    static async getDashboardById(id) {
        return new Promise(res => {
            setTimeout(() => {
                res(dashboards.find(dashboard => dashboard.id === id))
            }, 1500)
        })
    }

    // eslint-disable-next-line no-unused-vars
    static async saveDashboard(data) {
        return undefined
    }

}
