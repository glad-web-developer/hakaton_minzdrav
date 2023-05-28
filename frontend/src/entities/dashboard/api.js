import Api from "@/share/api";


export default class DashboardApi extends Api {


    static async getAllDashboards(page) {
        const response = await fetch(`${DashboardApi.basePath}/dashboards/?page=${page}`)
        return response.json()
    }

    static async getDashboardById(id) {
        const response = await fetch(`${DashboardApi.basePath}/dashboards/${id}/`)
        return response.json()
    }

    static async createDashboard(title, widgets) {
        return await fetch(`${DashboardApi.basePath}/dashboards/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: title,
                widgets: widgets,
            })
        })
    }

    static async deleteDashboard(id) {
        return await fetch(`${DashboardApi.basePath}/dashboards/${id}/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
        })
    }

    static async getAllWidgets() {
        const response = await fetch(`${DashboardApi.basePath}/dashboards/widgets/`)
        return response.json()
    }

}
