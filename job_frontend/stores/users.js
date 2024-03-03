import {defineStore} from "pinia";
// defining a state management for users with Pinia
export const useUserStore = defineStore({
    id: "user",
    state: () => ({
        user: {
            isAuthenticated: false,
            email: null,
            token: null,
        }
    }),
    actions:{
        initStore() {
            this.user.isAuthenticated = false
        //     if we stored the token into the localstorage and the user is authenticated
            if (localStorage.getItem("user.token")) {
                this.user.token = localStorage.getItem("user.token")
                this.user.email = localStorage.getItem("user.email")
                this.user.isAuthenticated = true

                console.log("Initialize user:", this.user)
            }
        },
        // Loging in
        setToken(token, email) {
            console.log("setToken", token, email)

            this.user.token = token
            this.user.email = email
            this.user.isAuthenticated = true
        //     Storing info into our local storage
            localStorage.setItem("user.token", token)
            localStorage.setItem("user.email", email)
        },
        // Loging out
        removeToken() {
            console.log("removeToken")

            this.user.token = null
            this.user.email = null
            this.user.isAuthenticated = false

            localStorage.setItem("user.token", "")
            localStorage.setItem("user.email", "")
        }
    }
})