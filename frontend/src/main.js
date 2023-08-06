import {createApp} from 'vue';

import App from './App.vue';
import {createRouter, createWebHistory} from 'vue-router';
import LoginForm from '@/views/LoginForm.vue';
import MachinesList from '@/components/MachinesList.vue';
import AppDashboard from '@/components/AppDashboard.vue';
import ErrorPage from '@/views/ErrorPage.vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import "bootstrap";
import AdminDashboard from '@/views/AdminDashboard.vue';
import UserDashboard from "@/views/UserDashboard.vue";
import EditMachines from "@/views/EditMachines.vue";
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'primevue/resources/themes/saga-blue/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';
import RemoveAddMachine from "@/views/RemoveAddMachine.vue";
import AddRemoveEmployee from "@/views/AddRemoveEmployee.vue";
import UserProfile from "@/views/UserProfile.vue";
import ProfileEdit from "@/views/ProfileEdit.vue";
import MachineStatistics from "@/components/MachineStatistics.vue";
import AppMessages from "@/views/AppMessages.vue";
import EmpOverview from "@/views/EmpOverview.vue";
import UserMessages from "@/views/UserMessages.vue";
import AdminProfile from "@/views/AdminProfile.vue";
import UserProfileEdit from "@/views/UserProfileEdit.vue";
import LogsOverview from "@/views/LogsOverview.vue";


const routes = [

    {
        path:'/applogs',
        component: LogsOverview,
        meta:{requiresAuth: true}

    },

    {
        path:'/usermessages',
        component: UserMessages,
        meta:{ requiresAuth: true}

    },
    {
        path:'/employees',
        component: EmpOverview,
        meta:{ requiresAuth: true}


    },
    {
        path: '/messages',
        component: AppMessages,
        meta: {requiresAuth: true}

    },


    {
        path: '/reports',
        component: MachineStatistics,
        meta: {
            requiresAuth: true
        }

    },
    {
        path: '/userprofile',
        component: UserProfile,
        meta: {requiresAuth: true},

    },
     {
        path: '/adminprofile',
        component: AdminProfile,
        meta: {requiresAuth: true},

    },


    {
        path: '/profileedit',
        component: ProfileEdit,
        meta: {requiresAuth: true},
    },
    {
        path: '/userprofileedit',
        component: UserProfileEdit,
        meta: {requiresAuth: true},
    },

    {
        path: '/addremoveemployee',
        component: AddRemoveEmployee,
        meta: {requiresAuth: true},
    },
    {
        path: '/removeaddmachine',
        component: RemoveAddMachine,
        meta: {requiresAuth: true},

    },
    {
        path: '/',
        component: LoginForm,

    },
    {
        path: '/machines',
        component: MachinesList,
        meta: {requiresAuth: true}
    },
    {
        path: '/dashboard',
        component: AppDashboard,
        meta: {requiresAuth: true}
    },
    {
        path: '/error',
        component: ErrorPage
    },
    {
        path: '/admindashboard',
        name: 'AdminDashboard',
        component: AdminDashboard,
        meta: {requiresAuth: true}
    },
    {
        path: '/userdashboard',
        component: UserDashboard,
        meta: {requiresAuth: true}
    },

    {
        path: '/editmachines',
        component: EditMachines,
        meta: {requiresAuth: true}

    },


    {
        path: '/admindashboard',
        name: 'AdminDashboard',
        component: AdminDashboard,
        beforeEnter: (to, from, next) => {
            const isAdmin = localStorage.getItem('role') === 'admin';
            if (!isAdmin) {
                next('/');
            } else {
                next();
            }
        },
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});


const app = createApp(App);
app.use(router).mount('#app');
