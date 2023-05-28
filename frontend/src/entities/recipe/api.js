import BaseApi from '@/share/api'

const recipe = {
    src: './path-to-recipe-file.png'
}

export class RecipeApi extends BaseApi {

    // eslint-disable-next-line no-unused-vars
    static async createRecipe(recipeForm, medications) {
        return new Promise(res => {
            setTimeout(() => {
                res(recipe)
            }, 1000)
        })
    }

}
