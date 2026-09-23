import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/vacinacao',
    name: 'Vacinação',
    // route level code-splitting
    // this generates a separate chunk (vacinacao.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "vacinacao" */ '../views/Vacinacao.vue')
  },
  {
    path: '/indigenas',
    name: 'Indígenas',
    // route level code-splitting
    // this generates a separate chunk (indigenas.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "indigenas" */ '../views/Indigenas.vue')
  },
  {
    path: '/variantes',
    name: 'Variantes',
    // route level code-splitting
    // this generates a separate chunk (variantes.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "variantes" */ '../views/Variantes.vue')
  },
  {
    path: '/ocupacao',
    name: 'Ocupação',
    // route level code-splitting
    // this generates a separate chunk (ocupacao.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "ocupacao" */ '../views/Ocupacao.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
