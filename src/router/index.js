import { createRouter, createWebHistory } from 'vue-router'
import { ElMessage } from 'element-plus'
import { nextTick } from 'vue'

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import('../views/Home.vue'),
            meta: {
                title: '首页'
            }
        },
        {
            path: '/model1',
            name: 'model1',
            component: () => import('../views/Model1.vue'),
            meta: {
                needRefresh: true
            }
        },
        {
            path: '/model2',
            name: 'model2',
            component: () => import('../views/Model2.vue'),
            meta: {
                needRefresh: true
            }
        },
        {
            path: '/model3',
            name: 'model3',
            component: () => import('../views/Model3.vue'),
            meta: {
                needRefresh: true
            }
        },
        {
            path: '/history',
            name: 'history',
            component: () => import('../views/History.vue'),
            meta: {
                keepAlive: true,
                title: '发展历程'
            }
        },
        {
            path: '/demo',
            name: 'demo',
            component: () => import('../views/Demo.vue'),
            meta: {
                keepAlive: true,
                noRefresh: true
            }
        }
    ]
})

// 添加全局导航守卫
router.beforeEach((to, from, next) => {
    // 如果正在分析中，阻止导航
    const demoComponent = document.querySelector('.demo-page')?.__vue__;
    if (demoComponent?.analyzing) {
        ElMessage.warning('请等待分析完成');
        next(false);
        return;
    }
    next();
});

// 添加导航后的钩子
router.afterEach((to, from) => {
    // 如果需要刷新且不是首次访问，且是不同页面间的跳转，且目标页面不是demo
    if (to.meta.needRefresh && from.name && to.name !== from.name && to.name !== 'demo') {
        nextTick(() => {
            setTimeout(() => {
                window.location.reload();
            }, 100);
        });
    }
});

export default router 