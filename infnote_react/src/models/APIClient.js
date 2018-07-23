import axios from 'axios'
import Cookies from 'universal-cookie'

import { API_HOST } from 'config'

// import { alertAction } from 'models/actions'
// import { AlertStore } from 'models'



class APIClient {
    constructor() {
        this.client = axios.create({
            baseURL: API_HOST,
        })
        this.client.defaults.headers.common['Content-Type'] = 'application/json'
        this.cookies = new Cookies()

        const token = this.loadToken()
        if (token) {
            this.client.defaults.headers.common['Authorization'] = token
        }
    }

    // catchError = error => {
    //     AlertStore.dispatch(alertAction({
    //         open: true,
    //         title: 'Error',
    //         content: 'error'
    //     }))
    //     console.log(error.response.data)
    //     return error
    // }

    clearToken() {
        this.cookies.remove('token')
    }

    loadToken() {
        return this.cookies.get('token')
    }

    authorize(email, password) {
        return this.client.post('/api-token-auth/', {
            email: email,
            password: password,
        }).then(response => {
            const token = 'JWT ' + response.data.token
            this.cookies.set('token', token, { path: '/', maxAge: 60 * 60 * 24 * 30 })
            this.client.defaults.headers.common['Authorization'] = token
            return this.client.get('/user/')
        })
    }

    register(user) {
        return this.client.post('/user/create/', user)
    }

    user() {
        if (this.loadToken()) {
            return this.client.get('/user/')
        }
        return null
    }

    posts(category = '/', page = 1) {
        let url = '/post/list/?category=' + category + '&page=' + page
        return this.client.get(url)
    }

    retrievePost(id) {
        return this.client.get('/post/' + id)
    }

    retrieveReplies(id, page = 1) {
        return this.client.get('/post/' + id + '/replies/?page=' + page)
    }

    sendPost(post) {
        return this.client.post('/post/', post)
    }

    categories() {
        return this.client.get('/category/list/')
    }

    coins(value) {
        return this.client.get('/wallet/coins/?confirmed=0&value=' + value)
    }

    sendUserinfo(data) {
        return this.client.post('/user/info/', data)
    }
}

export default new APIClient()
