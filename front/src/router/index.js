import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginView from '@/views/LoginView'
import SignUpView from '@/views/SignUpView'
import ProfileView from '@/views/ProfileView'
import CollectionCreate from '@/views/Collection/CollectionCreate'
import AllCollection from '@/views/Collection/AllCollection'
import CollectionRevise from '@/views/Collection/CollectionRevise'
import testView from '@/views/testView'
import HomeView from '@/views/HomeView'
import LikeView from '@/views/LikeView'






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
    path: '/collectioncreate',
    name: 'CollectionCreate',
    component: CollectionCreate
  },
  {
    path: '/allcollection',
    name: 'AllCollection',
    component: AllCollection,
  },
  {
    path: '/testView',
    name: 'testView',
    component: testView,
  },
  {
    path: '/revise/:pk',
    name: 'CollectionRevise',
    component: CollectionRevise,
  },
  {
    path: '/home',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/:id/like',
    name: 'Like',
    component: LikeView
  },
  { //주소 바인딩한 값은 무조건 마지막에 두는 게 좋음. :id는 string이기 때문에 주소가 바뀔 때 모든 주소가 id값과 같다고 판단한다.
    path: '/:id',
    name: 'ProfileView',
    component: ProfileView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
