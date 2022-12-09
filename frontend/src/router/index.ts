import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import AddTodoView from '@/views/AddTodoView.vue'

const routes: Array<RouteRecordRaw> = [
  {path: '/', component: HomeView},
  {path: '', component: HomeView},
  {path: '/login', component: LoginView},
  {path: '/register', component: RegisterView},
  {path: '/add-todo', component: AddTodoView},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
