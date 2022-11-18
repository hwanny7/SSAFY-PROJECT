import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginView from '@/views/LoginView'
import SignUpView from '@/views/SignUpView'
import ProfileView from '@/views/ProfileView'
import CollectionCreate from '@/views/Collection/CollectionCreate'




Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/:id',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/CollectionCreate',
    name: 'CollectionCreate',
    component: CollectionCreate
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
